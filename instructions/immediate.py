
class store_immediate(Instruction):
      code = "STRI"
      description = """
Begins a rung/branch of logic with a normally open contact. The contact
will be updated with teh current inptu field status when processed
in the program scan.
"""     

class store_not_immediate(Instruction):
      code = "STRNI"
      description = """
Begins a rung/branch of logic with a normally closed contact. The contact
will be updated with teh current inptu field status when processed
in the program scan.
"""     

class or_immediate(Instruction):
      code = "ORI"
      description = """
Connects a normaly open contact in parallel with another contact. The
contact will be updated with the current input field status when
processed in the program scan.
"""     

class or_not_immediate(Instruction):
      code = "ORNI"
      description = """
Connects a normally closed contact in parallel with another contact.
The contact will be updated with teh current input field status when
processed in the program scan.
"""     

class and_immediate(Instruction):
      code = "ANDI"
      description = """
Connects a normally open contact in series with another contact. The
contact will be updated with the current input field status whne
processed in the program scan.
"""     

class and_not_immediate(Instruction):
      code = "ANDNI"
      description = """
Connects a normally closed contact in series with another contact. The
contact will be updated with the current input field status when
processed in the program scan.
"""     

class out_immediate(Instruction):
      code = "OUTI"
      description = """
Reflects the status of the rung. The output field device status is updated
when the instruction is processed in the program scan.
"""     

class or_out_immediate(Instruction):
      code = "OROUTI"
      description = """
Reflects teh status of the rung and outputs teh discrete (ON/OFF) state
to the image register. Multiple OR OUT instructions referencing the 
same discrete point can be used in the program. The output field 
device status is updated when the instruction is processed in the
program scan.
"""     

class set_immediate(Instruction):
      code = "SETI"
      description = """
An output that turns on a point or a range of points. The reset instruction
is used to turn the point(s) off that were set. The output field device
status is updated when the instruction is processed in the program
scan.
"""     

class reset_immediate(Instruction):
      code = "RSTI"
      description = """
an output that resets a point or a range of points. The output field
device status is updated when the isntruction is processed in the 
program scan.
"""     

class load_immediate(Instruction):
      code = "LDI"
      description = """
DL06 Only. Loads the accumulator with the contents of a specified
16-bit V-memory location. The statusfor each bit of the specified 
V-memory location is loaded into the accumulator. Typically used for
input module V-memory addresses. Allows you to specify the V-location
instead of the X-location and the number of points as with the LDIF.
"""     

class load_immediate_formatted(Instruction):
      code = "LDIF"
      description = """
DL06 Only. Loads the accumulator with a specified number of
consecutive inputs. The field device status for the specified inputs
points is loaded into the accumulator when the instruction is executed.
"""     

class out_immediate_formatted(Instruction):
      code = "OUTIF"
      description = """
DL06 Only. Outputs the contents of the accumulator to a specified
number of consecutive outputs. The output field devices are updated
when the instruction is processed by the program scan.
"""     
