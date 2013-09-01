import sublime, sublime_plugin, re

class InsIfNotDefHeadCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		name = self.view.file_name()
		if (name):
			match_obj = re.search("[^/]+$",name)
			if ( match_obj ):
				name = match_obj.group(0).lower()
				name = re.sub("\.","_",name)
				head = "#ifndef _" + name + "_\n#define _" + name + "_\n"
				self.view.insert(edit,0,head)
				self.view.insert(edit,self.view.size(),"\n#endif")
				return
			
		head = "#ifndef __\n#define __\n"
		self.view.insert(edit,0,head)
		self.view.insert(edit,self.view.size(),"\n#endif")
		s = self.view.sel()
		s.clear()
		region = sublime.Region(9,9)
		s.add(region)
		region = sublime.Region(20,20)
		s.add(region)