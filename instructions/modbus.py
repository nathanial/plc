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

