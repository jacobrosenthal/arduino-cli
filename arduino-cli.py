import subprocess, sublime, sublime_plugin

def get_setting(name):
    settings = sublime.load_settings('arduino-cli.sublime-settings')
    return sublime.active_window().active_view().settings().get(name, settings.get(name))

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

        print(args)
        try:
            a = subprocess.check_output(args, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            print(e.output)
        else:
            print(a)

class ArduinoverifyCommand(ArduinoCommand):
    action = "verify"

class ArduinouploadCommand(ArduinoCommand):
    action = "upload"
