class load(Instruction):
      code = "LD"
      description = """
Loads a 16-bit word into the lower 16 bits of teh acummulator/stack.
"""     

class load_double(Instruction):
      code = "LDD"
      description = """
Loads a 32-bit word into the accumulator/stack.
"""     

class load_real_number(Instruction):
      code = "LDR"
      description = """
DL06 Only. Loads a real number contained in two consecutive
V-memory locations or a real constant into the accumulator.
"""     

class load_formatted(Instruction):
      code = "LDF"
      description = """
Loads the accumuator with a specified number of consecutive discrete
memory bits.
"""     

class load_address(Instruction):
      code = "LDA"
      description = """
Loads the accumulator with the HEX value for an octal constant
(address)
"""     

class load_accumulator_indexed(Instruction):
      code = "LDX"
      description = """
Specifies a source address (V memory) which will be offset by the 
value in the first stack location.
"""     

class out(Instruction):
      code = "OUT"
      description = """
Copies the value in the lower 16 bits of the accumulator to a specified
V memory location.
"""     

class out_double(Instruction):
      code = "OUTD"
      description = """
Copies the value in the accumlator to two consecutive V memory
locations.
"""     

class out_formatted(Instruction):
      code = "OUTF"
      description = """
Outputs a specified number of bits (1-32) from the accumulator to the 
specified discrete memory locations.
"""     

class pop(Instruction):
      code = "POP"
      description = """
Moves the value from the first level of the accumulator stack to the 
accumulator and shifts each value in the stack up one level.
"""     

class out_least(Instruction):
      code = "OUTL"
      description = """
DL06 only. Copies the value in the upper 8-bits of the lower accumulator
word (1st 16bits) to the lower 8 bits of a specified V-memory 
location.
"""     

class out_most(Instruction):
      code = "OUTM"
      description = """
DL06 Only. Copies the value in the upper 8-bits of the lowe accumulator 
word (1st 16bits) to the upper 8 bits of a specified V-memory
location.
"""     

class output_indexed(Instruction):
      code = "OUTX"
      description = """
DL06 only. Copies a 16-bit value from the first level of the accumulator
stack to a source address offset by the value in the accumulator.
"""     

