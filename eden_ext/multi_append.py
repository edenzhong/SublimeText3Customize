import sublime, sublime_plugin

class InsPrefixCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# make an input plane to get user input
		input_view = self.view.window().show_input_panel("Input Prefix","",self.doit,None,None)
		pass
		# get the col number


		# expand selection to line
		# get selection
		# split the selection by line

		# if user input is \C
		# self.AppendByClipboard(edit)

	def doit(self,user_input):
		options = self.input_parser(user_input)
		if ( "show_help" in options.keys() ):
			self.help_info()
		else:
			sublime.message_dialog("hello")

	def help_info(self):
		help_msg = '''option start by a \\, a char, and a number. i.e. \\w2
A "\\\\" will be regarded as a single "\\", and the options parsing will be terminated.

Position options:
w(num): before x words
W(num): after x words
b(num): after x chars
c(num): before current chars

Context type options:
C: the content comes from clip board
d(step): the content comes from dec num,and increase step every line.
D(step): same as \\d, but decrease step every line.
x(step): same as \\d, but the number is hex format.
X(step): same as \\x, but decrease step every line.

Context:
e(str): the string to insert. if option is d,D,x,X, this is the start number. e must presented as the last option

Example:
\\w2\\d2\\e10
Insert context before 2nd word, the context is a dec number, starts from 10, and increase by 2.
'''
		sublime.message_dialog(help_msg)

	
	def input_parser(self,user_input):
		ops = []
		option_str = user_input
		while (len(option_str)>0):
			op_item = {}
			if ( option_str[0] == "\\"):
				if ( option_str[1] == "\\"):
					op_item.update({"option":"e"})
					op_item.update({"value":option_str[1:]})
					option_str = ""
				else:
					op_item.update({"option":option_str[1]})
					pos = option_str.find("\\",2)
					if ( pos > 0 ):
						op_item.update({"value":option_str[2:pos]})
						option_str = option_str[pos:]
					else:
						op_item.update({"value":option_str[2:]})
						option_str = ""
			else:
				op_item.update({"option":"e"})
				op_item.update({"value":option_str[:]})
				option_str = ""
			ops.append(op_item)

		options = {"potions_type":"b","position_value":0,"context_type":"constant","context":user_input}

		for op in ops:
			if ( op["option"] == "w" ) or ( op["option"] == "W" ) or ( op["option"] == "b" ) or ( op["option"] == "c" ):
				options["position_type"] = op["option"]
				options["position_value"] = op["value"]
			elif ( op["option"] == "C" ) or ( op["option"] == "d" ) or ( op["option"] == "D" ) or ( op["option"] == "x" ) or ( op["option"] == "X" ):
				options["context_type"] = op["option"]
				options["context_value"] = op["value"]
			elif ( op["option"] == "e" ):
				options["context"] = op["value"]
			else:
				options["show_help"] = 1

		return options



	