class store(Instruction):
      code = "STR"
      description = """
Begins a new run or an additional branch in a rung with a normally
open contact.
"""          
      
class store_not(Instruction):
      code = "STRN"
      description = """
Begins a new run or an additional branch in a run with a normaly
closed contact.
"""           

class store_bit_of_word(Instruction):
      code = "STRB"
      description = """
DL06 Only. Begins a new run or an additional branch in a run with
a normally open V-memory bit-of-word contact.
"""     

class store_not_bit_of_word(Instruction):
      code = "STRNB"
      description = """
DL06 Only. Begins a new wrung or an additional branch in a run
with a normally closed V-memory bit-of-word contact.
"""     

class _or(Instruction):
      code = "OR"
      description = """
Logically ors a normally open contact in parallel with another contact
in a run.
"""     

class or_not(Instruction):
      code = "ORN"
      description = """
Logically ors a normally closed contact in parallel with another contact
in a run.
"""     

class or_bit_of_word(Instruction):
      code = "ORB"
      description = """
DL06 Only. ors a normally closed open V-memory bit-of-word contact in 
parallel with another contact in a run.
"""     

class or_not_bit_of_word(Instruction):
      code = "ORNB"
      description = """
DL06 Only. ors a normally closed V-memory bit-of-word contact in
parallel with another contact in a run.
"""     

class _and(Instruction):
      code = "AND"
      description = """
Logically ands a normally open contact in series with another contact
in a rung.
"""     

class and_not(Instruction):
      code = "ANDN"
      description = """
Logically ands a normally closed contact in series with another contact
in a rung.
"""     

class and_bit_of_word(Instruction):
      code = "ANDB"
      description = """
DL06 Only. ands a normally closed contact in series with another contact
in a rung.
"""     

class and_not_bit_of_word(Instruction):
      code = "ANDNB"
      description = """
DL06 Only. ands a normally closed contact in series with another contact
in a rung.
"""     

class and_store(Instruction):
      code = "ANDSTR"
      description = """
Logically ands two branches of a rung in series.
"""     

class or_store(Instruction):
      code = "ORSTR"
      description = """
Logically ors two branches of a rung in parallel.
"""     

class out(Instruction):
      code = "OUT"
      description = """
Reflects the status of the rung (on/off) and outputs the discrete (on/off)
state to the specified image register point or memory location.
"""     

class or_out(Instruction):
      code = "OROUT"
      description = """
Reflects the status of the rung and outputs the discrete (ON/OFF) state
to the image register. Multiple OR OUT instructions referencing the
smae discrete point can be used in the program.
"""     

class out_bit_of_word(Instruction):
      code = "OUTB"
      description = """
DL06 Only. Reflects status of the rung (on/off) and outputs the discrete
(on/off) state to teh specified bit in the referenced V-memory location.
"""     

class _not(Instruction):
      code = "NOT"
      description = """
Inverts the status of teh run at the point of the instruction.
"""     

class positive_differential(Instruction):
      code = "PD"
      description = """
One-shot output coil. When the input logic produces an off to on
transition, the output will energize for one CPU scan.
"""     

class store_positive_differential(Instruction):
      code = "STRPD"
      description = """
Leading edge triggered one-shot contact. When the corresponding
memory location transitions from low to high, the contact comes on
for one CPU scan.
"""     

class store_negative_differential(Instruction):
      code = "STRND"
      description = """
Trailing edge triggered one-shot contact. When the corresponding
memory location transitions from low to high, the contact comes on
for one CPU scan.
"""     

class or_positive_differential(Instruction):
      code = "ORPD"
      description = """
Logically ors a leading edge triggered one-shot contact in parallel with
another contact in a run.
"""     

class or_negative_differential(Instruction):
      code = "ORPD"
      description = """
Logically ors a trailing edge triggered one-shot contact in parallel wiht
another contact in a rung.
"""     

class and_positive_differential(Instruction):
      code = "ANDPD"
      description = """
Logically ands a leading edge triggered one-shot contact in series with
another contact in a rung.
"""     

class and_negative_differential(Instruction):
      code = "ANDND"
      description = """
Logically ands a trailing edge triggered one-shot contact in series with
another contact in a rung.
"""     

class _set(Instruction):
      code = "SET"
      description = """
An output that turns on a point or a range of points. The reset instruction
is used to turn the point(s) OFF that were set ON with teh set instruction.
"""     

class Reset(Instruction):
      code = "RST"
      description = """
An output that resets a point or a range of points.
"""     

class set_bit_of_word(Instruction):
      code = "SETB"
      description = """
DL06 Only. Sets or turns on a bit in a V-memory location.
"""     

class reset_bit_or_word(Instruction):
      code = "RSTB"
      description = """
DL06 Only. Resets or turns off a bit in a V-memory location
"""     

class pause_outputs(Instruction):
      code = "PAUSE"
      description = """
Disable the update for a range of specified 
"""     
