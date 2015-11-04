from math import sqrt, floor;

def encrypt (text):
	lo, final = floor (sqrt (len (text))), '';
	rows, cols = lo, lo if (lo ** 2) >= len (text) else lo + 1;

	for j in range (1, cols + 1):
		for i in range (j, len (text) + 1, cols):
			final += text [i - 1];
		final += ' ';

	return (final);

print (encrypt (input()));
