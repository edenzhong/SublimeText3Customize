import sublime, sublime_plugin
from .str_plus import get_indent_of_string

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

def get_enclose_leading_ending(user_input):
	leading = "("
	ending = ")"

	if ( len(user_input) > 0):
		if ( "\"" == user_input[0] ):
			print("double q")
			if ( len(user_input) == 1):
				print("len=1")
				leading = "\""
				ending = "\""
			else:
				idx = user_input.find("\"",1)
				if ( idx < 0 ):
					print("q not found")
					leading = user_input
					ending = user_input
				else:
					print("q found")
					leading = user_input[1:idx]
					ending = user_input[idx+1:] # start from the ch next to "
		elif ( "'" == user_input[0] ):
			print("single q")
			if ( len(user_input) == 1):
				print("len=1")
				leading = "'"
				ending = "'"
			else:
				idx = user_input.find("'",1)
				if ( idx < 0 ):
					print("q not found")
					leading = user_input
					ending = user_input
				else:
					print("found q")
					leading = user_input[1:idx]
					ending = user_input[idx+1:] # start from the ch next to "
		else:
			print("no quote")
			idx = user_input.find(" ")
			if ( idx < 0 ):
				print("space not found")
				leading = user_input
				ending = user_input
			else:
				print("found space")
				leading = user_input[0:idx]
				ending = user_input[idx+1:] # start from the ch next to space
	return {"leading":leading,"ending":ending}

class InsEncloseCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		input_view = self.view.window().show_input_panel("Input enclosure","",self.doit,None,None)

	def doit(self,user_input):
		le = get_enclose_leading_ending(user_input)
		self.view.run_command("enclose",le)

class InsEncloseByLineCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		input_view = self.view.window().show_input_panel("Input enclosure","",self.doit,None,None)

	def doit(self,user_input):
		le = get_enclose_leading_ending(user_input)
		self.view.run_command("enclose_by_line",le)

class EncloseByIf0Command(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("expand_selection",{"to": "line"})
		sel = self.view.sel()
		for region in sel:
			self.view.insert(edit,region.end(),"#endif\n")
			self.view.insert(edit,region.begin(),"#if 0\n")
			
class IndentByCurlyBracketCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("expand_selection",{"to": "line"})
		sel = self.view.sel()
		for region in sel:
			# get indent of 1st line
			tmp_str = self.view.substr(region)
			indent = get_indent_of_string(tmp_str)
			self.view.insert(edit,region.end(),indent+"}\n") # to do: if this is the last line, a \n is missing
			self.view.insert(edit,region.begin(),indent+"{\n")
		self.view.run_command("indent")