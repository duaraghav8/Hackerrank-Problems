#O (N) solution all cases passed

def steady_substr (gene_len, gene):
	frequencies = {'A': 0, 'T': 0, 'C': 0, 'G': 0};
	min_len = float ('inf');
	chars_needed = {};

	for nt in gene: frequencies [nt] += 1;		#nt = nucleotide
	for i in frequencies:
		if (frequencies [i] > gene_len // 4): chars_needed [i] = frequencies [i] - (gene_len // 4);

	if (not chars_needed):
		return 0;

	start = 0;
	for end in range (gene_len):
		if gene [end] in chars_needed:
			chars_needed [gene [end]] -= 1;

		if (all (i <= 0 for i in chars_needed.values ())):
			min_len = min (min_len, end - start + 1);
			while (start <= end):
				if (gene [start] in chars_needed): chars_needed [gene [start]] += 1;

				if (not all (i <= 0 for i in chars_needed.values ())):
					chars_needed [gene [start]] -= 1;
					break;
				else:
					start += 1;
					min_len = min (min_len, end - start + 1);

	return min_len;

print (steady_substr (int (input ()), input ()));
