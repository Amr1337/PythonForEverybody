'''Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line.
Count the number of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most commits.
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195'''



fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("File not found: ",fname)
counts = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
       words = line.split()
       mail_addr = words[1]
       if mail_addr not in counts:
           counts[mail_addr] = 1
       else:
           counts[mail_addr] += 1
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:1]:
    print(val, key)
