
instructions = {}

class InstructionType(type):
    def __new__(cls,name,bases,dct):
        if dct.get('description'):
            dct['description'] = dct.get('description').strip()
        class_obj = type.__new__(cls,name,bases,dct)
        if dct.get('code'):
            instructions[dct['code']] = class_obj
        return class_obj

class Instruction(object):
    __metaclass__ = InstructionType
    @staticmethod
    def lookup(name):
        instruction = instructions.get(name)
        if instruction:
            return instruction()
        else:
            return None
        
    def __str__(self):
        return self.__class__.code
    
    def __repr__(self):
        return self.__str__()


class math_add(Instruction):
      code = "ADD"
      description = """
Adds a BCD value in the lower 16 bits in teh accumulator with a V-memory
location. The result resides in the accumulator.
"""     

class math_add_double(Instruction):
      code = "ADDD"
      description = """
Adds a BCD value in the accumulator with two consecutive V-memory
locations or an 8-digit constant. The result resides in the accumulator.
"""     

class math_add_real_number(Instruction):
      code = "ADDR"
      description = """
DL06 Only. Adds a real number in the accumulator with a real number
constant or a real number contains in two consecutive V-memory
locations. The result resides in the accumulator.
"""     

class math_subtract(Instruction):
      code = "SUB"
      description = """
Subtract a BCD value, which is either a V memory location or a 4-digit
constant from the lower 16 bits in the accumulator. The result resides in
the accumulator.
"""     

class math_subtract_double(Instruction):
      code = "SUBD"
      description = """
Subtracts a BCD-value, which is either two consecutive V memory
locations or an 8-bit constant, from a value in the accumulator. The result 
resides in the accumulator.
"""     

class math_subtract_real_number(Instruction):
      code = "SUBR"
      description = """
DL06 Only. Subtracts a real number, which is either two consecutive
V-memory locations or an 8-digit constant, from the real number in the
accumulator. The result resides in the accumulator.
"""     

class math_multiply(Instruction):
      code = "MUL"
      description = """
Multiplies a BCD value, which is either a V-memory location or a 4-digit
constant, by the value in the lower 16 bits of the accumulator. The result
resides in the accumulator.
"""     

class math_multiply_double(Instruction):
      code = "MULD"
      description = """
Multiples a BCD value contained in two consecutive V-memory locations
by the value in the accumulator. The result resides in the accumulator.
"""     

class math_multiply_real_number(Instruction):
      code = "MULR"
      description = """
DL06 Only. Multiplies a real number, which is either two consecutive
V-memory locations or a real number constant, by the real number in 
the accumulator. The result resides in the accumulator.
"""     

class math_divide(Instruction):
      code = "DIV"
      description = """
Divides a BCD value in the accumulator by a BCD value which is either
a V-memory location or a 4-digit constant. The result resides in the accumulator.
"""     

class math_divide_double(Instruction):
      code = "DIVD"
      description = """
Divides a BCD value in the accumulator by a BCD value which is
either two consecutive V-memory locations or a real number 
constant. The result resides in the accumulator.
"""     

class math_divide_real_number(Instruction):
      code = "DIVR"
      description = """
DL06 Only. Divides a real number in the accumulator by a real number
which is either two consecutive V-memory locations or a real number
constant. The result resides in the accumulator.
"""     

class math_increment(Instruction):
      code = "INC"
      description = """
Increments a BCD value in a specified V-memory location by 1 each
time the instruction is executed.
"""     

class math_decrement(Instruction):
      code = "DEC"
      description = """
Decrements a BCD value in a specified V-memory location by 1 each
time the instruction is executed.
"""     

class math_add_binary(Instruction):
      code = "ADDB"
      description = """
Adds the binary value in the lower 16 bits of the accumulator to a value
which is either a V-memory location or a 16-bit constant. The result
resides in the accumulator.
"""     

class math_add_binary_double(Instruction):
      code = "ADDBD"
      description = """
DL06 only. Adds teh binary value in the accumulator to a value which
is either two consecutive V-memory locations or a 32-bit constant. The
result resides in the accumulator.
"""     

class math_subtract_binary(Instruction):
      code = "SUBB"
      description = """
Subtract a 16-bit binary value, which is either a V-memory location or a
16-bit constant, from the lower 16 bits in the accumulator. The result
resides in the accumulator.
"""     

class math_subtract_binary_double(Instruction):
      code = "SUBBD"
      description = """
DL06 Only. subtracts a 32-bit binary value, which is either two consecutive
V-memory locations or a 32-bit constant, from the value in the accumulator.
The result resides in the accumulator.
"""     

class math_multiply_binary(Instruction):
      code = "MULB"
      description = """
Multiplies a 16-bit binary value, which is either a V-memory location or
a 16-bit constant, by the lower 16 bites in teh accumulator. The result
resides in the accumulator.
"""     

class math_divide_binary(Instruction):
      code = "DIVB"
      description = """
Divides the binary value in the lower 16 bits in the accumulator by a
value which is either a V-memory location or a 16-bit constant. The 
result resides in the accumulator.
"""     

class math_increment_binary(Instruction):
      code = "INCB"
      description = """
Increments a binary value in a specified V-memory location by 1 each
time the instruction is executed.
"""     

class math_decrement_binary(Instruction):
      code = "DECB"
      description = """
Decrements a binary value in a specified V-memory location 1 each
time the instruction is executed.
"""     

class math_add_formatted(Instruction):
      code = "ADDF"
      description = """
DL06 Only. Subtracts a BCD value which is a range of discrete bits
(1-32) from the BCD value in the accumulator. The result resides in the
accumulator
"""     
class math_subtract_formatted(Instruction):
      code = "SUBF"
      description = """
DL06 Only. Adds the BCD value which is a range of discrete bits
(1-32) from the BCD value in the accumulator. The result resides in the 
accumulator.
"""     

class math_multiply_formatted(Instruction):
      code = "MULF"
      description = """
DL06 Only. Multiples a BCD value in the lower 16-bits in the accumulator
by a BCD value which is range of discrete bits (1-16). The result
resides in the accumulator.
"""     

class math_divide_formatted(Instruction):
      code = "DIVF"
      description = """
DL06 Only. Divides the BCD value in the lower 16-bits in the accumlator
by the BCD value which is a range of discrete bits (1-16). The result
resides in teh accumulator.
"""     

class math_add_top_of_stack(Instruction):
      code = "ADDS"
      description = """
DL06 Only. Adds the BCD value in the accumulator with the BCD
value in the first level of the accumulator stack. The result resides in the
accumulator.
"""     

class math_subtract_top_of_stack(Instruction):
      code = "SUBS"
      description = """
DL06 Only. Subtracts the BCD value in the first level of the accumulator
stack from the BCD value in the accumulator. The result resides in the 
accumulator.
"""     

class math_multiply_top_of_stack(Instruction):
      code = "MULS"
      description = """
DL06 Only. Multiplies a 4-digit BCD value in the first level of the
accumulator stack by a 4-digit BCD value in the accumulator. The result
resides in the accumulator.
"""     

class math_divide_by_top_of_stack(Instruction):
      code = "DIVS"
      description = """
DL06 Only. Divides the 8-digit BCD value in the accumulator by the
4-digit BCD value in the first level of the accumulator by the 4-digit
BCD value in the first level of the accumulator stack. The result resides
in the accumulator.
"""     

class math_add_binary_top_of_stack(Instruction):
      code = "ADDBS"
      description = """
DL06 Only. Adds the binary value in the accumulator with the binary
value in the first accumulator stack location. The result resides in
the accumulator.
"""     

class math_subtract_binary_top_of_stack(Instruction):
      code = "SUBBS"
      description = """
DL06 Only. Subtracts the binary value in the first level of the
accumulator stack from the binary value in the accumulator. The result
resides in the accumulator.
"""     

class math_multiply_binary_top_of_stack(Instruction):
      code = "MULBS"
      description = """
DL06 Only. Multiplies the 16-binary value in the first level of the
accumulator stack by the 16-bit binary value in the accumulator. The
result resides in the accumulator.
"""     

class math_divide_binary_top_of_stack(Instruction):
      code = "DIVBS"
      description = """
DL06 Only. Dividesa value in the accumulator by the binary value in
the top location of the stack. The accumulator contains the result.
"""     

class ascii_in(Instruction):
      code = "AIN"
      description = """
Configures port 2 to read raw ASCII input strings.
"""     

class ascii_find(Instruction):
      code = "AFIND"
      description = """
Searches ASCII string in V-memory to find a specific portion of the
string.
"""     

class ascii_in(Instruction):
      code = "AEX"
      description = """
Extracts a psecific portion from an ASCII string.
"""     

class ascii_compare_vmemory(Instruction):
      code = "CMPV"
      description = """
Compares two blocks of V-memory
"""     

class ascii_swap_bytes(Instruction):
      code = "SWAPB"
      description = """
Swaps V-memory bytes.
"""     

class ascii_print_to_vmemory(Instruction):
      code = "VPRINT"
      description = """
Used to send pre-coded ASCII strings to a pre-defined V-memory
address when enabled.
"""     

class ascii_print_from_vmemory(Instruction):
      code = "PRINTV"
      description = """
Used to write raw ASCII string out of port 2 when enabled.
"""     

class ext_table_fill(Instruction):
      code = "FILL"
      description = """
Fills a table of specified V-memory locations with a value which is either
a V-memory location or a 4-digit constant.
"""     

class ext_table_find(Instruction):
      code = "FIND"
      description = """
Finds a value in a V-memory table and returns the table position 
containing the value to the accumulator.
"""     

class ext_table_find_greater_than(Instruction):
      code = "FDGT"
      description = """
Finds a value in a V-memory table which is greater than the specified
search value. The table position containing the value is returned to the 
accumulator.
"""     

class ext_table_find_block(Instruction):
      code = "FINDB"
      description = """
Finds a block of data values in a V-memory table and returns the starting
address of the table containing the values to teh accumulator.
"""     

class ext_table_table_to_destination(Instruction):
      code = "TTD"
      description = """
Moves the value from the top of a V-memory table to a specified
V-memory location. The table pointer increments each scan.
"""     

class ext_table_remove_from_bottom(Instruction):
      code = "RFB"
      description = """
Moves the value from the bottom of a v-memory table to a specified
V-memory location. The table pointer increments each scan.
"""     

class ext_table_source_to_table(Instruction):
      code = "STT"
      description = """
Moves a value from specified V-memory location to a V-memory table.
The table pointer increments each scan.
"""     

class ext_table_remove_from_top(Instruction):
      code = "RFT"
      description = """
Pops a value from the top of a V-memory table and stores it in a
specified V-memory location. All other values in the V-memory table 
are shifted up each time a value is popped from table.
"""     

class ext_table_add_to_top_table(Instruction):
      code = "ATT"
      description = """
Pushes a value from a specified V-memory location onto top of a 
V-memory table. All other values in the V-memory table are shifted
down each time a value is pushed onto the table.
"""     

class ext_table_table_shift_left(Instruction):
      code = "TSHFL"
      description = """
Shifts specified number of bits to the left in a V-memory table
"""     

class ext_table_table_shift_right(Instruction):
      code = "TSHFR"
      description = """
Shifts specified number of bits to the right in a V-memory table.
"""     

class ext_table_and_move(Instruction):
      code = "ANDMOV"
      description = """
Copies data from a table to the specified location, ANDing each word
with the accumulator data as it is written.
"""     

class ext_table_or_move(Instruction):
      code = "ORMOV"
      description = """
Copies data from a table to the specified memory location, ORing each
word with the accumulator data as it is written.
"""     

class ext_table_exclusive_or_move(Instruction):
      code = "XORMOV"
      description = """
Copies data from a table to the specified memory location, XORing
each word with the accumulator data as it is written.
"""     

class ext_table_swap(Instruction):
      code = "SWAP"
      description = """
Exchanges teh data in two tables of equal length.
"""     

class immediate_store(Instruction):
      code = "STRI"
      description = """
Begins a rung/branch of logic with a normally open contact. The contact
will be updated with teh current inptu field status when processed
in the program scan.
"""     

class immediate_store_not(Instruction):
      code = "STRNI"
      description = """
Begins a rung/branch of logic with a normally closed contact. The contact
will be updated with teh current inptu field status when processed
in the program scan.
"""     

class immediate_or(Instruction):
      code = "ORI"
      description = """
Connects a normaly open contact in parallel with another contact. The
contact will be updated with the current input field status when
processed in the program scan.
"""     

class immediate_or_not(Instruction):
      code = "ORNI"
      description = """
Connects a normally closed contact in parallel with another contact.
The contact will be updated with teh current input field status when
processed in the program scan.
"""     

class immediate_and(Instruction):
      code = "ANDI"
      description = """
Connects a normally open contact in series with another contact. The
contact will be updated with the current input field status whne
processed in the program scan.
"""     

class immediate_and_not(Instruction):
      code = "ANDNI"
      description = """
Connects a normally closed contact in series with another contact. The
contact will be updated with the current input field status when
processed in the program scan.
"""     

class immediate_out(Instruction):
      code = "OUTI"
      description = """
Reflects the status of the rung. The output field device status is updated
when the instruction is processed in the program scan.
"""     

class immediate_or_out(Instruction):
      code = "OROUTI"
      description = """
Reflects teh status of the rung and outputs teh discrete (ON/OFF) state
to the image register. Multiple OR OUT instructions referencing the 
same discrete point can be used in the program. The output field 
device status is updated when the instruction is processed in the
program scan.
"""     

class immediate_set(Instruction):
      code = "SETI"
      description = """
An output that turns on a point or a range of points. The reset instruction
is used to turn the point(s) off that were set. The output field device
status is updated when the instruction is processed in the program
scan.
"""     

class immediate_reset(Instruction):
      code = "RSTI"
      description = """
an output that resets a point or a range of points. The output field
device status is updated when the isntruction is processed in the 
program scan.
"""     

class immediate_load(Instruction):
      code = "LDI"
      description = """
DL06 Only. Loads the accumulator with the contents of a specified
16-bit V-memory location. The statusfor each bit of the specified 
V-memory location is loaded into the accumulator. Typically used for
input module V-memory addresses. Allows you to specify the V-location
instead of the X-location and the number of points as with the LDIF.
"""     

class immediate_load_formatted(Instruction):
      code = "LDIF"
      description = """
DL06 Only. Loads the accumulator with a specified number of
consecutive inputs. The field device status for the specified inputs
points is loaded into the accumulator when the instruction is executed.
"""     

class immediate_out_formatted(Instruction):
      code = "OUTIF"
      description = """
DL06 Only. Outputs the contents of the accumulator to a specified
number of consecutive outputs. The output field devices are updated
when the instruction is processed by the program scan.
"""     

class number_conversion_binary(Instruction):
      code = "BIN"
      description = """
Converts teh BCD value in the accumulator to the equivalent binary
value. The result resides in the accumulator.
"""     

class number_conversion_binary_coded_decimal(Instruction):
      code = "BCD"
      description = """
Converts the binary value in the accumulator to the equivalent BCD
value. The result resides in the accumulator.
"""     

class number_conversion_invert(Instruction):
      code = "INV"
      description = """
Takes the one's complement of the 32-bit value in the accumulator. The
result resides in the accumulator.
"""     

class number_conversion_tens_complement(Instruction):
      code = "BCDCPL"
      description = """
DL06 Only. Takes the 10's complement (BCD) of the 8-digit accumulator.
"""     

class number_conversion_ascii_to_hex(Instruction):
      code = "ATH"
      description = """
Converts a table of ASCII values to a table of hexadecimal values.
"""     

class number_conversion_hex_to_ascii(Instruction):
      code = "HTA"
      description = """
Converts a table of hexadecimal values to a table of ASCII values.
"""     

class number_conversion_segment(Instruction):
      code = "SEG"
      description = """
DL06 Only. Converts four digit HEX value in accumulator to seven
segment display format.
"""     

class number_conversion_gray_code_to_bcd(Instruction):
      code = "GRAY"
      description = """
Converts a 16-bit GRAY code value in the accumulator to a 
corressponding BCD value. The result resides in the accumulator.
"""     

class number_conversion_shuffle_digits(Instruction):
      code = "SFLDGT"
      description = """
Shuffles a maximum of 8 digits, rearranging them in a specified order.
The result resides in the accumulator.
"""     

class number_conversion_radina_real(Instruction):
      code = "RADR"
      description = """
DL06 ONly. Converts teh real degree value in the accumulator to the
equivalent real number in radians. the result resides in the accumulator.
"""     

class number_conversion_degree_real(Instruction):
      code = "DEGR"
      description = """
DL06 Only. Converts the real radian value in the accumulator to the
equivalent real member of degrees. The result resides in the accumulator.
"""     

class number_conversion_binary_to_real_number(Instruction):
      code = "BTOR"
      description = """
DL06 Only. Converts the binary value in the accumulator into a real
number. The result resides in the accumulator.
"""     

class number_conversion_real_to_binary(Instruction):
      code = "RTOB"
      description = """
DL06 Only. Converts the real number in the accumulator into a binary
value. The result resides in the accumulator.
"""     

class modbus_read(Instruction):
      code = "MRX"
      description = """
Used CPU port 2 to read a block of data from MODBUS RTU devices on the network
"""     

class modbus_write(Instruction):
      code = "MWX"
      description = """
Writes a block of data from CPU port 2 to MODBUS RTU devices on
the network.
"""     

class network_read(Instruction):
      code = "RX"
      description = """
Reads a block of data from another CPU on the network.
"""     

class network_write(Instruction):
      code = "WX"
      description = """
Writes a block of data from the master device to a slave device on
the network.
"""     

class program_label(Instruction):
      code = "LBL"
      description = """
Declares label
"""     

class program_goto_label(Instruction):
      code = "GOTO"
      description = """
Skips all instruction between teh Goto and corresponding LBL
instruction. DL06 units only. Not available in Dl05.
"""     

class program_goto_subroutine(Instruction):
      code = "GTS/SBR/RT/RTC"
      description = """
When a GTS instruction is executed the program jumps to the SBR
(Subroutine.) The subroutine is terminated with a RT instruction
(unconditional return.) When a return is exectued, the prgoram 
continues from the instruction after the calling GTS instruction. The RTC
(Subroutine return conditional) instruction is used with an input contact
to implement a conditioanl return from the subroutine.
"""     

class program_subroutine(Instruction):
      code = "SBR"
      description = """
subroutine
"""     

class program__return(Instruction):
      code = "RT"
      description = """
return
"""   

class program_return_conditional(Instruction):
      code = "RTC"
      description = """
subroutine return conditional
"""       

class program_master_line_set(Instruction):
    code = "MLS"
    description = """
Allows the program to control sections of ladder logic by forming a new
power rail. The MLS marks the beginning of a power rail and the MLR 
marks the end of the power rail control.
"""     

class program_master_line_reset(Instruction):
      code = "MLR"
      description = """
see MasterLineSet
"""     

class logical_and(Instruction):
      code = "AND"
      description = """
Logically ands the lower 16 bits in the accumulator with a V-memory
location.
"""     

class logical_and_double(Instruction):
      code = "ANDD"
      description = """
Logically ands teh value in the accumulator with an 8-digit constant or
a value in two consecutive V-memory locations.
"""     

class logical_and_formatted(Instruction):
      code = "ANDF"
      description = """
DL06 Only. Logically ands teh value in the accumulator and a
specified range of discrete memory bits (1-32).
"""     

class logical_and_with_stack(Instruction):
      code = "ANDS"
      description = """
DL06 Only. Logically ands the value in the accumulator with the first
value in the accumulator stack.
"""     

class logical_or(Instruction):
      code = "OR"
      description = """
Logically ors the lower 16 bits in the accumulator with the first
value in the accumulator stack.
"""     

class logical_or_double(Instruction):
      code = "ORD"
      description = """
Logically ors teh value in the accumulator with an 8-digit constant or a 
value in two consecutive V-memory locations.
"""     

class logical_or_formatted(Instruction):
      code = "ORF"
      description = """
DL06 Only. Logically ors teh value in teh accumulator with a range of
discrete bits (1-32).
"""     

class logical_or_with_stack(Instruction):
      code = "ORS"
      description = """
DL06 Only. Logically ors the value in the accumulator with teh first
value in the accumulator stack.
"""     

class logical_exclusive_or(Instruction):
      code = "XOR"
      description = """
Performs an exclusive or of the value in the lower 16 bits of the 
accumulator and a V-memory location.
"""     

class logical_exclusive_or_double(Instruction):
      code = "XORD"
      description = """
Performs an exclusive or of the value in the accumulator and an
8-digit constant or a value in two consecutive V-memory locations.
"""     

class logical_exclusive_or_formatted(Instruction):
      code = "XORF"
      description = """
DL06 Only. Performs an exclusive or of the value in the accumulator
and a range of discrete bits (1-32).
"""     

class logical_exclusive_or_with_stack(Instruction):
      code = "XORS"
      description = """
DL06 Only. Performs an exclusive or of the value in the accumulator
and the first accumulator stack location.
"""     

class logical_compare(Instruction):
      code = "CMP"
      description = """
Compares teh value in the lower 16 bits of the accumulator with a 
V-memory location.
"""     

class logical_compare_double(Instruction):
      code = "CMPD"
      description = """
Compares teh value in the accumulator with two consecutive 
V-memory locations or an 8-digit constant.
"""     

class logical_compare_formatted(Instruction):
      code = "CMPF"
      description = """
DL06 only. Compares the value in the accumulator with a specified
number of discrete locations (1-32).
"""     

class logical_compare_with_stack(Instruction):
      code = "CMPS"
      description = """
DL06 only. Compares the value in the accumulator with the first 
accumulator stack location.
"""     

class logical_compare_real_number(Instruction):
      code = "CMPR"
      description = """
Dl06 Only. Compares the real number in the accumulator with two
consecutive V-memory locations or a real number constant.
"""     

class cpu_no_operation(Instruction):
      code = "NOP"
      description = """
Inserts a no operation coil at specified program address.
"""     

class cpu_end(Instruction):
      code = "END"
      description = """
Marks the termination point for the normal program scan. And End
instruction is required at the end of the main program body.
"""     

class cpu_stop(Instruction):
      code = "STOP"
      description = """
Changes the operational mode of the CPU from Run to Program (Stop)
"""     

class cpu_reset_watchdog_timer(Instruction):
      code = "RSTWT"
      description = """
Resets the CPU watchdog timer.
"""     

class drum_tuned_with_discrete_outputs(Instruction):
      code = "DRUM"
      description = """
Time driven drum with up to 16 steps and 16 discrete outputs points.
Output status is written to the appropriate output during each step.
Specify a time base per count (in milliseconds.) Each step can hava a
different number of counts to trigger the transition to the next step. Also
define preset step as destination when reset occurs.
"""     


class drum_time_and_event_with_discrete_outputs(Instruction):
      code = "EDRUM"
      description = """
Time and or event driven drum with up to 16 steps and 16 discrete
output points. Output status is written to the appropriate output
during each step. Specify a time base per count (in milliseconds.)
Each step can have a different number of counts and an event to trigger
the counting. Once the time has expired, a transition to the next step
occurs. Also define preset step as destination when reset occurs.
"""     


class drum_time_and_event_with_discreteoutputs_and_output_mask(Instruction):
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


class drum_time_and_event_with_word_output_and_output_mask(Instruction):
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


class comparative_boolean_store_if_equal(Instruction):
      code = "STRE"
      description = """
Begins a new rung or additional branch in a run with a normally
open comparative contact. The contact will be on when A = B.
"""     

class comparative_boolean_store_if_not_equal(Instruction):
      code = "STRNE"
      description = """
Begins a new rung or additional branch in a rung with a normally
closed comparative contact. The contact will be on when A is not
equal to B.
"""     

class comparative_boolean_or_if_equal(Instruction):
      code = "ORE"
      description = """
Connects a normally open comparative contact in parallel with another
contact. The ocntact will be on when A = B.
"""     

class comparative_boolean_or_if_not_equal(Instruction):
      code = "ORNE"
      description = """
Connects a normally closed comparative contact in parallel with
another contact. The contact will be on when A is not equal to B.
"""     

class comparative_boolean_and_if_equal(Instruction):
      code = "ANDE"
      description = """
Connects a normally open comparative contact in series with another
contact. The contact will be on when A = B.
"""     

class comparative_boolean_and_if_not_equal(Instruction):
      code = "ANDNE"
      description = """
Connects a normally closed comparative contact in series with another
contact. the contact will be on when A is not equal B.
"""     

class rllplus_initial_stage(Instruction):
      code = "ISG"
      description = """
The initial stage instruciton is used for a starting point for user
application program. The ISG instruction will be active on power up
and PROGRAM to RUN transitions.
"""     

class rllplus_stage(Instruction):
      code = "SG"
      description = """
Stage instructions are used to create structured programs. They are
program segments which can be activated or deactivated with control 
logic.
"""     

class rllplus_jump(Instruction):
      code = "JMP"
      description = """
Normally open coil that deactivates the active stage and activates a
specified stage when there is power flow to the coil.
"""     

class rllplus_not_jump(Instruction):
      code = "NJMP"
      description = """
Normally closed coil that deactivates the active stage and activates a
specified stage when there is power flow to the coil.
"""     

class rllplus_converge_stages(Instruction):
      code = "CV"
      description = """
Converge stages are a group of stages that when all stages are active
the associated converge jump(s). (CVJMP) will active another stage(s).
Once scan after teh CVJMP is executed, the converge stages will be 
deactivated.
"""     

class rllplus_converge_jump(Instruction):
      code = "CVJMP"
      description = """
Normally open coil that deactivates the active CV stages and activates
a specified stage when there is power flow to the coil.
"""     

class rllplus_block_call(Instruction):
      code = "BCALL"
      description = """

"""     
class rllplus_block(Instruction):
      code = "BLK"
      description = """

"""     
class rllplus_bend(Instruction):
      code = "BEND"
      description = """

"""     

class table_move(Instruction):
      code = "MOV"
      description = """
Moves the values from one V-memory table to another V memory table.
"""     

class table_move_memory_cartridge_load_label(Instruction):
      code = "MOVMC/LDLBL"
      description = """
DL06 Only. Copies data between V-memory and program ladder 
memory.
"""     

class table_set_bit(Instruction):
      code = "SETBIT"
      description = """
DL06 only. Sets a single bit (to a 0) in a V-memory location.
"""     

class table_reset_bit(Instruction):
      code = "RSTBIT"
      description = """
DL06 Only. Resets a single bit (to a 0) in a V-memory location.
"""     
 
class aslodata_load(Instruction):
      code = "LD"
      description = """
Loads a 16-bit word into the lower 16 bits of teh acummulator/stack.
"""     

class aslodata_load_double(Instruction):
      code = "LDD"
      description = """
Loads a 32-bit word into the accumulator/stack.
"""     

class aslodata_load_real_number(Instruction):
      code = "LDR"
      description = """
DL06 Only. Loads a real number contained in two consecutive
V-memory locations or a real constant into the accumulator.
"""     

class aslodata_load_formatted(Instruction):
      code = "LDF"
      description = """
Loads the accumuator with a specified number of consecutive discrete
memory bits.
"""     

class aslodata_load_address(Instruction):
      code = "LDA"
      description = """
Loads the accumulator with the HEX value for an octal constant
(address)
"""     

class aslodata_load_accumulator_indexed(Instruction):
      code = "LDX"
      description = """
Specifies a source address (V memory) which will be offset by the 
value in the first stack location.
"""     

class aslodata_out(Instruction):
      code = "OUT"
      description = """
Copies the value in the lower 16 bits of the accumulator to a specified
V memory location.
"""     

class aslodata_out_double(Instruction):
      code = "OUTD"
      description = """
Copies the value in the accumlator to two consecutive V memory
locations.
"""     

class aslodata_out_formatted(Instruction):
      code = "OUTF"
      description = """
Outputs a specified number of bits (1-32) from the accumulator to the 
specified discrete memory locations.
"""     

class aslodata_pop(Instruction):
      code = "POP"
      description = """
Moves the value from the first level of the accumulator stack to the 
accumulator and shifts each value in the stack up one level.
"""     

class aslodata_out_least(Instruction):
      code = "OUTL"
      description = """
DL06 only. Copies the value in the upper 8-bits of the lower accumulator
word (1st 16bits) to the lower 8 bits of a specified V-memory 
location.
"""     

class aslodata_out_most(Instruction):
      code = "OUTM"
      description = """
DL06 Only. Copies the value in the upper 8-bits of the lowe accumulator 
word (1st 16bits) to the upper 8 bits of a specified V-memory
location.
"""     

class aslodata_output_indexed(Instruction):
      code = "OUTX"
      description = """
DL06 only. Copies a 16-bit value from the first level of the accumulator
stack to a source address offset by the value in the accumulator.
"""     

class bit_sum(Instruction):
      code = "SUM"
      description = """
Counts the number of bits set to '1' in the accumulator. The HEX result
resides in the accumulator.
"""     

class bit_shift_left(Instruction):
      code = "SHFL"
      description = """
Shifts the bits in the accumulator a specified number of places to the left
"""     

class bit_shift_right(Instruction):
      code = "SHFR"
      description = """
Shifts the bits in the accumulator a specified number of places to the right
"""     

class bit_rotate_left(Instruction):
      code = "ROTL"
      description = """
Rotates teh bits in the accumulator a specified nubmer of places to the left
"""     

class bit_rotate_right(Instruction):
      code = "ROTR"
      description = """
Rotates teh bits in the accumulator a specified nubmer of places to the right
"""     

class bit_encode(Instruction):
      code = "ENCO"
      description = """
Encodes the bit position set to 1 in the accumulator, and returns the
appropriate binary representation in the accumulator.
"""     

class bit_decodes(Instruction):
      code = "DECO"
      description = """
Decodes a 5 bit binary value(0-31) in the accumulator by setting the
appropriate bit position to a 1.
"""     

class boolean_store(Instruction):
      code = "STR"
      description = """
Begins a new run or an additional branch in a rung with a normally
open contact.
"""          
      
class boolean_store_not(Instruction):
      code = "STRN"
      description = """
Begins a new run or an additional branch in a run with a normaly
closed contact.
"""           

class boolean_store_bit_of_word(Instruction):
      code = "STRB"
      description = """
DL06 Only. Begins a new run or an additional branch in a run with
a normally open V-memory bit-of-word contact.
"""     

class boolean_store_not_bit_of_word(Instruction):
      code = "STRNB"
      description = """
DL06 Only. Begins a new wrung or an additional branch in a run
with a normally closed V-memory bit-of-word contact.
"""     

class boolean_or(Instruction):
      code = "OR"
      description = """
Logically ors a normally open contact in parallel with another contact
in a run.
"""     

class boolean_or_not(Instruction):
      code = "ORN"
      description = """
Logically ors a normally closed contact in parallel with another contact
in a run.
"""     

class boolean_or_bit_of_word(Instruction):
      code = "ORB"
      description = """
DL06 Only. ors a normally closed open V-memory bit-of-word contact in 
parallel with another contact in a run.
"""     

class boolean_or_not_bit_of_word(Instruction):
      code = "ORNB"
      description = """
DL06 Only. ors a normally closed V-memory bit-of-word contact in
parallel with another contact in a run.
"""     

class boolean_and(Instruction):
      code = "AND"
      description = """
Logically ands a normally open contact in series with another contact
in a rung.
"""     

class boolean_and_not(Instruction):
      code = "ANDN"
      description = """
Logically ands a normally closed contact in series with another contact
in a rung.
"""     

class boolean_and_bit_of_word(Instruction):
      code = "ANDB"
      description = """
DL06 Only. ands a normally closed contact in series with another contact
in a rung.
"""     

class boolean_and_not_bit_of_word(Instruction):
      code = "ANDNB"
      description = """
DL06 Only. ands a normally closed contact in series with another contact
in a rung.
"""     

class boolean_and_store(Instruction):
      code = "ANDSTR"
      description = """
Logically ands two branches of a rung in series.
"""     

class boolean_or_store(Instruction):
      code = "ORSTR"
      description = """
Logically ors two branches of a rung in parallel.
"""     

class boolean_out(Instruction):
      code = "OUT"
      description = """
Reflects the status of the rung (on/off) and outputs the discrete (on/off)
state to the specified image register point or memory location.
"""     

class boolean_or_out(Instruction):
      code = "OROUT"
      description = """
Reflects the status of the rung and outputs the discrete (ON/OFF) state
to the image register. Multiple OR OUT instructions referencing the
smae discrete point can be used in the program.
"""     

class boolean_out_bit_of_word(Instruction):
      code = "OUTB"
      description = """
DL06 Only. Reflects status of the rung (on/off) and outputs the discrete
(on/off) state to teh specified bit in the referenced V-memory location.
"""     

class boolean_not(Instruction):
      code = "NOT"
      description = """
Inverts the status of teh run at the point of the instruction.
"""     

class boolean_positive_differential(Instruction):
      code = "PD"
      description = """
One-shot output coil. When the input logic produces an off to on
transition, the output will energize for one CPU scan.
"""     

class boolean_store_positive_differential(Instruction):
      code = "STRPD"
      description = """
Leading edge triggered one-shot contact. When the corresponding
memory location transitions from low to high, the contact comes on
for one CPU scan.
"""     

class boolean_store_negative_differential(Instruction):
      code = "STRND"
      description = """
Trailing edge triggered one-shot contact. When the corresponding
memory location transitions from low to high, the contact comes on
for one CPU scan.
"""     

class boolean_or_positive_differential(Instruction):
      code = "ORPD"
      description = """
Logically ors a leading edge triggered one-shot contact in parallel with
another contact in a run.
"""     

class boolean_or_negative_differential(Instruction):
      code = "ORPD"
      description = """
Logically ors a trailing edge triggered one-shot contact in parallel wiht
another contact in a rung.
"""     

class boolean_and_positive_differential(Instruction):
      code = "ANDPD"
      description = """
Logically ands a leading edge triggered one-shot contact in series with
another contact in a rung.
"""     

class boolean_and_negative_differential(Instruction):
      code = "ANDND"
      description = """
Logically ands a trailing edge triggered one-shot contact in series with
another contact in a rung.
"""     

class boolean_set(Instruction):
      code = "SET"
      description = """
An output that turns on a point or a range of points. The reset instruction
is used to turn the point(s) OFF that were set ON with teh set instruction.
"""     

class boolean_Reset(Instruction):
      code = "RST"
      description = """
An output that resets a point or a range of points.
"""     

class boolean_set_bit_of_word(Instruction):
      code = "SETB"
      description = """
DL06 Only. Sets or turns on a bit in a V-memory location.
"""     

class boolean_reset_bit_or_word(Instruction):
      code = "RSTB"
      description = """
DL06 Only. Resets or turns off a bit in a V-memory location
"""     

class boolean_pause_outputs(Instruction):
      code = "PAUSE"
      description = """
Disable the update for a range of specified 
"""     

class clock_date(Instruction):
      code = "DATE"
      description = """
Use to set the date in the CPU
"""     

class clock_time(Instruction):
      code = "TIME"
      description = """
Use to set the time in the CPU.
"""     

class lcd_lcd(Instruction):
      code = "LCD"
      description = """
Configures LCD display.
"""     

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

class interrupt_enable(Instruction):
      code = "ENI"
      description = """
Enables hardware and software interrupts to be acknowledged.
"""     

class message_fault_label(Instruction):
      code = "FAULT"
      description = """
Displays a V-memory value or a data label constant to the hand-held
programmer or personal computer using DirectSOFT.
"""     

class message_data_label(Instruction):
      code = "DLBL"
      description = """

"""     

class message_numerical_constant(Instruction):
      code = "NCON"
      description = """
Stores constants in numerical form for use with other 
instructions.
"""     

class message_ascii_constant(Instruction):
      code = "ACON"
      description = """
Stores constants in ascii form for use with other 
instructions.
"""     


class message_print(Instruction):
      code = "PRINT"
      description = """
Prints teh embedded text or text/data variable message to the specified
communications port. Maximumum message length is 255 words.
appropriate bit position to 1 in the accumulator.
"""     

class tcsregister_timer(Instruction):
      code = "TMR"
      description = """
Single input incrementing timer with 0.1 second resolution (0-999.9 seconds)
"""     

class tcsregister_fast_timer(Instruction):
      code = "TMRF"
      description = """
Single input incrementing timer with 0.01 second resolution (0-99.99 seconds)
"""     

class tcsregister_accumulating_timer(Instruction):
      code = "TMRA"
      description = """
Two input incrementing timer with 0.1 second resolution
(0-9,999,999.99 sec.) Time and enable/reset inputs control the timer
"""     

class tcsregister_accumulating_fast_timer(Instruction):
      code = "TMRAF"
      description = """
Two input incrementing timer with 0.01 second resolution
(0-99,999.99 sec) Time and enable/reset inputs control the timer.
"""     

class tcsregister_counter(Instruction):
      code = "CNT"
      description = """
Two input incrementing counter (0-9999). Count and reset inputs 
control the counter.
"""     

class tcsregister_stage_counter(Instruction):
      code = "SGCNT"
      description = """
Single input incrementing counter (0-9999) RST instruction must be
used to reset count.
"""     

class tcsregister_up_down_counter(Instruction):
      code = "UDC"
      description = """
Three input counter (0-99,999,999). Up, down and reset inputs control
the counter.
"""     

class tcsregister_shift_register(Instruction):
      code = "SR"
      description = """
Shifts data through a range of control relays with each clock pulse. The
data clock and reset inputs control the shift register.
"""     

class intelligent_read_from_module(Instruction):
      code = "RD"
      description = """
Reads a block of memory from an intelligent I/O module into the CPU's 
V-memory.
"""     

class intelligent_write_to_module(Instruction):
      code = "WT"
      description = """
Writes a block of data to an intelligent I/O module from a block of
CPU's V-memory.
"""     

class transcendental_square_root_real(Instruction):
      code = "SQRTR"
      description = """
Takes the square root of the real number stored in the accumulator. The
result resides in the accumulator.
"""     

class transcendental_sine_real(Instruction):
      code = "SINR"
      description = """
Takes the sine of the real number stored in the accumulator. The result
resides in the accumulator.
"""     

class transcendental_cosine_real(Instruction):
      code = "COSR"
      description = """
Takes the cosine of the real number stored in the accumulator. The 
result resides in the accumulator.
"""     

class transcendental_tangent_real(Instruction):
      code = "TANR"
      description = """
Takes the tangent of the real number stored in the accumulator. The
result resides in the accumulator.
"""     

class transcendental_arc_sine_real(Instruction):
      code = "ASINR"
      description = """
Takes teh inverse sine of the real number stored in the accumulator. The
result resides in the accumulator.
"""     

class transcendental_arc_cosine_real(Instruction):
      code = "ACOSR"
      description = """
Takes the inverse cosine of teh real number stored in the accumulator.
The result resides in the accumulator.
"""     

class transcendental_arc_tangent_real(Instruction):
      code = "ATANR"
      description = """
Takes the inverse tangent of the real number stored in the accumulator.
The result resides in the accumulator.
"""     




      
