class sum(Instruction):
      code = "SUM"
      description = """
Counts the number of bits set to '1' in the accumulator. The HEX result
resides in the accumulator.
"""     

class shift_left(Instruction):
      code = "SHFL"
      description = """
Shifts the bits in the accumulator a specified number of places to the left
"""     

class shift_right(Instruction):
      code = "SHFR"
      description = """
Shifts the bits in the accumulator a specified number of places to the right
"""     

class rotate_left(Instruction):
      code = "ROTL"
      description = """
Rotates teh bits in the accumulator a specified nubmer of places to the left
"""     

class rotate_right(Instruction):
      code = "ROTR"
      description = """
Rotates teh bits in the accumulator a specified nubmer of places to the right
"""     

class encode(Instruction):
      code = "ENCO"
      description = """
Encodes the bit position set to 1 in the accumulator, and returns the
appropriate binary representation in the accumulator.
"""     

class decodes(Instruction):
      code = "DECO"
      description = """
Decodes a 5 bit binary value(0-31) in the accumulator by setting the
appropriate bit position to a 1.
"""     

