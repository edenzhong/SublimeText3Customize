import sublime, sublime_plugin

class TestCommand(sublime_plugin.TextCommand):
	def fun(self):
		print("this is fun")

	def run(self, edit):
		#sublime.active_window().show_quick_panel(["a","s","d","f"],self.fun)
		
		self.fun()
		#self.view.sel().add(sublime.Region(34,40))
