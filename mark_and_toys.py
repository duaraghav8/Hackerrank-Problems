from heapq import heapify, heappush, heappop;

toys, money = [int(i) for i in input ().split ()];
costs = [int(i) for i in input ().split ()];
counter = -1;

heapify (costs);
while (money > 0):
	money -= heappop (costs);
	counter += 1;

print (counter);
