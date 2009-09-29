from plc.instructions.instruction import Instruction
class date(Instruction):
      code = "DATE"
      description = """
Use to set the date in the CPU
"""     

class time(Instruction):
      code = "TIME"
      description = """
Use to set the time in the CPU.
"""     


