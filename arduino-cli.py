import subprocess, sublime, sublime_plugin

def get_setting(name):
    settings = sublime.load_settings('arduino-cli.sublime-settings')
    return sublime.active_window().active_view().settings().get(name, settings.get(name))

class ArduinocliCommand(sublime_plugin.WindowCommand):

    def run(self, **kwargs):
        sublime.set_timeout_async(lambda: self.go(kwargs), 0)

    def go(self, options):

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

        args += options['cmd']

        options['cmd'] = args

        self.window.run_command("exec", options)
