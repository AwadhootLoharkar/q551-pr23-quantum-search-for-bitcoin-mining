import numpy as np

# Constants and Initialization
shift = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
         5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
         4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
         6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]
sines = np.abs(np.sin(np.arange(64) + 1))  # "nothing up my sleeve" randomness
sine_randomness = [int(x) for x in np.floor(2 ** 32 * sines)]

md5_block_size = 8  # Modified to 8-bit block size
md5_digest_size = 1  # Modified to 8-bit digest size


# Helper Functions

def left_rotate(x: int, y: int) -> int:
    """
    Rotate the bits of x by y places, as if x and y are 8-bit unsigned integers.
    """
    return ((x << (y & 7)) | ((x & 0xff) >> (8 - (y & 7)))) & 0xff  # Modified to 8-bit rotation


def bit_not(x: int) -> int:
    """
    The bitwise complement of x if x were represented as an 8-bit unsigned integer.
    """
    return 255 - x  # Modified to 8-bit complement


# Mixing Functions
def F(b: int, c: int, d: int) -> int:
    return d ^ (b & (c ^ d))


def G(b: int, c: int, d: int) -> int:
    return c ^ (d & (b ^ c))


def H(b: int, c: int, d: int) -> int:
    return b ^ c ^ d


def I(b: int, c: int, d: int) -> int:
    return c ^ (b | bit_not(d))


# Mixing Functions for Each Step
mixer_for_step = [F for _ in range(16)] + [G for _ in range(16)] + [H for _ in range(16)] + [I for _ in range(16)]

# Permutations of [0, ..., 15]
round_1_perm = [i for i in range(16)]
round_2_perm = [(5 * i + 1) % 16 for i in range(16)]
round_3_perm = [(3 * i + 5) % 16 for i in range(16)]
round_4_perm = [(7 * i) % 16 for i in range(16)]
msg_idx_for_step = round_1_perm + round_2_perm + round_3_perm + round_4_perm


# MD5 State Class
class MD5State:
    def __init__(self):
        """
        MD5 state initialization.
        """
        self.length: int = 0
        self.state: tuple[int, int, int, int] = (0x67, 0xef, 0x98, 0x10)  # Modified to 8-bit initial state
        self.n_filled_bytes: int = 0
        self.buf: bytearray = bytearray(md5_block_size)

    def digest(self) -> bytes:
        """
        Get the MD5 digest as bytes.
        """
        return bytes([self.state[0] & 0xff])  # Modified to return 8-bit state as bytes

    def hex_digest(self) -> str:
        """
        Get the MD5 digest as a hexadecimal string.
        """
        return format(self.state[0], '02x')  # Modified to return 8-bit state as hexadecimal string

    def process(self, byte_value: int) -> None:
        """
        Process an 8-bit input value.
        """
        assert self.n_filled_bytes < len(self.buf)

        self.buf[self.n_filled_bytes] = byte_value
        self.n_filled_bytes += 1

        if self.n_filled_bytes == md5_block_size:
            self.compress(self.buf)
            self.length += md5_block_size
            self.n_filled_bytes = 0

    def finalize(self) -> None:
        """
        Finalize the MD5 hashing process.
        """
        assert self.n_filled_bytes < md5_block_size

        self.length += self.n_filled_bytes
        self.buf[self.n_filled_bytes] = 0b10000000
        self.n_filled_bytes += 1

        n_bytes_needed_for_len = 8

        if self.n_filled_bytes + n_bytes_needed_for_len > md5_block_size:
            self.buf[self.n_filled_bytes:] = bytes(md5_block_size - self.n_filled_bytes)
            self.compress(self.buf)
            self.n_filled_bytes = 0

        self.buf[self.n_filled_bytes:] = bytes(md5_block_size - self.n_filled_bytes)
        bit_len_64 = (self.length * 8) % (2 ** 64)
        self.buf[-n_bytes_needed_for_len:] = bit_len_64.to_bytes(length=n_bytes_needed_for_len,
                                                                 byteorder='little')
        self.compress(self.buf)

    def compress(self, msg_chunk: bytearray) -> None:
        """
        Compress a block of input data using MD5.
        """
        assert len(msg_chunk) == md5_block_size
        msg_ints = [msg_chunk[i] for i in range(md5_block_size)]
        assert len(msg_ints) == 8

        a, b, c, d = self.state

        for i in range(md5_block_size):
            bit_mixer = mixer_for_step[i]
            msg_idx = msg_idx_for_step[i]
            a = (a + bit_mixer(b, c, d) + msg_ints[msg_idx] + sine_randomness[i]) % 256
            a = left_rotate(a, shift[i])
            a = (a + b) % 256
            a, b, c, d = d, a, b, c

        self.state = (
            (self.state[0] + a) % 256,
            (self.state[1] + b) % 256,
            (self.state[2] + c) % 256,
            (self.state[3] + d) % 256,
        )


# Get input character from user
user_input = input("Enter a single ASCII character: ")
if len(user_input) == 1 and ord(user_input) < 256:
    input_byte_value = ord(user_input)

    # Hashing process
    state = MD5State()
    state.process(input_byte_value)
    state.finalize()

    # Print results
    print(f"Input Character (Binary): {format(input_byte_value, '08b')}")
    print(f"MD5 Hash (Binary): {format(state.digest()[0], '08b')}")
    print(f"MD5 Hash (Hex): {state.hex_digest()}")
else:
    print("Invalid input. Please enter a single ASCII character.")
