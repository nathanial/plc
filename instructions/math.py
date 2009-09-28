class add(Instruction):
      code = "ADD"
      description = """
Adds a BCD value in the lower 16 bits in teh accumulator with a V-memory
location. The result resides in the accumulator.
"""     

class add_double(Instruction):
      code = "ADDD"
      description = """
Adds a BCD value in the accumulator with two consecutive V-memory
locations or an 8-digit constant. The result resides in the accumulator.
"""     

class add_real_number(Instruction):
      code = "ADDR"
      description = """
DL06 Only. Adds a real number in the accumulator with a real number
constant or a real number contains in two consecutive V-memory
locations. The result resides in the accumulator.
"""     

class subtract(Instruction):
      code = "SUB"
      description = """
Subtract a BCD value, which is either a V memory location or a 4-digit
constant from the lower 16 bits in the accumulator. The result resides in
the accumulator.
"""     

class subtract_double(Instruction):
      code = "SUBD"
      description = """
Subtracts a BCD-value, which is either two consecutive V memory
locations or an 8-bit constant, from a value in the accumulator. The result 
resides in the accumulator.
"""     

class subtract_real_number(Instruction):
      code = "SUBR"
      description = """
DL06 Only. Subtracts a real number, which is either two consecutive
V-memory locations or an 8-digit constant, from the real number in the
accumulator. The result resides in the accumulator.
"""     

class multiply(Instruction):
      code = "MUL"
      description = """
Multiplies a BCD value, which is either a V-memory location or a 4-digit
constant, by the value in the lower 16 bits of the accumulator. The result
resides in the accumulator.
"""     

class multiply_double(Instruction):
      code = "MULD"
      description = """
Multiples a BCD value contained in two consecutive V-memory locations
by the value in the accumulator. The result resides in the accumulator.
"""     

class multiply_real_number(Instruction):
      code = "MULR"
      description = """
DL06 Only. Multiplies a real number, which is either two consecutive
V-memory locations or a real number constant, by the real number in 
the accumulator. The result resides in the accumulator.
"""     

class divide(Instruction):
      code = "DIV"
      description = """
Divides a BCD value in the accumulator by a BCD value which is either
a V-memory location or a 4-digit constant. The result resides in the accumulator.
"""     

class divide_double(Instruction):
      code = "DIVD"
      description = """
Divides a BCD value in the accumulator by a BCD value which is
either two consecutive V-memory locations or a real number 
constant. The result resides in the accumulator.
"""     

class divide_real_number(Instruction):
      code = "DIVR"
      description = """
DL06 Only. Divides a real number in the accumulator by a real number
which is either two consecutive V-memory locations or a real number
constant. The result resides in the accumulator.
"""     

class increment(Instruction):
      code = "INC"
      description = """
Increments a BCD value in a specified V-memory location by 1 each
time the instruction is executed.
"""     

class decrement(Instruction):
      code = "DEC"
      description = """
Decrements a BCD value in a specified V-memory location by 1 each
time the instruction is executed.
"""     

class add_binary(Instruction):
      code = "ADDB"
      description = """
Adds the binary value in the lower 16 bits of the accumulator to a value
which is either a V-memory location or a 16-bit constant. The result
resides in the accumulator.
"""     

class add_binary_double(Instruction):
      code = "ADDBD"
      description = """
DL06 only. Adds teh binary value in the accumulator to a value which
is either two consecutive V-memory locations or a 32-bit constant. The
result resides in the accumulator.
"""     

class subtract_binary(Instruction):
      code = "SUBB"
      description = """
Subtract a 16-bit binary value, which is either a V-memory location or a
16-bit constant, from the lower 16 bits in the accumulator. The result
resides in the accumulator.
"""     

class subtract_binary_double(Instruction):
      code = "SUBBD"
      description = """
DL06 Only. subtracts a 32-bit binary value, which is either two consecutive
V-memory locations or a 32-bit constant, from the value in the accumulator.
The result resides in the accumulator.
"""     

class multiply_binary(Instruction):
      code = "MULB"
      description = """
Multiplies a 16-bit binary value, which is either a V-memory location or
a 16-bit constant, by the lower 16 bites in teh accumulator. The result
resides in the accumulator.
"""     

class divide_binary(Instruction):
      code = "DIVB"
      description = """
Divides the binary value in the lower 16 bits in the accumulator by a
value which is either a V-memory location or a 16-bit constant. The 
result resides in the accumulator.
"""     

class increment_binary(Instruction):
      code = "INCB"
      description = """
Increments a binary value in a specified V-memory location by 1 each
time the instruction is executed.
"""     

class decrement_binary(Instruction):
      code = "DECB"
      description = """
Decrements a binary value in a specified V-memory location 1 each
time the instruction is executed.
"""     

class add_formatted(Instruction):
      code = "ADDF"
      description = """
DL06 Only. Subtracts a BCD value which is a range of discrete bits
(1-32) from the BCD value in the accumulator. The result resides in the
accumulator
"""     
class subtract_formatted(Instruction):
      code = "SUBF"
      description = """
DL06 Only. Adds the BCD value which is a range of discrete bits
(1-32) from the BCD value in the accumulator. The result resides in the 
accumulator.
"""     

class multiply_formatted(Instruction):
      code = "MULF"
      description = """
DL06 Only. Multiples a BCD value in the lower 16-bits in the accumulator
by a BCD value which is range of discrete bits (1-16). The result
resides in the accumulator.
"""     

class divide_formatted(Instruction):
      code = "DIVF"
      description = """
DL06 Only. Divides the BCD value in the lower 16-bits in the accumlator
by the BCD value which is a range of discrete bits (1-16). The result
resides in teh accumulator.
"""     

class add_top_of_stack(Instruction):
      code = "ADDS"
      description = """
DL06 Only. Adds the BCD value in the accumulator with the BCD
value in the first level of the accumulator stack. The result resides in the
accumulator.
"""     

class subtract_top_of_stack(Instruction):
      code = "SUBS"
      description = """
DL06 Only. Subtracts the BCD value in the first level of the accumulator
stack from the BCD value in the accumulator. The result resides in the 
accumulator.
"""     

class multiply_top_of_stack(Instruction):
      code = "MULS"
      description = """
DL06 Only. Multiplies a 4-digit BCD value in the first level of the
accumulator stack by a 4-digit BCD value in the accumulator. The result
resides in the accumulator.
"""     

class divide_by_top_of_stack(Instruction):
      code = "DIVS"
      description = """
DL06 Only. Divides the 8-digit BCD value in the accumulator by the
4-digit BCD value in the first level of the accumulator by the 4-digit
BCD value in the first level of the accumulator stack. The result resides
in the accumulator.
"""     

class add_binary_top_of_stack(Instruction):
      code = "ADDBS"
      description = """
DL06 Only. Adds the binary value in the accumulator with the binary
value in the first accumulator stack location. The result resides in
the accumulator.
"""     

class subtract_binary_top_of_stack(Instruction):
      code = "SUBBS"
      description = """
DL06 Only. Subtracts the binary value in the first level of the
accumulator stack from the binary value in the accumulator. The result
resides in the accumulator.
"""     

class multiply_binary_top_of_stack(Instruction):
      code = "MULBS"
      description = """
DL06 Only. Multiplies the 16-binary value in the first level of the
accumulator stack by the 16-bit binary value in the accumulator. The
result resides in the accumulator.
"""     

class divide_binary_top_of_stack(Instruction):
      code = "DIVBS"
      description = """
DL06 Only. Dividesa value in the accumulator by the binary value in
the top location of the stack. The accumulator contains the result.
"""     

