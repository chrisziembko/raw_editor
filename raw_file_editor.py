

class RawFileEditor(object):
	def __init__(self, old_filepath, new_filepath=None, version=None,
				 raw_line_changers=[], raw_line_adders=[]):
		self.old_filepath = old_filepath
		self.new_filepath = new_filepath
		self.raw_line_changers = raw_line_changers
		self.raw_line_adders = raw_line_adders
		self.old_contents = self.read_file(self.old_filepath)
	
	@staticmethod
	def read_file(filepath):
		contents = []
		with open(filepath, 'r') as openfile:
			for line in openfile:
				contents.append(line)
			openfile.close()
		return contents

	@staticmethod
	def write_file(contents, filepath):
		with open(filepath, 'w') as openfile:
			for line in contents:
				openfile.write(line)
			openfile.close()

	@staticmethod
	def edit_contents(contents, raw_line_changers, raw_line_adders):
		pass

