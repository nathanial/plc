from plc.instructions.instruction import Instruction
class move(Instruction):
      code = "MOV"
      description = """
Moves the values from one V-memory table to another V memory table.
"""     

class move_memory_cartridge_load_label(Instruction):
      code = "MOVMC/LDLBL"
      description = """
DL06 Only. Copies data between V-memory and program ladder 
memory.
"""     

class set_bit(Instruction):
      code = "SETBIT"
      description = """
DL06 only. Sets a single bit (to a 0) in a V-memory location.
"""     

class reset_bit(Instruction):
      code = "RSTBIT"
      description = """
DL06 Only. Resets a single bit (to a 0) in a V-memory location.
"""     

