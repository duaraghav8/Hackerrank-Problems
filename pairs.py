size, diff = [int (i) for i in input ().split ()];
counter, numbers = 0, {int (i) : 1 for i in input ().split ()};

for num in numbers:
	try:
		t = numbers [num + diff];
	except Exception as e:
		continue;
	counter += 1;
print (counter);
