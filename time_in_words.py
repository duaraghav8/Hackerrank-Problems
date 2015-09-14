def get_time_sentence (hour, mins):
	singles = [
		'sentinal', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'senventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine'
	];
	
	min_word = [
		'minute', 'minutes'
	];
	zero_min = "o' clock";
	past = 'past';
	to = 'to';
	special = [
		'half', 'quarter'
	];
	final_string = '';
	space = ' ';

	if (mins == 0):
		final_string += singles [hour] + space + zero_min;
	else:
		if (mins == 15):
			final_string += special [1] + space + past + space + singles [hour];
		elif (mins == 30):
			final_string += special [0] + space + past + space + singles [hour];
		elif (mins == 45):
			if (hour == 12):
				final_string += special [1] + space + to + space + singles [1];
			else:
				final_string += special [1] + space + to + space + singles [(hour + 1)];
		else:
			if (mins < 30):
				if (mins == 1):
					final_string += singles [mins] + space + min_word [0] + space + past + space + singles [hour];
				else:
					final_string += singles [mins] + space + min_word [1] + space + past + space + singles [hour];
			else:
				mins = 60 - mins;
				final_string += singles [mins] + space + min_word [1] + space + to + space + singles [(hour + 1)];

	return (final_string);

if (__name__) == '__main__':
	hour = int (input ());
	minutes = int (input ());

	print (get_time_sentence (hour, minutes));
