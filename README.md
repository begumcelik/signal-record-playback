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
- Record script is written in [Python3.9.](https://www.python.org/downloads/release/python-390/). To run the script you need to install following packages:
```pip install pyserial</br>
   pip install pandas```
- Download `signal-recorder.ino` `record-playback.ino` and `serial_read.py`.

## Step 1: Recording the Signal Output

- Open `signal-recorder.ino` in Teensyduino.
- Run `serial_read.py`
`python3.9 '/path/to/serial_read.py'`

### Output

## Step 2: Playback the Recording


## Contact
begumcelik@sabanciuniv.edu

## License 

