from plc.instructions.instruction import Instruction
class _and(Instruction):
      code = "AND"
      description = """
Logically ands the lower 16 bits in the accumulator with a V-memory
location.
"""     

class and_double(Instruction):
      code = "ANDD"
      description = """
Logically ands teh value in the accumulator with an 8-digit constant or
a value in two consecutive V-memory locations.
"""     

class and_formatted(Instruction):
      code = "ANDF"
      description = """
DL06 Only. Logically ands teh value in the accumulator and a
specified range of discrete memory bits (1-32).
"""     

class and_with_stack(Instruction):
      code = "ANDS"
      description = """
DL06 Only. Logically ands the value in the accumulator with the first
value in the accumulator stack.
"""     

class _or(Instruction):
      code = "OR"
      description = """
Logically ors the lower 16 bits in the accumulator with the first
value in the accumulator stack.
"""     

class or_double(Instruction):
      code = "ORD"
      description = """
Logically ors teh value in the accumulator with an 8-digit constant or a 
value in two consecutive V-memory locations.
"""     

class or_formatted(Instruction):
      code = "ORF"
      description = """
DL06 Only. Logically ors teh value in teh accumulator with a range of
discrete bits (1-32).
"""     

class or_with_stack(Instruction):
      code = "ORS"
      description = """
DL06 Only. Logically ors the value in the accumulator with teh first
value in the accumulator stack.
"""     

class exclusive_or(Instruction):
      code = "XOR"
      description = """
Performs an exclusive or of the value in the lower 16 bits of the 
accumulator and a V-memory location.
"""     

class exclusive_or_double(Instruction):
      code = "XORD"
      description = """
Performs an exclusive or of the value in the accumulator and an
8-digit constant or a value in two consecutive V-memory locations.
"""     

class exclusive_or_formatted(Instruction):
      code = "XORF"
      description = """
DL06 Only. Performs an exclusive or of the value in the accumulator
and a range of discrete bits (1-32).
"""     

class exclusive_or_with_stack(Instruction):
      code = "XORS"
      description = """
DL06 Only. Performs an exclusive or of the value in the accumulator
and the first accumulator stack location.
"""     

class compare(Instruction):
      code = "CMP"
      description = """
Compares teh value in the lower 16 bits of the accumulator with a 
V-memory location.
"""     

class compare_double(Instruction):
      code = "CMPD"
      description = """
Compares teh value in the accumulator with two consecutive 
V-memory locations or an 8-digit constant.
"""     

class compare_formatted(Instruction):
      code = "CMPF"
      description = """
DL06 only. Compares the value in the accumulator with a specified
number of discrete locations (1-32).
"""     

class compare_with_stack(Instruction):
      code = "CMPS"
      description = """
DL06 only. Compares the value in the accumulator with the first 
accumulator stack location.
"""     

class compare_real_number(Instruction):
      code = "CMPR"
      description = """
Dl06 Only. Compares the real number in the accumulator with two
consecutive V-memory locations or a real number constant.
"""     

      
