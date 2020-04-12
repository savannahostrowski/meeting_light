#!/Users/savannah/Documents/code/mini-project/venv/bin/python
import pyfirmata
import time
from get_calendar_events import is_savannah_in_meeting

print("Connected to port")

def update_led():
    savannah_in_meeting = is_savannah_in_meeting()

    green_led = board.digital[12]
    red_led = board.digital[13]

    if savannah_in_meeting:
        on_led = red_led
        off_led = green_led
    else:
        on_led = green_led
        off_led = red_led
    on_led.write(1)
    off_led.write(0)

while True:
    update_led()
    time.sleep(5)