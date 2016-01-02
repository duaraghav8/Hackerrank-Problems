#Was previously causing TLE for TC #10 & #11, but thanks to @AbhishekVermaIIT for suggesting an optimality trick, did the job.

def grand_total (string):
	total, mult = 0, 1;
	for i in range (len (string), 0, -1):
		total += int (string [i - 1]) * mult * i;
		mult = ( (mult * 10) + 1 ) % ( (10**9) + 7);

	return (total);		

print (grand_total (input ()) % ( (10 ** 9) + 7));
