class Instruction(object):
    pass

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

#immediate instructions

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

class timer(Instruction):
      code = "TMR"
      description = """
Single input incrementing timer with 0.1 second resolution (0-999.9 seconds)
"""     

class fast_timer(Instruction):
      code = "TMRF"
      description = """
Single input incrementing timer with 0.01 second resolution (0-99.99 seconds)
"""     

class accumulating_timer(Instruction):
      code = "TMRA"
      description = """
Two input incrementing timer with 0.1 second resolution
(0-9,999,999.99 sec.) Time and enable/reset inputs control the timer
"""     

class accumulating_fast_timer(Instruction):
      code = "TMRAF"
      description = """
Two input incrementing timer with 0.01 second resolution
(0-99,999.99 sec) Time and enable/reset inputs control the timer.
"""     

class counter(Instruction):
      code = "CNT"
      description = """
Two input incrementing counter (0-9999). Count and reset inputs 
control the counter.
"""     

class stage_counter(Instruction):
      code = "SGCNT"
      description = """
Single input incrementing counter (0-9999) RST instruction must be
used to reset count.
"""     

class up_down_counter(Instruction):
      code = "UDC"
      description = """
Three input counter (0-99,999,999). Up, down and reset inputs control
the counter.
"""     

class shift_register(Instruction):
      code = "SR"
      description = """
Shifts data through a range of control relays with each clock pulse. The
data clock and reset inputs control the shift register.
"""     

class load(Instruction):
      code = "LD"
      description = """
Loads a 16-bit word into the lower 16 bits of teh acummulator/stack.
"""     

class load_double(Instruction):
      code = "LDD"
      description = """
Loads a 32-bit word into the accumulator/stack.
"""     

class load_real_number(Instruction):
      code = "LDR"
      description = """
DL06 Only. Loads a real number contained in two consecutive
V-memory locations or a real constant into the accumulator.
"""     

class load_formatted(Instruction):
      code = "LDF"
      description = """
Loads the accumuator with a specified number of consecutive discrete
memory bits.
"""     

class load_address(Instruction):
      code = "LDA"
      description = """
Loads the accumulator with the HEX value for an octal constant
(address)
"""     

class load_accumulator_indexed(Instruction):
      code = "LDX"
      description = """
Specifies a source address (V memory) which will be offset by the 
value in the first stack location.
"""     

class out(Instruction):
      code = "OUT"
      description = """
Copies the value in the lower 16 bits of the accumulator to a specified
V memory location.
"""     

class out_double(Instruction):
      code = "OUTD"
      description = """
Copies the value in the accumlator to two consecutive V memory
locations.
"""     

class out_formatted(Instruction):
      code = "OUTF"
      description = """
Outputs a specified number of bits (1-32) from the accumulator to the 
specified discrete memory locations.
"""     

class pop(Instruction):
      code = "POP"
      description = """
Moves the value from the first level of the accumulator stack to the 
accumulator and shifts each value in the stack up one level.
"""     

class out_least(Instruction):
      code = "OUTL"
      description = """
DL06 only. Copies the value in the upper 8-bits of the lower accumulator
word (1st 16bits) to the lower 8 bits of a specified V-memory 
location.
"""     

class out_most(Instruction):
      code = "OUTM"
      description = """
DL06 Only. Copies the value in the upper 8-bits of the lowe accumulator 
word (1st 16bits) to the upper 8 bits of a specified V-memory
location.
"""     

class output_indexed(Instruction):
      code = "OUTX"
      description = """
DL06 only. Copies a 16-bit value from the first level of the accumulator
stack to a source address offset by the value in the accumulator.
"""     

