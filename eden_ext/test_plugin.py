import sublime, sublime_plugin
from .str_plus import clear_cpp_comment

class TestPluginCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sel = self.view.sel()
		r = sel[0]
		s = self.view.substr(r)
		sublime.message_dialog(s)
		s = clear_cpp_comment(s)
		
		sublime.message_dialog(s)
