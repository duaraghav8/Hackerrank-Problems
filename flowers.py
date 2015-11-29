from heapq import heapify, heappop, heappush;

def min_cost (n, k, costs):
	people = [ (0, i + 1) for i in range (k) ];
	costs = [-i for i in costs];
	amount = 0;

	heapify (people);
	heapify (costs);

	while (costs):
		bought, person = heappop (people);
		cost = -heappop (costs);

		amount += (bought + 1) * cost;
		heappush (people, (bought + 1, person));

	return (amount);

n, k = [int (i) for i in input ().split ()];
costs = [int (i) for i in input ().split ()];
print (min_cost (n, k, costs));
