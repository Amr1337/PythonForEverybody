'''Exercise 2: Write a program to prompt for a file name, and then read
through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence
values from these lines. When you reach the end of the file, print out
the average spam confidence.
Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
Test your file on the mbox.txt and mbox-short.txt files.
'''
fname = input("Enter file name: ")
count= 0
spam_total_value = 0
try:
    fhand = open(fname)
except:
    print("file name not found ",fname)
for line in fhand:
    line = line.rstrip()
    if line.find("X-DSPAM-Confidence: ") == -1:
        continue
    count += 1
    spam_total_value += float(line[20:])
avg_spam = spam_total_value /count
print("Average spam confidence: ",avg_spam)















