Arduino Build System for Sublime Text 3
---------------------------------------

Utilizes the [Arduino command line interface](https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc) and as such requires Arduino to be installed.

NOTE - If you're updating from v0.0.3 you may need to alter your path to the Arduino executable, instead of the Arduino folder as in previous versions. See below for examples.

INSTALL
-------
Use [Package Control](https://packagecontrol.io/installation) to install. Within Sublime Text, bring up the Command Palette and type install. Among the commands you should see Package Control: Install Package. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins. When the plugin list appears, type arduino-cli

USE
---
While viewing a .ino file, use Command + b builds and upload to your board. Command + Shift + B lets you 
select to just build.

SETTINGS
--------
Settings include:
 * path - The path to the Arduino executable. eg /Applications/Arduino.app/Contents/MacOS/Arduino
 * board - (optional) The package:arch:board. See the [Arduino CLI docs](https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc). eg arduino:avr:uno
 * port - (optional) The serialport to upload with. eg /dev/tty.usbmodem1411
 * sketchbook.path - (optional) The directory to look for additonal libraries and architectures in. eg /Users/jacobrosenthal/Documents/firmware-pinoccio/

All settings are optional with Path being set internally to likely candidate based on OS. If board and port are not specified, the arduino executable will pull the settings from those last set in the graphical IDE. However you may wish to override


You can set them two places. Use Tool->Arduino->Open User Settings. This is an example override configuration for OS X:
```json
{
  "path": "/Applications/Arduino.app/Contents/MacOS/Arduino",
  "board": "arduino:avr:uno",
  "port": "/dev/tty.usbmodem1421"
} 
```

Or you can override sublime's settings on a per project basis by adding this to the root folder with the file name whatever.sublime-project and then open it to launch your project in Sublime
```
{
  "folders":
  [
    {
      "path": "."
    }
  ],
  "settings":
  {
    "path": "/Applications/Arduino.app/Contents/MacOS/Arduino",
    "board": "arduino:avr:uno",
    "port": "/dev/tty.usbmodem1421",
    "sketchbook.path": "/Users/jacobrosenthal/Documents/Arduino"
  }
}
```

TODO
--------
Sadly I dont have the regex working yet to bring console messages into the status bar. See [this issue](https://github.com/jacobrosenthal/arduino-cli/issues/1) if you think you can help