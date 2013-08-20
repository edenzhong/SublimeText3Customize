import sublime, sublime_plugin, re

class TestCommand(sublime_plugin.TextCommand):
	def fun(self):
		print("this is fun")

	def run(self, edit):
		m = re.finditer("[\S]+"," hello eden")
		for ii in m:
			print(ii.span())
