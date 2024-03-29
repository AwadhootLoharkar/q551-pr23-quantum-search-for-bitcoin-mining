from classiq import Model, RegisterUserInput, synthesize, show
from classiq.builtin_functions import ArithmeticOracle
from classiq import Model, synthesize, set_constraints
from classiq.model import Constraints, TranspilerBasisGates

#there will be 4 inputs with each a 2-bit value, i.e. a,b,c,d 

import numpy as np

def simplified_MD5_8bit(x1):
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
    
    result = 'a == ((d ^ (b & (c ^ d))) + (c ^ (d & (b ^ c))) + (b ^ c ^ d) + (c ^ (b | ~(d))) + b)' + ' and' + ' d == ' + str(d) + ' and' + ' a == ' + str(a) + ' and' + ' b == ' + str(b) + ' and' + ' c == ' + str(c)
    return result


    
params = ArithmeticOracle(
    expression=simplified_MD5_8bit('b'),
    definitions=dict(
        a=RegisterUserInput(size=2),
        b=RegisterUserInput(size=2),
        c=RegisterUserInput(size=2),
        d=RegisterUserInput(size=2)
    ),
    uncomputation_method="optimized",
)

constraints = Constraints(
    max_width=20,
)

model = Model()
model.ArithmeticOracle(params)
serialized_model = model.get_model()
serialized_model = set_constraints(serialized_model, constraints)

quantum_program = synthesize(serialized_model)
show(quantum_program)
