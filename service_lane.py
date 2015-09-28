t = int (input ().split () [1]);
array = [int (i) for i in input ().split ()];
cases = [];
for i in range (t):
	cases.append ([int (i) for i in input ().split ()]);
for case in cases:
	print (min (array [case [0] : case [1] + 1]));
