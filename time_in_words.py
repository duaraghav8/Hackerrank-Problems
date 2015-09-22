#I'm trying to design a better solution (thanks to cucurbita for suggestions)
def split_minutes (mins):
	digits = [];
	while (mins):
		digits.insert (0, (mins % 10) * ( 10 ** len (digits) ));
		mins //= 10;
	return (digits);

table_en = {
     0: 'o\' clock',
     1: 'one',
     2: 'two',
     3: 'three',
     4: 'four',
     5: 'five',
     6: 'six',
     7: 'seven',
     8: 'eight',
     9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'quarter',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'half',
};

TO = 'to';
PAST = 'past';
SPACE = ' ';

def get_time_sentence (hour, minutes):
	time_string = '';

	if (minutes == 0):
		time_string += table_en [hour] + SPACE + table_en [minutes];
	elif (minutes == 30):
		time_string += table_en [minutes] + SPACE + PAST + SPACE + table_en [hour];
	elif (minutes == 15):
		time_string += table_en [minutes] + SPACE + PAST + SPACE + table_en [hour];
	elif (minutes == 45):
		time_string += table_en [minutes - 30] + SPACE + TO + SPACE + table_en [ (1 if hour == 12 else hour + 1) ];
	else:
		CONNECTOR = PAST;
		if (minutes > 30):
			minutes = 60 % minutes;
			hour = (1 if hour == 12 else hour + 1);
			CONNECTOR = TO;

		if (minutes > 20):
			mins = split_minutes (minutes);
		else:
			mins = [minutes];

		time_string += ' '.join ([table_en [digit] for digit in mins]) + SPACE + ('minute' if minutes == 1 else 'minutes') + SPACE + CONNECTOR + SPACE + table_en [hour];

	return (time_string);

if (__name__) == '__main__':
	hour = int (input ());
	minutes = int (input ());
	print (get_time_sentence (hour, minutes));
