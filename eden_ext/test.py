import sublime, sublime_plugin, re

class TestCommand(sublime_plugin.TextCommand):
	def fun(self):
		print("this is fun")

	def run(self, edit,s,syntax_type="cpp"):
		if ( "cpp" == syntax_type ):
			print("this is cpp type")
			s = re.sub("//[^\n$]*","",s)
		print(s)
