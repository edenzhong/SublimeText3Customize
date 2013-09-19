import sublime, sublime_plugin
from .str_plus import get_file_name_from_full

class CopyFileNameToClipboardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		name = get_file_name_from_full(self.view.file_name())
		sublime.set_clipboard(name)

class InsFileNameCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		name = get_file_name_from_full(self.view.file_name())
		sel = self.view.sel()
		for region in sel:
			self.view.replace(edit,region,name)