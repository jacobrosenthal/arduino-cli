import subprocess, shlex, sublime, sublime_plugin

class ArduinouverifyCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        sublime.set_timeout_async(self.go(kwargs), 0)

    def go(self, kwargs):
        ino = kwargs["working_dir"]
        settings = sublime.load_settings('arduino-cli.sublime-settings')
        path = settings.get('path')
        board = settings.get('board')
        tmp = settings.get('tmp')
        port = settings.get('port')

        command_line = path + "Arduino --board " + board + " --pref build.path=" + tmp +  " --verify " + ino
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
        sublime.set_timeout_async(self.go(kwargs), 0)

    def go(self, kwargs):
        ino = kwargs["working_dir"]
        settings = sublime.load_settings('arduino-cli.sublime-settings')
        path = settings.get('path')
        board = settings.get('board')
        tmp = settings.get('tmp')
        port = settings.get('port')

        command_line = path + "Arduino --board " + board + " --pref build.path=" + tmp +  " --upload " + ino + " --port " + port
        print(command_line)
        args = shlex.split(command_line)
        try:
            a = subprocess.check_output(args, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            print(e.output)
        else:
            print(a)

