from plc.instructions.instruction import Instruction
class fault_label(Instruction):
      code = "FAULT"
      description = """
Displays a V-memory value or a data label constant to the hand-held
programmer or personal computer using DirectSOFT.
"""     

class data_label(Instruction):
      code = "DLBL"
      description = """

"""     

class numerical_constant(Instruction):
      code = "NCON"
      description = """
Stores constants in numerical form for use with other 
instructions.
"""     

class ascii_constant(Instruction):
      code = "ACON"
      description = """
Stores constants in ascii form for use with other 
instructions.
"""     


class print_message(Instruction):
      code = "PRINT"
      description = """
Prints teh embedded text or text/data variable message to the specified
communications port. Maximumum message length is 255 words.
appropriate bit position to 1 in the accumulator.
"""     

