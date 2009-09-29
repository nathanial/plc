from plc.instructions.instruction import Instruction
class label(Instruction):
      code = "LBL"
      description = """
Declares label
"""     

class goto_label(Instruction):
      code = "GOTO"
      description = """
Skips all instruction between teh Goto and corresponding LBL
instruction. DL06 units only. Not available in Dl05.
"""     

class goto_subroutine(Instruction):
      code = "GTS/SBR/RT/RTC"
      description = """
When a GTS instruction is executed the program jumps to the SBR
(Subroutine.) The subroutine is terminated with a RT instruction
(unconditional return.) When a return is exectued, the prgoram 
continues from the instruction after the calling GTS instruction. The RTC
(Subroutine return conditional) instruction is used with an input contact
to implement a conditioanl return from the subroutine.
"""     

class subroutine(Instruction):
      code = "SBR"
      description = """
subroutine
"""     

class _return(Instruction):
      code = "RT"
      description = """
return
"""   

class return_conditional(Instruction):
      code = "RTC"
      description = """
subroutine return conditional
"""       

class master_line_set(Instruction):
    code = "MLS"
    description = """
Allows the program to control sections of ladder logic by forming a new
power rail. The MLS marks the beginning of a power rail and the MLR 
marks the end of the power rail control.
"""     

class master_line_reset(Instruction):
      code = "MLR"
      description = """
see MasterLineSet
"""     

