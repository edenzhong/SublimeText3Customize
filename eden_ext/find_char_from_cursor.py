import sublime, sublime_plugin

class FindCharFromCursorCommand(sublime_plugin.TextCommand):
	def run(self, edit, pattern):
		rs = self.view.sel()
		start_pos = rs[0].a + 1
		r = self.view.find(pattern, start_pos,sublime.LITERAL)
		if r.a < 0:
			return
		r.b = r.a
		rs.clear()
		rs.add(r)
		
