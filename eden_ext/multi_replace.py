import sublime, sublime_plugin

class multi_replace(sublime_plugin.TextCommand):
	def run(self, edit):
		'''Select multi regions, replace each region by context in clipboard. Each line of clipboard replace one region.'''
		cursel = self.view.sel()
		clip_cont = sublime.get_clipboard()
		replace_src = clip_cont.splitlines()
		i = 0
		for sel_region in cursel:
			if ( i < len(replace_src)):
				self.view.replace(edit,sel_region,replace_src[i])
			else:
				break
			i = i + 1
