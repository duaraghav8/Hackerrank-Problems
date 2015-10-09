t = int (input ());
weights = sorted ([int (i) for i in input ().split ()]);
radii = [ [weights [0], weights [0] + 4] ];

#countingsort (weights, max (weights));
for i in range (t):
	belongs = False;
	for radius in radii:
		if (weights [i] <= radius [1] and weights [i] >= radius [0]):
			belongs = True;
			break;
	if (not belongs):
		radii.append ([weights [i], weights [i] + 4]);
print (len (radii));
