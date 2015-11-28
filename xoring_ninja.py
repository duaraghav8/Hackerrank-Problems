def xor_sum (n, nums):
	mask = 0;
	for i in nums: mask = (mask | i) % (10**9 + 7);
	mask *= (2 ** (n - 1));
	return (mask % (10**9 + 7));

cases = [ (int (input ()), [int (i) for i in input ().split ()]) for j in range (int (input ())) ];
for case in cases:
	print (xor_sum (case [0], case [1]));
