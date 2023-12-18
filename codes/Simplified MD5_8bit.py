import numpy as np

def simplified_MD5_8bit(x1 = input('Type a single ASCII character whse hash you would like to find : ')):

    x2 = ord(x1)
    #print(x2)

    x3 = bin(x2)[2:]
    #print(x3)

    if len(str(x3))==7:
        x4 = x3+'0'
        #print(x4)
    if len(str(x3))==6:
        x4 = x3+'00'
        #print(x4)

    x5 = x4
    #print(x5)

    x6 = list(x5)
    #print(x6)

    a0 = 2*int((x6[0]))
    a1 = int(x6[1])

    b0 = 2*int((x6[2]))
    b1 = int(x6[3])

    c0 = 2*int((x6[4]))
    c1 = int(x6[5])

    d0 = 2*int((x6[6]))
    d1 = int(x6[7])

    a = a0 + a1
    #print('a == ', a)

    b = b0 + b1
    #print('b == ', b)

    c = c0 + c1
    #print('c == ', c)

    d = d0 + d1
    #print('d == ', d)
    
    F = (d ^ (b & (c ^ d)))
    G = (c ^ (d & (b ^ c)))
    H = (b ^ c ^ d)
    I = (c ^ (b | ~(d)))
    
    sines = np.abs(np.sin(np.arange(64) + 1))
    sine_randomness = [int(x) for x in np.floor(2 ** 32 * sines)]
    R= sine_randomness[0]
    
    a = (((a + F + G + H + I + R)<<7)+b)%4 
    #print("The hash value of variable a after bit_mixing is", a)
    #print()
    #print(a)
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
    #print('Difficulty_1 list ',difficulty_1)
    #print('Difficulty_2 list ',difficulty_2)'''
    
     

#print('Testing for hashes having a difficulty = 1 or, hexadecimal output starting 0x0:')
#printables_list = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#for i in printables_list:



simplified_MD5_8bit()

    


