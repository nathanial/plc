from plc.instructions.instruction import Instruction
class read_from_network(Instruction):
      code = "RX"
      description = """
Reads a block of data from another CPU on the network.
"""     

class write_to_network(Instruction):
      code = "WX"
      description = """
Writes a block of data from the master device to a slave device on
the network.
"""     
