def get_optimal (array, size, pivot, op1, op2):
	inc = dec = cost = 0
	for i in array:
		if (i < pivot):
			inc += (pivot - i);
		elif (i > pivot):
			dec += (i - pivot);

	if (dec > inc):
		return (float ('inf'));

	cost += dec * op1;
	inc -= dec;
	cost += (inc * op2);
	return (cost);

size, op1, op2 = [int (i) for i in input ().split ()];
array, optimal = [int (i) for i in input ().split ()], float ('inf');

for i in range (min (array), max (array) + 1):
	temp = get_optimal (array, size, i, op1, op2);
	optimal = temp if optimal > temp else optimal;
print (optimal);
