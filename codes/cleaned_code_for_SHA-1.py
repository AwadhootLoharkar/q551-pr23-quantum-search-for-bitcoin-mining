import random
import string
import numpy as np

print('Welcome to the SHA-1 algorithm for 1 input string character')
input("Press Enter to continue...")

def simplified_SHA_1(a):
    x = ord(a)

    # Convert the ASCII value to an 8-bit binary string using NumPy
    binary_1 = np.binary_repr(x, width=8)
    
    binary_1 += '10'  # Append '10' for padding

    def findRandom():
        p = ''.join([str(random.randint(0, 1)) for _ in range(12)])
        return p

    q = findRandom()
    return binary_1, q

printables_list = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
binaries_list = []
list_to_check = []

for a in printables_list:
    binary_1, q = simplified_SHA_1(a)
    while q in list_to_check:
        binary_1, q = simplified_SHA_1(a)
    
    binaries_list.append(binary_1)
    list_to_check.append(q)

input_character = input("Enter a single ASCII character: ")
if len(input_character) == 1:
    if input_character in printables_list:
        prehash = printables_list.index(input_character)
        prehash_binary = binaries_list[prehash]
        dhash = list_to_check[prehash]
        print(f'The binary of your string character is {prehash_binary}')
        print(f'Your hash is {dhash}')
    else:
        print('Invalid character. Please enter a valid ASCII character.')
else:
    print('Error: You did not type one single ASCII character')
