import random;

def bribe_count_init (n, final_state):
	bribe_count = 0;
	numbers, positions = [i+1 for i in range (n)], [i for i in range (n)];

	for i in range (n):
		item_index = numbers.index (final_state [i]);

		if (i < item_index):
			if (item_index - i > 2):
				return ('Too chaotic');

			numbers [item_index], numbers [item_index-1] = numbers [item_index-1], numbers [item_index];
			if (item_index - i == 2):
				numbers [item_index-1], numbers [item_index-2] = numbers [item_index-2], numbers [item_index-1];

			bribe_count += item_index - i;

	return (bribe_count);

if (__name__ == '__main__'):
	cases = [(int (input ()), [int (j) for j in input ().split ()]) for i in range (int (input ()))];
	for case in cases: print (bribe_count_init (case [0], case [1]));
