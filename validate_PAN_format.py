import re;

t = int (input ());
pans = [];
matchObject = re.compile ('[A-Z]{5}[0-9]{4}[A-Z]');

for i in range (t):
	pans.append (input ());
for result in ['YES' if matchObject.match (pan) else 'NO' for pan in pans]:
	print (result);
