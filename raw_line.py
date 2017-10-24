

class RawLineChanger(object):
	def __init__(self, rawfilepath=None):
		self.rawfilepath = rawfilepath

	@staticmethod
	def is_change_line(line):
		pass

	@staticmethod
	def change_line(line):
		pass


class RawLineAdder(object):
	def __init__(self, rawline, type):
		"""
		Information to add a line to a RAW file.

		Args:
			rawline: string, full contents of line
			type: 'Line', 'Transformer', etc. -- type of object to be added.
		 		  Needed to determine what section to insert.
		"""
		self.line = rawline
		self.type = type

