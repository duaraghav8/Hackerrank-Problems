#Score: 40.0 / 50.0 (Failed Test Case #5)
class Case:
	def __init__ (self):
		self.dim = [int (i) for i in input ().split ()];
		self.grid = '';

		for i in range (0, self.dim [0]):
			self.grid += input ();

		self.patternDim = [int (i) for i in input ().split ()];
		self.pattern = [];

		for i in range (0, self.patternDim [0]):
			self.pattern.append (input ());

	def holds (self):
		counter = 0;
		positions = [];
		differences = [];

		for line in self.pattern:
			if (len (positions) == 0):
				positions.append (self.grid.find (line));
			else:
				positions.append (self.grid.find (line, positions [counter] + len (line)));

		if (self.patternDim [0] == 2):
			#a 2x2 matrix is a special case, where the difference list only holds 1 value, thus always classifying the case as YES
			linePosA = positions [0] % self.dim [1];
			linePosB = positions [1] % self.dim [1];
			rowA = positions [0] // self.dim [1];
			rowB = positions [1] // self.dim [1];

			return (True if linePosA == linePosB and rowA + 1 == rowB else False);

		for i in range (0, len (positions) - 1):
			differences.append (positions [i + 1] - positions [i]);
		
		return (True if len (set (differences)) == 1 and positions.count (-1) == 0 else False);

if (__name__) == '__main__':
	t = int (input ());
	cases = [];
	for i in range (0, t):
		case = Case ();
		cases.append (case);

	for case in cases:
		print ('YES' if case.holds () else 'NO');
