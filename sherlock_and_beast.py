def get_num (n):
	k = n;
	while (not k % 3 == 0):
		k -= 5;
		if (k < 0):
			return ('-1');
	result = ('5' * k) + ('3' * (n - k));
	return (result);

t = int (input ());
cases = [];

for i in range (t):
	cases.append (int (input ()));
for case in cases:
	print (get_num (case));
