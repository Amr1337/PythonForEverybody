'''Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines
that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print
out the contents of your dictionary (order does not matter).
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
'''

fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("File name: "+fname+" can't be found")
ddays = dict()
week_day = ""
for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        week_day = words[2]
        if week_day not in ddays:
            ddays[week_day] = 1
        else:
            ddays[week_day] += 1
print(ddays)
