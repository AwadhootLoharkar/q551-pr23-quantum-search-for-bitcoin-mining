from classiq import Model, RegisterUserInput, synthesize
from classiq.builtin_functions import ArithmeticOracle

#there will be 4 inputs with each a 2-bit value, i.e. a,b,c,d 

import numpy as np

def simplified_MD5_8bit(x1):
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
    a = (((a + (d ^ (b & (c ^ d))) + (c ^ (d & (b ^ c))) + (b ^ c ^ d) + (c ^ (b | ~(d)))  + 3614090360)<<7) + b)%4
    result = 'a == (((a + (d ^ (b & (c ^ d))) + (c ^ (d & (b ^ c))) + (b ^ c ^ d) + (c ^ (b | ~(d)))  + 3614090360)<<7) + b)%4' + ' and' + ' d == ' + str(d) + ' and' + ' a == ' + str(a) + ' and' + ' b == ' + str(b) + ' and' + ' c == ' + str(c)
    return result


    
params = ArithmeticOracle(
    expression=simplified_MD5_8bit('a'),
    definitions=dict(
        a=RegisterUserInput(size=2),
        b=RegisterUserInput(size=2),
        c=RegisterUserInput(size=2),
        d=RegisterUserInput(size=2)
    ),
    uncomputation_method="optimized",
)
model = Model()
model.ArithmeticOracle(params)
quantum_program = synthesize(model.get_model())
