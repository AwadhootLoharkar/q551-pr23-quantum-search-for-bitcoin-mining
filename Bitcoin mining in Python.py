#SHA256 Bitcoin mining in Python

from bitcoin import *
import hashlib
from hashlib import sha256

def double_SHA256(text):
    first_hash = sha256(text.encode("ascii")).digest()
    second_hash = sha256(first_hash).hexdigest()
    return second_hash
    
MAX_NONCE=100000000      # You can also use a while loop to run infinitely with no upper limit

def mine(block_number,transaction,previous_hash,prefix_zeros):
  prefix_str='0'*prefix_zeros
  for nonce in range(MAX_NONCE):
    text= str(block_number) + str(transaction) + str(previous_hash) + str(nonce)
    hash = double_SHA256(text)
    #print(hash)
    #print()
    if hash.startswith(prefix_str):
      print("Bitcoin mined with nonce value :",nonce)
      return hash
  print("Could not find a hash in the given range of upto", MAX_NONCE)

transactions='''
A->B->10
B->c->5
'''
difficulty = 6
import time as t
begin=t.time()


# Block header data (80 bytes)
block_header = b'\x00\x00\x00\x20'  # Version
block_header += bytes.fromhex('0000000000000000000000000000000000000000000000000000000000000000')  # Previous Block Hash
block_header += bytes.fromhex('0b09e8fbdce74a149b54f07e53e45ea0b785c2d25a292a21c92737d6d943bb25')  # Merkle Root
block_header += b'\x63d96b5c'  # Timestamp
block_header += b'\x1a0944e3'  # Bits (Difficulty)
block_header += b'\x1c504c2f'  # Nonce
print(block_header)

new_hash = mine(block_header,transactions,"000000000000000000006bd3d6ef94d8a01de84e171d3553534783b128f06aad",difficulty)
print("Hash value : ",new_hash)
time_taken=t.time()- begin
print("The mining process took ",time_taken,"seconds")
