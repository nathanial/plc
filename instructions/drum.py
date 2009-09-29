from plc.instructions.instruction import Instruction
class tuned_drum_with_discrete_outputs(Instruction):
      code = "DRUM"
      description = """
Time driven drum with up to 16 steps and 16 discrete outputs points.
Output status is written to the appropriate output during each step.
Specify a time base per count (in milliseconds.) Each step can hava a
different number of counts to trigger the transition to the next step. Also
define preset step as destination when reset occurs.
"""     


class time_and_event_drum_with_discrete_outputs(Instruction):
      code = "EDRUM"
      description = """
Time and or event driven drum with up to 16 steps and 16 discrete
output points. Output status is written to the appropriate output
during each step. Specify a time base per count (in milliseconds.)
Each step can have a different number of counts and an event to trigger
the counting. Once the time has expired, a transition to the next step
occurs. Also define preset step as destination when reset occurs.
"""     


class time_and_event_drum_with_discreteoutputs_and_output_mask(Instruction):
      code = "MDRMD"
      description = """
DL06 Only. Time and/or event driven drum with up to 16 steps and 16 
discrete output points. Actual output statis is the result of a bit-by-bit
AND between the utput mask and a bit mask in the step. Specify a time
base per count (in milliseconds.) Each step can have a different number
of counts and an event to trigger the counting. once the time has
expried, a transition to the next step occurs. Also define present step as
destnation when reset occurs.
"""     


class time_and_event_drum_with_word_output_and_output_mask(Instruction):
      code = "MDRMW"
      description = """
Dl06 Only. Time and or event driven drum with up to 16 steps and a
single V-memory output location. Actual output word is the result of a
bit-by-bit AND between the word mask and the bit mask in the step.
Specify a time base per count (in milliseconds.) Each step can have a
different number of counts and an event to trigger the counting. Once
the time has expired, a transition to the next step occurs. Also define
preset step as destination when reset occurs.
"""     
