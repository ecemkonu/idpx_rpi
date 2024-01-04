from pyfirmata import Arduino, util
from time import sleep
board = Arduino('/dev/ttyUSB0')
led = 9
it = util.Iterator(board) 
it.start()
vrx = 0
vry = 1
sw = 5
board.analog[vrx].enable_reporting()
board.analog[vry].enable_reporting()

while True: 
     value = board.analog[0].read() 
     print(value) 
     if value == None: 
          value = 0
     elif value > 0.05: 
          board.digital[led].write(1) 
          sleep(value) 
          board.digital[led].write(0) 
          sleep(value)