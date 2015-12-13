def sequence (dna1, dna2):
	prev = min (dna1 [0], dna2 [0]);
	for i in range (1, len (dna1)):
		print (prev);
		if (min (dna1 [i], dna2 [i]) >= prev):
			prev = min (dna1 [i], dna2 [i]);
		elif (max (dna1 [i], dna2 [i]) >= prev):
			prev = max (dna1 [i], dna2 [i]);
		else:
			return (False);
	return (True);

cases = [ (int (input ()), [int (i) for i in input ().split ()], [int (i) for i in input ().split ()]) for i in range (int (input ())) ];
for case in cases:
	print ('YES' if sequence (case [1], case [2]) else 'NO');
