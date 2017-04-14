import subprocess, sublime, sublime_plugin
import os
import glob

SKETCH_FILE_EXTENSTION = ".ino"
SKETCH_FILE_PATTERN = "*.ino"

def get_setting(name):
    settings = sublime.load_settings('arduino-cli.sublime-settings')
    return sublime.active_window().active_view().settings().get(name, settings.get(name))

class ArduinocliCommand(sublime_plugin.WindowCommand):

    def run(self, **kwargs):
        sublime.set_timeout_async(lambda: self.go(kwargs), 0)

    def _find_ino_file(self, filename):
        project_dir = os.path.dirname(filename)
        
        # The .ino file is probably in the current directory,
        # but maybe it's in the parent directory
        for d in [".", ".."]:
            ino_files = glob.glob(os.path.join(project_dir, d, SKETCH_FILE_PATTERN))
            if len(ino_files) == 1:
                return os.path.normpath(ino_files[0])
        
        raise ValueError("There should be exactly one .ino file in the project directory")
        
    def _get_filename(self):
        return sublime.active_window().active_view().file_name()
        
    def _set_ino_file(self, cmd):
        filename = self._get_filename()
        cmd[cmd.index(filename)] = self._find_ino_file(filename)
        
    def _is_ino_file(self):
        return self._get_filename().endswith(SKETCH_FILE_EXTENSTION)
        
    def go(self, options):

        args = [get_setting('path')]

        board = get_setting('board')
        if board:
            args += ["--board", board]

        port = get_setting('port')
        if (port and "--verify" not in options['cmd']):
            args += ["--port", port]

        sketchbook_path = get_setting('sketchbook.path')
        if sketchbook_path:
            args += ["--pref", "sketchbook.path={}".format(sketchbook_path)]

        cmd = options['cmd']
        
        if not self._is_ino_file():
            self._set_ino_file(cmd)
        
        args += cmd

        options['cmd'] = args

        self.window.run_command("exec", options)
