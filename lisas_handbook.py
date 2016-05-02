#Status: All Cases passed
#Since constraints were way too small, I didn't bother optimizing the algorithm & code

import math;

def special_problem_count (chapters, problem_count, prob_per_page):
	index = 0;
	special = 0;

	for ch in range (1, chapters+1):
		pages_reqd = math.ceil (problem_count [ch-1] / prob_per_page);
		fp, lp = 1, min (prob_per_page, problem_count [ch-1]);

		while (pages_reqd):
			index += 1;
			pages_reqd -= 1;
			if (index <= lp and index >= fp): special += 1;

			fp = lp+1;
			lp = min (lp + prob_per_page, problem_count [ch-1]);

	return special;

chapters, prob_per_page = [int (i) for i in input ().split ()];
problem_count = [int (i) for i in input ().split ()];

print (special_problem_count (chapters, problem_count, prob_per_page));
