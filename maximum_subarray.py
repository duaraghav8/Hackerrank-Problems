t = int (input ());
arrays = [];

for i in range (0, t):
	irrelevant = input ();
	arrays.append ([int (i) for i in input ().split ()]);

for array in arrays:
	max_so_far = 0;
	max_ending_here = 0;
	non_cont_sum = 0;

	for i in range (0, len (array)):
		if (array [i] > 0):
			non_cont_sum += array [i];
	
		max_ending_here += array [i];
		if (max_ending_here < 0):
			max_ending_here = 0;
		elif (max_ending_here > max_so_far):
			max_so_far = max_ending_here;

	max_so_far += max(array) if (max_so_far == 0) else 0;
	non_cont_sum += max (array) if non_cont_sum == 0 else 0;
	print (max_so_far, non_cont_sum);
