def simplified_MD5_8bit_difficulty_1or2():
    printables_list = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for i in printables_list:
        x2 = ord(i)

        x3 = bin(x2)[2:]

        if len(str(x3))==7:
            x4 = x3+'0'
        if len(str(x3))==6:
            x4 = x3+'00'

        x5 = list(x4)

        a0 = 2*int((x5[0]))
        a1 = int(x5[1])

        b0 = 2*int((x5[2]))
        b1 = int(x5[3])

        c0 = 2*int((x5[4]))
        c1 = int(x5[5])

        d0 = 2*int((x5[6]))
        d1 = int(x5[7])

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
        print(binary_result)
        hex_result = hex(decimal_result)
        print(hex_result)

        if hex_result == '0x0':
            difficulty_2.append(hex_result)
            collisions_difficulty_2.append(i)
        if hex_result == ('0x1' or '0x2' or '0x3' or '0x4' or '0x5' or '0x6' or '0x7' or '0x8' or '0x9' or '0xa' or '0xb' or '0xc' or '0xd' or '0xe' or '0xf'):
            difficulty_1.append(hex_result)
            collisions_difficulty_1.append(i)

    print('Difficulty_1 list = ',difficulty_1)
    print('Difficulty_2 list = ',difficulty_2)
    print('Colliding inputs for difficulty 1 = ',collisions_difficulty_1)
    print('Colliding inputs for difficulty 2 = ',collisions_difficulty_2)
    
difficulty_2 = []
difficulty_1 = []     
collisions_difficulty_1 = []
collisions_difficulty_2 = []

import numpy as np
simplified_MD5_8bit_difficulty_1or2()

    


