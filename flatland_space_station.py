#########################################################################
#This got only 1 TLE and one Runtime Error, which resulted in 21.5 / 25
#Time complexity is O (MN), M = no. of space stations and N = no. of cities
#I am missing some special case, because of which the Runtime Err occured.
#Possible places where RE could happen in this code seem to be any of the for statements or the max () statement. Can't think :/
#########################################################################

cityCount, station_count = [int (i) for i in input ().split ()];
stationIndices = [int (i) for i in input ().split ()];

bestDists = {i : float ('inf') for i in range (cityCount)};
for station in stationIndices:
	for i in range (cityCount):
		if (abs (i - station) < bestDists [i]):
			bestDists [i] = abs (i - station);

print (max (bestDists.values ()));
