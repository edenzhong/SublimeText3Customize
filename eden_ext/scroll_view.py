import sublime, sublime_plugin

class ScrollHalfDownCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		r = self.view.visible_region()
		self.view.show_at_center(r.b)

class ScrollHalfUpCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		r = self.view.visible_region()
		self.view.show_at_center(r.a)
