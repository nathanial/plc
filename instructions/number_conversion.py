from plc.instructions.instruction import Instruction
class binary(Instruction):
      code = "BIN"
      description = """
Converts teh BCD value in the accumulator to the equivalent binary
value. The result resides in the accumulator.
"""     

class binary_coded_decimal(Instruction):
      code = "BCD"
      description = """
Converts the binary value in the accumulator to the equivalent BCD
value. The result resides in the accumulator.
"""     

class invert(Instruction):
      code = "INV"
      description = """
Takes the one's complement of the 32-bit value in the accumulator. The
result resides in the accumulator.
"""     

class tens_complement(Instruction):
      code = "BCDCPL"
      description = """
DL06 Only. Takes the 10's complement (BCD) of the 8-digit accumulator.
"""     

class ascii_to_hex(Instruction):
      code = "ATH"
      description = """
Converts a table of ASCII values to a table of hexadecimal values.
"""     

class hex_to_ascii(Instruction):
      code = "HTA"
      description = """
Converts a table of hexadecimal values to a table of ASCII values.
"""     

class segment(Instruction):
      code = "SEG"
      description = """
DL06 Only. Converts four digit HEX value in accumulator to seven
segment display format.
"""     

class gray_code_to_bcd(Instruction):
      code = "GRAY"
      description = """
Converts a 16-bit GRAY code value in the accumulator to a 
corressponding BCD value. The result resides in the accumulator.
"""     

class shuffle_digits(Instruction):
      code = "SFLDGT"
      description = """
Shuffles a maximum of 8 digits, rearranging them in a specified order.
The result resides in the accumulator.
"""     

class radina_real_conversion(Instruction):
      code = "RADR"
      description = """
DL06 ONly. Converts teh real degree value in the accumulator to the
equivalent real number in radians. the result resides in the accumulator.
"""     

class degree_real_conversion(Instruction):
      code = "DEGR"
      description = """
DL06 Only. Converts the real radian value in the accumulator to the
equivalent real member of degrees. The result resides in the accumulator.
"""     

class binary_to_real_number(Instruction):
      code = "BTOR"
      description = """
DL06 Only. Converts the binary value in the accumulator into a real
number. The result resides in the accumulator.
"""     

class real_to_binary(Instruction):
      code = "RTOB"
      description = """
DL06 Only. Converts the real number in the accumulator into a binary
value. The result resides in the accumulator.
"""     


