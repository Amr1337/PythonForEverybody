'''Exercise 2: Write a program to look for lines of the form:
New Revision: 39772
Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and
print out the average as an integer.
Enter file:mbox.txt
38549
Enter file:mbox-short.txt
39756
'''

import re
fname = input("Enter file:")

try:
    fhand = open(fname)
    # file must be in the same directory or you should navigate to it while
    # entering the input
except:
    print("invalid file name:", fname)
count =0
sum_x = 0
for line in fhand:
    line = line.rstrip()
    x = re.findall("^New Revision: ([0-9.]+)", line)
    if len(x) > 0:
        count+=1
        #print(x)
        sum_x+= int(x[0])
#print(sum_x)
#print(count)
print(int(sum_x/count))