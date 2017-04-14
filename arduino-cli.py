import subprocess, sublime, sublime_plugin
import glob

def get_setting(name):
    settings = sublime.load_settings('arduino-cli.sublime-settings')
    return sublime.active_window().active_view().settings().get(name, settings.get(name))

class ArduinocliCommand(sublime_plugin.WindowCommand):

    def run(self, **kwargs):
        sublime.set_timeout_async(lambda: self.go(kwargs), 0)

    def go(self, options):

        compiler_path = get_setting('path')
        if "?" in compiler_path or "*" in compiler_path:
            compiler_paths = glob.glob(compiler_path)
            assert len(compiler_paths) == 1, "There should be only one compiler matching the given path (See arduino-cli (Platform).sublime-settings file"
            compiler_path = compiler_paths[0]

        args = [compiler_path]

        board = get_setting('board')
        if board:
            args += ["--board", board]

        port = get_setting('port')
        if (port and "--verify" not in options['cmd']):
            args += ["--port", port]

        sketchbook_path = get_setting('sketchbook.path')
        if sketchbook_path:
            args += ["--pref", "sketchbook.path={}".format(sketchbook_path)]

        args += options['cmd']

        options['cmd'] = args

        self.window.run_command("exec", options)
