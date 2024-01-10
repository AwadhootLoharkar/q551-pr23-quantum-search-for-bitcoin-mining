import numpy as np

def simplified_MD5_8bit(x1 = input('Type a single ASCII character whose hash you would like to find : ')):

    x2 = ord(x1)

    x3 = bin(x2)[2:]

    if len(str(x3))==7:
        x4 = x3+'0' 
    if len(str(x3))==6:
        x4 = x3+'00'

    x5 = x4

    x6 = list(x5)

    a0 = 2*int((x6[0]))
    a1 = int(x6[1])

    b0 = 2*int((x6[2]))
    b1 = int(x6[3])

    c0 = 2*int((x6[4]))
    c1 = int(x6[5])

    d0 = 2*int((x6[6]))
    d1 = int(x6[7])

    a = a0 + a1

    b = b0 + b1

    c = c0 + c1

    d = d0 + d1
    
    a = ((d ^ (b & (c ^ d))) + (c ^ (d & (b ^ c))) + (b ^ c ^ d) + (c ^ (b | ~(d))) + b) 

    print()

    d1 = d//2
    d0 = d%2
    d = d1*(2**7) + d0*(2**6)

    a1 = a//2
    a0 = a%2
    a = a1*(2**5) + a0*(2**4)

    b1 = b//2
    b0 = b%2
    b = b1*(2**3) + b0*(2**2)

    c1 = c//2
    c0 = c%2
    c = c1*(2**1) + c0*(2**0)

    decimal_result = d + a + b + c
    binary_result = bin(decimal_result)[2:]
    hex_result = hex(decimal_result)
    hash_value = str(hex_result)

    difficulty_2 = []
    difficulty_1 = []

    if hash_value == '0x00':
        difficulty_2.append(hash_value)
        difficulty_1.append
    if hash_value.startswith('0x0'):
        difficulty_1.append(hash_value)    

    print('The output in decimal is ',decimal_result)
    print('The output in binary is ', binary_result)
    print('The output in hexadecimal is ',hex_result)


simplified_MD5_8bit()

    


