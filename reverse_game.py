#Score: 30.0 All Test Cases Passed. Sorry for the bad code though. Its 12:30 am and I'm too sleepy to give a poop about code quality
t = int (input ());
cases = [];

for i in range (t):
	cases.append ([int (i) for i in input ().split ()]);
for case in cases:
	if (case [0] // 2 < case [1]):
		pos = 0;
		start = case [0] - 1;
		while (not start == case [1]):
			pos += 2;
			start -= 1;

	elif (case [0] // 2 > case [1]):
		pos = 1;
		start = 0
		while (not start == case [1]):
			pos += 2;
			start += 1;
	else:
		pos = case [0] - 1;
	print (pos);
