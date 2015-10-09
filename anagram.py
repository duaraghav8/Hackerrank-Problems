t = int (input ());
strings = [input () for i in range (t)];

for string in strings:
	if (len (string) % 2 == 1):
		print ('-1');
		continue;

	counter, a, b = 0, string [ : len (string) // 2], string [ len (string) // 2 : ];
	for i in range (ord ('a'), ord ('z') + 1):
		counter += abs (b.count (chr (i)) - a.count (chr (i)));
	print (counter // 2);
