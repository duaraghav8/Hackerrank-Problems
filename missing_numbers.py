#Score: 23.1, Test Case #4 Timeout (10s)
if (__name__) == '__main__':
	aLen = int (input ());
	listA = [int (i) for i in input ().split ()];
	bLen = int (input ());
	listB = [int (i) for i in input ().split ()];

	for item in listA:
		listB.pop (listB.index (item));
	result = list (set (listB));
	result.sort ();
	result = [str (i) + ' ' for i in result];
	result = ''.join (result);
	result = result [ : -1];

	print (result);
