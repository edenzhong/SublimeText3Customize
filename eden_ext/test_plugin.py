import sublime, sublime_plugin
from .str_plus import clear_cpp_comment

class TestPluginCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		w = sublime.active_window()
		v = w.create_output_panel("context")
		self.view.run_command("show_panel",{"panel":"output.context"})
		sublime.message_dialog("done")
		#v = sublime.Window.create_output_panel("context")
		return

		sel = self.view.sel()
		r = sel[0]
		s = self.view.substr(r)
		sublime.message_dialog(s)
		s = clear_cpp_comment(s)
		
		sublime.message_dialog(s)
