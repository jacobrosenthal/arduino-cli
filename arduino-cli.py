import subprocess, shlex, sublime, sublime_plugin

class ArduinoverifyCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        sublime.set_timeout_async(lambda: self.go(kwargs), 0)

    def go(self, options):
        ino = options["working_dir"]
        settings = sublime.load_settings('arduino-cli.sublime-settings')
        path = settings.get('path')
        board = settings.get('board')
        port = settings.get('port')

        command_line = path + "/Arduino --board " + board + " --verify " + ino

        if settings.get('sketchbook.path'):
            command_line += " --pref sketchbook.path=" + settings.get('sketchbook.path')
        
        print(command_line)
        args = shlex.split(command_line)
        try:
            a = subprocess.check_output(args, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            print(e.output)
        else:
            print(a)

class ArduinouploadCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        sublime.set_timeout_async(lambda: self.go(kwargs), 0)

    def go(self, options):
        ino = options["working_dir"]
        settings = sublime.load_settings('arduino-cli.sublime-settings')
        path = settings.get('path')
        board = settings.get('board')
        port = settings.get('port')

        command_line = path + "/Arduino --board " + board + " --upload " + ino + " --port " + port

        if settings.get('sketchbook.path'):
            command_line += " --pref sketchbook.path=" + settings.get('sketchbook.path')

        print(command_line)
        args = shlex.split(command_line)
        try:
            a = subprocess.check_output(args, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            print(e.output)
        else:
            print(a)

