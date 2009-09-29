from plc.instructions.instruction import Instruction
class interrupt_routine(Instruction):
      code = "INT"
      description = """
When a hardware or software interrupt occurs, the interrupt routine
will be executed. The INT instruction is beginning of the interrupt
routine. The interrupt routine is terminated with an IRT of the interrupt
routine. The interrupt routine is terminated with an IRT instruction
(unconditional interrupt return.) When an interrupt is reached the
execution of the program contineus from the instruction where the
program execution was prior to the interrupt.
"""     

class interrupt_return(Instruction):
      code = "IRT"
      description = """
interrupt return
"""     

class interrupt_return_conditional(Instruction):
      code = "IRTC"
      description = """
interrupt return conditional
"""     

class enable_interrupt(Instruction):
      code = "ENI"
      description = """
Enables hardware and software interrupts to be acknowledged.
"""     


