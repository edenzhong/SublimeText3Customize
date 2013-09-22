import sublime, sublime_plugin, re
from .str_plus import clear_cpp_comment

class GenAccMemVarCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("expand_selection",{"to": "line"})
		methods = ""
		sel = self.view.sel()
		for region in sel:
			lns = self.view.substr(region).splitlines()
			if ( len(lns) > 0):
				for ln in lns:
					ln = clear_cpp_comment(ln)
					match = re.findall("(\w+)",ln)
					if (match and len(match)>1):
						# get last word as var name. 
						varname = match[-1]
						if ( re.match("[Mm]_",varname)):
							pure_var_name = varname[2:]
						elif( re.match("_",varname)):
							pure_var_name = varname[1:]
						else:
							pure_var_name = varname

						# get var type
						typename = ""
						for i in range(len(match)-1) :
							typename += match[i] + " "

						# gen acc method
						method = "inline void set_" + pure_var_name + "(" + typename + " val){"+varname+"=val;}\n"
						method += "inline "+typename+"get_"+pure_var_name+"()const{return "+varname+";}\n"
						methods += method
		sublime.set_clipboard(methods)


