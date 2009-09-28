class read_from_intelligent_module(Instruction):
      code = "RD"
      description = """
Reads a block of memory from an intelligent I/O module into the CPU's 
V-memory.
"""     

class write_to_intelligent_module(Instruction):
      code = "WT"
      description = """
Writes a block of data to an intelligent I/O module from a block of
CPU's V-memory.
"""     

