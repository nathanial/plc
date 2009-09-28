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
