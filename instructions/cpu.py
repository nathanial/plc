from plc.instructions.instruction import Instruction
class no_operation(Instruction):
      code = "NOP"
      description = """
Inserts a no operation coil at specified program address.
"""     

class end(Instruction):
      code = "END"
      description = """
Marks the termination point for the normal program scan. And End
instruction is required at the end of the main program body.
"""     

class stop(Instruction):
      code = "STOP"
      description = """
Changes the operational mode of the CPU from Run to Program (Stop)
"""     

class reset_watchdog_timer(Instruction):
      code = "RSTWT"
      description = """
Resets the CPU watchdog timer.
"""     

