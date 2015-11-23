#https://www.hackerrank.com/contests/w18/challenges/target
#Overall Time Complexity: O (Nlog(N))

from math import sqrt;
from heapq import heapify, heappop, heappush;

def radius (x, y):
	return (sqrt ( (x ** 2) + (y ** 2) ));

def get_net_score (coords, radii):
	radii = radii + [-float ('inf')];
	point_radii = [-radius (xy [0], xy [1]) for xy in coords] + [float ('inf')];
	score, circle, i = 0, 0, 0;

	heapify (point_radii);
	max_radius = -heappop (point_radii);

	while (point_radii):
		if (max_radius <= radii [i]):
			circle += 1;
			i += 1;
		else:
			score += circle;
			max_radius = -heappop (point_radii);

	return (score);

k, n = [int (i) for i in input ().split ()];
radii = [int (i) for i in input ().split ()];
coords = [ [int (i) for i in input ().split ()] for j in range (n) ];

print (get_net_score (coords, radii));
