# Meeting Light PhysiDig Mini Project
This project was created as part of the experiential research the physidig team conducted as part of as part of our capstone project.

## Getting started for /app (the main project)
### Required materials
- Arduino Uno
- 3 Male-to-Male Jumper Wires
- Two LEDs (one red and one green)
- 2 220 ohm resistors
- USB A to USB B cord

### Arduino Setup
- Plug in your Arduino Uno to your machine
- Launch the [Arduino IDE software](https://www.arduino.cc/en/main/software) (note that I built this on MacOS Catalina)
- Configure your board and port via top menu bar > Tools > Board > Select Arduino Uno and Tools > Port > some serial bus port (mine was 1420)
- Load the StandardFirmata code example via File > Examples > Firmata > StandardFirmata
- Compile and load this example onto your Arduino Uno (so you can control your board via the Firmata protocol)

Great, now your board is ready to run the Python Firmata client - pyfirmata!

- Unplug your board from your machine to cut power
- Assemble this circuit


<insert schematic>
  
  
- Plug your board back in


### Google Calendar API Setup
- Go to the [Google Calendar API Guide](https://developers.google.com/calendar/quickstart/python)
- Click 'Enable Google Calendar API' (note that you need a Google account)
  - This will open a module and download a `credentials.json` file which you should copy into the root of the project

### Code Setup
#### Install Required Packages
- Open this repo in your editor/IDE of choice (I like Visual Studio Code ;) )
- Select Python 3.7 as your interpreter
- Create a virtual environment via `python3 -m venv venv`
- Install the requirements.txt via `pip install -r requirements.txt` to install required packages

#### Configure your calendar
- Create a file called `calendar_id.py` in the `/app` directory with a constant called 'CAL_ID'
- Go to your [Google Calendar](https://calendar.google.com/calendar/r) 
- Find a calendar you want to use
- Click the Options (the three dots beside the calendar name) > Settings 
- Scroll to 'Integrate Calendar' and copy the ID (your default calendar ID is 'primary')
- Paste this ID as the value for your `CAL_ID` constant
- Open the `app/get_calendar_events.py` and run it
- In the terminal, you should see a Google link 
- Click the link to authenticate in the browser. Once you've done this, the browser will tell you that you can close the window
- Go back to your editor/terminal and verify that there are no other errors


### Running the script
- Go to `/app/hardware_interface.py`
- Replace the port in the `board=pyfirmata.Arduino('/dev/cu.usbserial-1420')` line if your port is not 1420
- Run this file and you should now see one of your LEDs light up on your board (red if your calendar says you are in a meeting and green if you are free)
  - You can test this by creating a new meeting on your Google calendar and verify that LEDs switch
  



