import subprocess, sublime, sublime_plugin, time

def get_setting(name):
    settings = sublime.load_settings('arduino-cli.sublime-settings')
    return sublime.active_window().active_view().settings().get(name, settings.get(name))
#removes the b'....' from the output string and fixes the newlines.
def clean_output(arg):
    output = str(arg)
    output = output[2:-1].replace("\\n","\n")
    return output

class ArduinoCommand(sublime_plugin.WindowCommand):

    def run(self, **kwargs):
        sublime.set_timeout_async(lambda: self.go(kwargs), 0)

    def go(self, options):
        ino = options["working_dir"]

        args = [get_setting('path')]

        board = get_setting('board')
        if board:
            args += ["--board", board]

        port = get_setting('port')
        if port:
            args += ["--port", port]

        sketchbook_path = get_setting('sketchbook.path')
        if sketchbook_path:
            args += ["--pref", "sketchbook.path={}".format(sketchbook_path)]

        args += ["--{}".format(self.action), ino]

        #get start time
        now = time.strftime("%H:%M:%S")
        print("\n----BEGIN----"+now+"\n")
        print(args)
        try:
            a = subprocess.check_output(args, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            now = time.strftime("%H:%M:%S")
            print("\n----ERROR----"+now+"\n")
            output = clean_output(e.output)
            print(output)
        else:
            now = time.strftime("%H:%M:%S")
            print("\n----DONE----"+now+"\n")
            output = clean_output(a)
            print(output)

class ArduinoverifyCommand(ArduinoCommand):
    action = "verify"

class ArduinouploadCommand(ArduinoCommand):
    action = "upload"
