import math;

t = int (input ());
cases = [];

for i in range (t):
	cases.append ([int (i) for i in input ().strip ().split ()]);
for case in cases:
	lower = math.ceil (math.sqrt (case [0]));
	upper = math.floor (math.sqrt (case [1]));
	print (upper - lower + 1);
