Arduino Build System for Sublime Text 3
---------------------------------------

Utilizes the new Arduino command line interface and as such requires Arduino to be installed. 

NOTE: OSX only right now, PRs welcome.

INSTALL
-------
```bash
cd '/Users/YOUR USER/Library/Application\ Support/Sublime\ Text\ 3/Packages'
git clone https://github.com/jacobrosenthal/arduino-cli.git
```

USE
---
Use Tool->Arduino->Open User Settings to set

 * tmp - The temporary directory to build in, be careful, Arduino may rm -rf this. eg /Users/jacobrosenthal/Downloads/build/
 * path - The path to the Arduino executable. eg /Applications/Arduino.app/Contents/MacOS/
 * board - The vendor:architecture:board. See the [Arduino CLI docs](https://github.com/arduino/Arduino/blob/ide-1.5.x/build/shared/manpage.adoc). eg arduino:avr:uno
 * port - The serialport to upload with. eg /dev/tty.usbmodem1411

Board is slightly confusing, but its the vendor:architecture:board. 

Command + B Builds and uploads to your board. Command + Shift + B lets you select to only build.