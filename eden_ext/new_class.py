import sublime, sublime_plugin

class CreateClassCommand(sublime_plugin.TextCommand):
	def run(self, edit,class_name):
		win = self.view.window()

		# create cpp file
		cpp_view = win.new_file()
		cpp_view.set_name(class_name+".cpp")
		cpp_view.set_syntax_file("Packages/C++/C++.tmLanguage")
		cpp_view.insert(edit,0,"#include \"" +class_name +".h\"\n")
		cpp_view.insert(edit,cpp_view.size(),class_name+"::"+class_name+"()\n{\n  \n}\n")
		cpp_view.insert(edit,cpp_view.size(),class_name+"::~"+class_name+"()\n{\n  \n}\n")

		# create h file
		h_view = win.new_file()
		h_view.set_name(class_name+".h")
		h_view.set_syntax_file("Packages/C++/C++.tmLanguage")
		h_view.insert(edit,0,"#ifndef _"+class_name+"_h_\n")
		h_view.insert(edit,h_view.size(),"#define _"+class_name+"_h_\n")
		h_view.insert(edit,h_view.size(),"class "+ class_name + "\n{\n")
		h_view.insert(edit,h_view.size(),"public:\n")
		h_view.insert(edit,h_view.size(),"  "+class_name+"();\n")
		h_view.insert(edit,h_view.size(),"  virtual ~"+class_name+"();\n")
		h_view.insert(edit,h_view.size(),"private:\n};\n")
		h_view.insert(edit,h_view.size(),"#endif")

class NewClassCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		input_view = self.view.window().show_input_panel("Input class name","",self.doit,None,None)

	def doit(self,user_input):
		self.view.run_command("create_class",{"class_name":user_input})
