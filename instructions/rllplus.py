from plc.instructions.instruction import Instruction
class initial_stage(Instruction):
      code = "ISG"
      description = """
The initial stage instruciton is used for a starting point for user
application program. The ISG instruction will be active on power up
and PROGRAM to RUN transitions.
"""     

class stage(Instruction):
      code = "SG"
      description = """
Stage instructions are used to create structured programs. They are
program segments which can be activated or deactivated with control 
logic.
"""     

class jump(Instruction):
      code = "JMP"
      description = """
Normally open coil that deactivates the active stage and activates a
specified stage when there is power flow to the coil.
"""     

class not_jump(Instruction):
      code = "NJMP"
      description = """
Normally closed coil that deactivates the active stage and activates a
specified stage when there is power flow to the coil.
"""     

class converge_stages(Instruction):
      code = "CV"
      description = """
Converge stages are a group of stages that when all stages are active
the associated converge jump(s). (CVJMP) will active another stage(s).
Once scan after teh CVJMP is executed, the converge stages will be 
deactivated.
"""     

class converge_jump(Instruction):
      code = "CVJMP"
      description = """
Normally open coil that deactivates the active CV stages and activates
a specified stage when there is power flow to the coil.
"""     

class block_call(Instruction):
      code = "BCALL"
      description = """

"""     
class block(Instruction):
      code = "BLK"
      description = """

"""     
class bend(Instruction):
      code = "BEND"
      description = """

"""     
