#Score: 54.10
from heapq import heapify, heappush, heappop;
def manhattan (a, b):
	return ( (abs (a [0] - b [0]) + abs (a [1] - b [1])) );

def next_move(posr, posc, dimx, dimy, grid):
	dirt_cells = [];
	for i in range (dimx):
		dirt_cells.extend ([(manhattan ( (posr, posc), (i, col) ), (i, col) ) for col, char in enumerate(grid [i]) if char == 'd']);

	heapify (dirt_cells);
	min_dist = heappop (dirt_cells);

	if (min_dist [1] [0] < posr):
		print ('UP');
	elif (min_dist [1] [0] > posr):
		print ('DOWN');
	elif (min_dist [1] [1] < posc):
		print ('LEFT');
	elif (min_dist [1] [1] > posc):
		print ('RIGHT');
	else:
		print ('CLEAN');
    
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()];
    dim = [int(i) for i in input().strip().split()];
    grid = [input ().strip () for i in range (dim [0])];
    next_move(pos[0], pos[1], dim[0], dim[1], grid)
