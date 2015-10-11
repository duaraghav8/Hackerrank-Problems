def is_sorted (array, size):
	return (False if [1 for i in range (size - 1) if array [i + 1] - array [i] < 0] else True);

size, array = int (input ()), [int (i) for i in input ().split ()];
a, b = -1, size - 1;

for i in range (size - 1):
	if array [i + 1] < array [i]:
		a = i;
		break;
for i in range (a + 1, size):
	if (array [i] > array [a]):
		b = i - 1;
		break;

x = array.copy ();
x [a], x [b] = x [b], x [a];
if (is_sorted (x, size)): 
	print ('yes\nswap %d %d' % (a + 1, b + 1));
	quit ();

x [a], x [b] = x [b], x [a];
sub = x [a : b + 1];
sub.reverse ();
x = x [ : a] + sub + x [b + 1 : ];
if (is_sorted (x, size)): print ('yes\nreverse %d %d' % (a + 1, b + 1));
else: print ('no');
