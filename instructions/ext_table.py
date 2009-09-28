class fill(Instruction):
      code = "FILL"
      description = """
Fills a table of specified V-memory locations with a value which is either
a V-memory location or a 4-digit constant.
"""     

class find(Instruction):
      code = "FIND"
      description = """
Finds a value in a V-memory table and returns the table position 
containing the value to the accumulator.
"""     

class find_greater_than(Instruction):
      code = "FDGT"
      description = """
Finds a value in a V-memory table which is greater than the specified
search value. The table position containing the value is returned to the 
accumulator.
"""     

class find_block(Instruction):
      code = "FINDB"
      description = """
Finds a block of data values in a V-memory table and returns the starting
address of the table containing the values to teh accumulator.
"""     

class table_to_destination(Instruction):
      code = "TTD"
      description = """
Moves the value from the top of a V-memory table to a specified
V-memory location. The table pointer increments each scan.
"""     

class remove_from_bottom(Instruction):
      code = "RFB"
      description = """
Moves the value from the bottom of a v-memory table to a specified
V-memory location. The table pointer increments each scan.
"""     

class source_to_table(Instruction):
      code = "STT"
      description = """
Moves a value from specified V-memory location to a V-memory table.
The table pointer increments each scan.
"""     

class remove_from_top(Instruction):
      code = "RFT"
      description = """
Pops a value from the top of a V-memory table and stores it in a
specified V-memory location. All other values in the V-memory table 
are shifted up each time a value is popped from table.
"""     

class add_to_top_table(Instruction):
      code = "ATT"
      description = """
Pushes a value from a specified V-memory location onto top of a 
V-memory table. All other values in the V-memory table are shifted
down each time a value is pushed onto the table.
"""     

class table_shift_left(Instruction):
      code = "TSHFL"
      description = """
Shifts specified number of bits to the left in a V-memory table
"""     

class table_shift_right(Instruction):
      code = "TSHFR"
      description = """
Shifts specified number of bits to the right in a V-memory table.
"""     

class and_move(Instruction):
      code = "ANDMOV"
      description = """
Copies data from a table to the specified location, ANDing each word
with the accumulator data as it is written.
"""     

class or_move(Instruction):
      code = "ORMOV"
      description = """
Copies data from a table to the specified memory location, ORing each
word with the accumulator data as it is written.
"""     

class exclusive_or_move(Instruction):
      code = "XORMOV"
      description = """
Copies data from a table to the specified memory location, XORing
each word with the accumulator data as it is written.
"""     

class swap(Instruction):
      code = "SWAP"
      description = """
Exchanges teh data in two tables of equal length.
"""     
