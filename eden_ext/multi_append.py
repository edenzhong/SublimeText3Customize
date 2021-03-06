import sublime, sublime_plugin, re, string
from .str_plus import (str_to_num,reverse_chars)

class SetEditTextCommand(sublime_plugin.TextCommand):
	def run(self,edit,start,end,str_to_insert):
		r = sublime.Region(start,end)
		self.view.replace(edit,r,str_to_insert)


class InsPreSurfixCommand(sublime_plugin.TextCommand):
	word_pattern = re.compile("[\w]+")
	new_line = '\n'

	def run(self, edit):
		# make an input plane to get user input
		input_view = self.view.window().show_input_panel("Input options and context","",self.doit,None,None)
		
	def doit(self,user_input):
		options = self.input_parser(user_input)
		if ( "show_help" in options.keys() ):
			self.help_info()
		else:
			self.view.run_command("expand_selection",{"to": "line"})
			rs = self.view.sel()
			for region in rs:
				s = self.view.substr(region)
				sl = s.splitlines()
				
				cont = ""
				#for l in sl:
				for idx in range(len(sl)):
					l = sl[idx]
					ins_pos = self.get_insert_pos(l,options["position_type"],options["position_value"])
					s = l[0:ins_pos] + str(self.get_insert_context(idx,options["context_type"],options["context_value"],options["context"])) + l[ins_pos:]
					cont = cont + s
					if ( idx < len(sl) - 1):
						cont = cont + self.new_line

				self.view.run_command("set_edit_text",{"start":region.begin(),"end":region.end(),"str_to_insert":cont})

	def get_insert_pos(self,original_str,pos_type,pos_val):
		raise Exception("pure: get_insert_pos")

	context_2b_insert = []
	def prepare_insert_context(self,context_type,context_value):
		'''prepare the insert context for \\C option, context comes from clipboard'''
		if ( context_type == "C"):
			clip_cont = sublime.get_clipboard()
			self.context_2b_insert = clip_cont.splitlines()
			
	def get_insert_context(self,idx,context_type,context_value,context):
		if ( context_type == "C"):
			if ( 0 == idx ):
				self.prepare_insert_context(context_type,context_value)
			if ( idx < len(self.context_2b_insert)):
				return self.context_2b_insert[idx]
			else:
				return ""
		elif (context_type == "d"):
			val = str_to_num(context)
			return (val + ( str_to_num(context_value) * idx ))
		elif (context_type == "D"):
			val = str_to_num(context)
			return (val - (str_to_num(context_value) * idx ))
		elif (context_type == "x"):
			val = str_to_num(context)
			return hex(val + (str_to_num(context_value) * idx ))
		elif (context_type == "X"):
			val = str_to_num(context)
			return hex(val - (str_to_num(context_value) * idx ))
		else: # constant
			return context


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

		options = {"position_type":"b","position_value":0,"context_type":"constant","context_value":"","context":user_input}

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

	def help_info(self):
		raise Exception("pure:help_info")

class InsPrefixCommand(InsPreSurfixCommand):
	def get_insert_pos(self,original_str,pos_type,pos_val):
		val = str_to_num(pos_val)

		if ( pos_type == "w") or ( pos_type == "W"):
			it = self.word_pattern.finditer(original_str)
			idx = 0
			for m in it:
				idx = idx + 1
				if ( idx < val):
					continue
				else:
					if ( pos_type == "w"):
						return m.start()
					else:
						return m.end()
			# if can not find enough word in the original string, return the end pos.
			return len(original_str)
		elif ( pos_type == "b"):
			return val
		else:
			return 0

	def help_info(self):
		help_msg = '''option start by a \\, a char, and a number. i.e. \\w2\n'''\
		'''A "\\\\" will be regarded as a single "\\", and the options parsing will be terminated.\n'''\
		'''\n'''\
		'''Position options:\n'''\
		'''w(num): before x words\n'''\
		'''W(num): after x words\n'''\
		'''b(num): after x chars\n'''\
		'''c(num): before current char (not implement)\n'''\
		'''\n'''\
		'''Context type options:\n'''\
		'''C: the content comes from clip board\n'''\
		'''d(step): the content comes from dec num,and increase step every line.\n'''\
		'''D(step): same as \\d, but decrease step every line.\n'''\
		'''x(step): same as \\d, but the number is hex format.\n'''\
		'''X(step): same as \\x, but decrease step every line.\n'''\
		'''if none of the above types is specified, a default constant type is applied.\n'''\
		'''\n'''\
		'''Context:\n'''\
		'''e(str): the string to insert. if option is d,D,x,X, this is the start number. e must presented as the last option\n'''\
		'''\n'''\
		'''Example:\n'''\
		'''\\w2\\d2\\e10\n'''\
		'''Insert context before 2nd word, the context is a dec number, starts from 10, and increase by 2.'''

		sublime.message_dialog(help_msg)

class InsSurfixCommand(InsPreSurfixCommand):
	def get_insert_pos(self,original_str,pos_type,pos_val):
		slen = len(original_str)
		val = str_to_num(pos_val)

		if ( pos_type == "w") or ( pos_type == "W"):
			reverse_str = reverse_chars(original_str)
			it = self.word_pattern.finditer(reverse_str)
			idx = 0
			for m in it:
				idx = idx + 1
				if ( idx < val):
					continue
				else:
					if ( pos_type == "w"):
						return slen - m.start()
					else:
						return slen - m.end()
			# if can not find enough word in the original string, return the end pos.
			return 0
		elif ( pos_type == "b"):
			if ( slen > val):
				return slen - val
			else:
				return 0
		else:
			return slen

	def help_info(self):
		help_msg = '''option start by a \\, a char, and a number. i.e. \\w2\n'''\
		'''A "\\\\" will be regarded as a single "\\", and the options parsing will be terminated.\n'''\
		'''\n'''\
		'''Position options:\n'''\
		'''w(num): after x words\n'''\
		'''W(num): before x words\n'''\
		'''b(num): before x chars\n'''\
		'''c(num): after current char (not implement)\n'''\
		'''\n'''\
		'''Context type options:\n'''\
		'''C: the content comes from clip board\n'''\
		'''d(step): the content comes from dec num,and increase step every line.\n'''\
		'''D(step): same as \\d, but decrease step every line.\n'''\
		'''x(step): same as \\d, but the number is hex format.\n'''\
		'''X(step): same as \\x, but decrease step every line.\n'''\
		'''if none of the above types is specified, a default constant type is applied.\n'''\
		'''\n'''\
		'''Context:\n'''\
		'''e(str): the string to insert. if option is d,D,x,X, this is the start number. e must presented as the last option\n'''\
		'''\n'''\
		'''Example:\n'''\
		'''\\w2\\d2\\e10\n'''\
		'''Insert context before 2nd word, the context is a dec number, starts from 10, and increase by 2.'''

		sublime.message_dialog(help_msg)