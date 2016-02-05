Arduino Build System for Sublime Text 3
---------------------------------------

Utilizes the new Arduino command line interface and as such requires Arduino to be installed. 

NOTE: OSX only right now, PRs welcome.

INSTALL
-------
Use [Package Control](https://packagecontrol.io/installation) to install. Within Sublime Text, bring up the Command Palette and type install. Among the commands you should see Package Control: Install Package. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins. When the plugin list appears, type arduino-cli

USE
---
While viewing a .ino file, use Command + b builds and upload to your board. Command + Shift + B lets you select to just build.

SETTINGS
--------
Settings include:
 * path - The path to the Arduino executable. eg /Applications/Arduino.app/Contents/MacOS/Arduino
 * board - (optional) The vendor:architecture:board. See the [Arduino CLI docs](https://github.com/arduino/Arduino/blob/ide-1.5.x/build/shared/manpage.adoc). eg arduino:avr:uno
 * port - (optional) The serialport to upload with. eg /dev/tty.usbmodem1411
 * sketchbook.path - (optional) The directory to look for additonal libraries and architectures in. eg /Users/jacobrosenthal/Documents/firmware-pinoccio/

If board and port are not specified anywhere, the arduino executable will pull the settings from those last set in the graphical IDE.


You can set them two places. Use Tool->Arduino->Open User Settings. This is an example configuration for OS X:
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
		"board":"pinoccio:avr:atmega256rfr2",
		"port":"/dev/tty.usbmodem1411",
		"sketchbook.path":"/Users/jacobrosenthal/Documents/firmware-pinoccio"
	}
}
```

CONSOLE
--------
If you want feedback on what happened, use View->Show Console. Sadly I dont have the regex working yet to bring this into the status bar. See [this issue](https://github.com/jacobrosenthal/arduino-cli/issues/1) if you think you can help