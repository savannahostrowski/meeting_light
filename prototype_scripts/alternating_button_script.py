import pyfirmata
import time
board=pyfirmata.Arduino('/dev/cu.usbserial-1420')

it = pyfirmata.util.Iterator(board)
it.start()

print("Connected to port")

button = board.digital[2]
green_led = board.digital[12]
red_led = board.digital[13]

button.mode = pyfirmata.INPUT

on_led = red_led
on_led.write(1)

while True:
    switch = button.read()

    if switch is not None and int(switch) == 1:
        on_led.write(0)
        on_led = green_led if on_led == red_led else red_led
        on_led.write(1)

    time.sleep(0.3)