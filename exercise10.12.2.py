'''This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.
python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1

'''

fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("File name is not found:", fname)
counts = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        time_val = words[5].split(':')
        hour = time_val[0]
        if hour not in counts:
            counts[hour] = 1
        else:
            counts[hour] += 1
# print(counts)
hours_list = list()
for key, val in list(counts.items()):
    hours_list.append((key, val))

hours_list.sort()

for key, val in hours_list:
    print(key, val)