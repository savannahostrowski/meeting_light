import pyfirmata
import time
board=pyfirmata.Arduino('/dev/cu.usbserial-1420')

it = pyfirmata.util.Iterator(board)
it.start()

print("Connected to port")

button = board.digital[2]
led = board.digital[12]

button.mode = pyfirmata.INPUT

led_state = 0
prev_led_state = 0

while True:
    switch = button.read()
    print(prev_led_state, led_state, switch)
    if switch is not None and int(switch) == 1:
        prev_led_state = led_state
        led_state = int(not led_state)
        led.write(led_state)
    time.sleep(0.3)