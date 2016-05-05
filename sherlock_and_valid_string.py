#I got 3 cases wrong until I checked Discussion and realized that Quesion is not formed properly.
#Now all cases passed in O (N) time

def valid_possible (string):
	freq = {i: string.count (i) for i in set (string)};
	fvalues = list (freq.values ());
	frequencies = set (fvalues);

	if (len (frequencies) == 1): return True;
	elif (len (frequencies) > 2): return False;

	a, b = frequencies.pop (), frequencies.pop ();

	if (fvalues.count (a) == 1 or fvalues.count (b) == 1): return True;
	return False;


print ('YES' if valid_possible (input ()) else 'NO');
