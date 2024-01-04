from pyfirmata import Arduino, util
from time import sleep
board = Arduino('/dev/ttyUSB0')
led = 9
it = util.Iterator(board) 
it.start()
vrx_pin = 0
vry_pin = 1
sw_pin = 5
board.analog[vrx_pin].enable_reporting()
board.analog[vry_pin].enable_reporting()

while True: 
    vrx_value = board.analog[vrx_pin].read()
    vry_value = board.analog[vry_pin].read() 

    print("Value of vrx: ", vrx_value)
    print("Value of vry: ", vry_value) 

    if vrx_value == None:
         vrx_value = 0
    elif vrx_value > 0.05: 
          board.digital[led].write(1) 
          sleep(vrx_value) 
          board.digital[led].write(0) 
          sleep(vrx_value)