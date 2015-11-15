def get_p (a_count, size, draws):
	if (draws == 0):
		if (a_count == a_count_original):
			return (0);
		return (1);

	a_found = (a_count / size) * get_p (a_count - 1, size - 1, draws - 1);
	a_nfound = ( (size - a_count) / size) * get_p (a_count, size - 1, draws - 1);

	return (a_found + a_nfound);

size, string, draws = int (input ()), [i for i in input ().split ()], int (input ());
a_count_original = string.count ('a');
print ( round (get_p (a_count_original, size, draws), 4) );
