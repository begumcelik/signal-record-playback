# Record and Playback the Signal Output of Black Box System

This project is designed to record the signal output of Stephan von Huene's artwork called _What’s wrong with Art? (1997)_. Nonetheless, the project can be thought of as a generic conservation workflow for artworks working in a similar manner. </br>
The artwork consists of three Energy Star computers of its age, and computers are in a functional state in the ZKM collection. The program controls the organ pipe blower that plays a melody by blowing into organ pipes alongside playing the audio recording repeating "What's wrong with art?". However, the source code of the program is not available today and to restage the work in the future without relying on the status of the old computers necessitates conservation practice to not let the artwork die with computers. 

_This project is developed in ZKM Karlsruhe._

Developed with:
- [Arduino Teensy 4.1.](https://www.pjrc.com/store/teensy41.html)
- [Audio Shield for Teensy 4](https://www.pjrc.com/store/teensy3_audio.html)

## Supervisor
- [Daniel Heiss](https://zkm.de/de/person/daniel-heiss)

## Developer
- Begüm Çelik

## Download
- Install Teensyduino software add-on with Arduino IDE. ([Teensyduino version 1.57](https://www.pjrc.com/teensy/td_download.html))
- Install [SD library](https://www.arduino.cc/reference/en/libraries/sd/) from `Sketch > Include Library > Manage Libraries`
- The recording script is written in [Python3.9.](https://www.python.org/downloads/release/python-390/) To run the script you need to install following packages:
```
pip install pyserial
pip install pandas
```
- Download `signal-recorder.ino` `record-playback.ino` and `serial_read.py`.

## Step 1: Recording the Signal Output
- In order to record the signal output of the computer, the DeLock DB37MT connector is inserted into the relay card (SMARTLAB, 8 Channels Relay Output) of the computer and is wired to the Teensy board. (input pins: 34-41)
- The python script reads the serial data and writes it into csv file.
- Open `signal-recorder.ino` in Teensyduino, upload the code into your board.
- Change the path to where you want to save your csv files and run `serial_read.py` </br>
`python3.9 '/path/to/serial_read.py'`

### Output
- The python script will save the signal output to csv file in the following format:
```
1st column: #timestamp in ms (the time when the change in signal happened)
2nd to 9th: #state of the signals (either 1 or 0)
2018773	1	1	1	1	1	1	1	0
2024744	1	1	0	1	1	1	1	0
2024756	1	1	0	1	1	0	1	0
2025015	1	1	0	1	1	1	1	0
```

## Step 2: Playback the Recording


## Contact
begumcelik@sabanciuniv.edu

## License 

