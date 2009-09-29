
class InstructionType(type):
    def __new__(cls,name,bases,dct):
        print "Registering Instruction %s" % name
        return type.__new__(cls,name, bases, dct)

class Instruction(object):
    __metaclass__ = InstructionType
