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

class compare_vmemory(Instruction):
      code = "CMPV"
      description = """
Compares two blocks of V-memory
"""     

class swap_bytes(Instruction):
      code = "SWAPB"
      description = """
Swaps V-memory bytes.
"""     

class print_to_vmemory(Instruction):
      code = "VPRINT"
      description = """
Used to send pre-coded ASCII strings to a pre-defined V-memory
address when enabled.
"""     

class print_from_vmemory(Instruction):
      code = "PRINTV"
      description = """
Used to write raw ASCII string out of port 2 when enabled.
"""     
