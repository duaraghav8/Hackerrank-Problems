time = input ();
meridian = time [-2];
time = time [ : -2];
hour = int (time [0 : -2].split (':') [0]);

if (meridian == 'P'):
        hour = str (hour + 12 if not hour == 12 else 12);
else:
        hour = '00' if hour == 12 else ('0' + str (hour) if hour < 10 else str (hour));
time = str (hour) + time [2 : ];
print(time);
