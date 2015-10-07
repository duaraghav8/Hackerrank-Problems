def getChocCount (money, cost, discount):
	wrappers = chocCount = money // cost;
	while (wrappers >= discount):
		extraChocs = wrappers // discount
		chocCount += extraChocs;
		wrappers %= discount;
		wrappers += extraChocs
	return (chocCount);

t = int (input ());
cases = [];

for i in range (t):
	cases.append ([int (i) for i in input ().split ()]);

for case in cases:
	print (getChocCount (case [0], case [1], case [2]));
