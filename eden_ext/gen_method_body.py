import sublime, sublime_plugin,re
from .str_plus import get_file_name_from_full,get_indent_of_string,clear_cpp_comment

class GenMethodBodyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		bodies = ""
		self.view.run_command("expand_selection",{"to": "line"})
		# get class name
		# work around: get file name as the class name
		filename = self.view.file_name()
		if ( filename ):
			classname = get_file_name_from_full(filename)
		else:
			filename = self.view.name()
			if ( filename ):
				classname = get_file_name_from_full(filename)
			else:
				sublime.message_dialog("Could not get the class name.")
				return

		sel = self.view.sel()
		for region in sel:
			lns = self.view.substr(region).splitlines()
			if ( len(lns) > 0):
				for ln in lns:
					ln = clear_cpp_comment(ln)
					ln = re.sub("[\t ]virtual[\t ]"," ",ln) # the keyword virtual is no need to present
					# get method name: the word before "("
					match = re.search("~?\w+\(",ln)
					if(match):
						pos = match.start(0)
						
						indent = get_indent_of_string(ln)
						body = ln[len(indent):pos] + classname + "::"

						endpos = ln.find(";")
						if ( endpos > pos):
							body += ln[pos:endpos]
						else:
							body += ln[pos:]
						body += "\n{\n\t\n}\n"
						bodies += body
		sublime.set_clipboard(bodies)