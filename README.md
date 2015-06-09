Arduino Build System for Sublime Text 3
---------------------------------------

Utilizes the new Arduino command line interface and as such requires Arduino to be installed. 

NOTE: OSX only right now, PRs welcome.

INSTALL
-------
Use [Package Control](https://packagecontrol.io/installation) to install. Within Sublime Text, bring up the Command Palette and type install. Among the commands you should see Package Control: Install Package. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins. When the plugin list appears, type arduino-cli

USE
---
Use Tool->Arduino->Open User Settings to set

 * path - The path to the Arduino executable. eg /Applications/Arduino.app/Contents/MacOS
 * board - The vendor:architecture:board. See the [Arduino CLI docs](https://github.com/arduino/Arduino/blob/ide-1.5.x/build/shared/manpage.adoc). eg arduino:avr:uno
 * port - The serialport to upload with. eg /dev/tty.usbmodem1411
 * sketchbook.path - (optional) The directory to look for additonal libraries and architectures in. eg /Users/jacobrosenthal/Documents/firmware-pinoccio/

While viewing a .ino file, use Command + b builds and upload to your board. Command + Shift + B lets you select to just build.
