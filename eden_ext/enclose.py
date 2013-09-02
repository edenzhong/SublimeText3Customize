import sublime, sublime_plugin

class EncloseCommand(sublime_plugin.TextCommand):
	def run(self, edit,leading,ending):
		sel = self.view.sel()
		for region in sel:
			cont = self.view.substr(region)
			self.view.replace(edit,region,leading + cont + ending)

class EncloseByLineCommand(sublime_plugin.TextCommand):
	def run(self, edit,leading,ending):
		self.view.run_command("expand_selection",{"to": "line"})
		sel = self.view.sel()
		for region in sel:
			lns = self.view.substr(region).splitlines()
			output = ""
			if ( len(lns) > 0):
				for ln in lns:
					print(ln)
					output = output + leading + ln + ending + "\n"
			else:
				output = leading + ending
			self.view.replace(edit,region,output)
		
class InsDefineCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("enclose_by_line",{"leading":"#define ","ending":""})

class InsIncludeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("enclose_by_line",{"leading":"#include \"","ending":"\""})

class InsSysIncludeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("enclose_by_line",{"leading":"#include <","ending":">"})


class InsEncloseCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		input_view = self.view.window().show_input_panel("Input enclosure","",self.doit,None,None)

	def doit(self,user_input):
		if ( user_input ):
			self.view.run_command("enclose",{"leading":user_input,"ending":user_input})
		else:
			self.view.run_command("enclose",{"leading":"(","ending":")"})

class InsEncloseByLineCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		input_view = self.view.window().show_input_panel("Input enclosure","",self.doit,None,None)

	def doit(self,user_input):
		if ( user_input ):
			self.view.run_command("enclose_by_line",{"leading":user_input,"ending":user_input})
		else:
			self.view.run_command("enclose_by_line",{"leading":"(","ending":")"})
