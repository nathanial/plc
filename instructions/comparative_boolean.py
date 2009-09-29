from plc.instructions.instruction import Instruction

class store_if_equal(Instruction):
      code = "STRE"
      description = """
Begins a new run or additional branch in a run with a normally
open comparative contact. The contact will be on when
A = B.
"""     

class store_if_not_equal(Instruction):
      code = "STRNE"
      description = """
Begins a new rung or additional branch in a rung with a normally
closed comparative contact. The contact will be on when A is not
equal to B.
"""     

class or_if_equal(Instruction):
      code = "ORE"
      description = """
Connects a normally open comparative contact in parallel with another
contact. The ocntact will be on when A = B.
"""     

class or_if_not_equal(Instruction):
      code = "ORNE"
      description = """
Connects a normally closed comparative contact in parallel with
another contact. The contact will be on when A is not equal to B.
"""     

class and_if_equal(Instruction):
      code = "ANDE"
      description = """
Connects a normally open comparative contact in series with another
contact. The contact will be on when A = B.
"""     

class and_if_not_equal(Instruction):
      code = "ANDNE"
      description = """
Connects a normally closed comparative contact in series with another
contact. the contact will be on when A is not equal B.
"""     
