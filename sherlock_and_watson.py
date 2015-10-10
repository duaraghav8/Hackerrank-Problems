#this simple mathematical trick would do the job
size, rotation, q = [int (i) for i in input ().split ()];
array, queries = [int (i) for i in input ().split ()], [int (input ()) for i in range (q)];

for query in queries:
	print (array [query - rotation]);

#but if you really want to change the array (just to simulate the entire thing
'''
size, rotation, q = [int (i) for i in input ().split ()];
array, queries = [int (i) for i in input ().split ()], [int (input ()) for i in range (q)];

while (rotation > 0):
	array.insert (0, array.pop (-1));
	rotation -= 1;

for query in queries:
	print (array [query]);
'''

#both programs will pass the cases, though the first one takes a max of 0.07s and the second takes a max of almost 8s
