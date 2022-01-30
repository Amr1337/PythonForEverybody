'''We will write a Python program to read through the lines of the file(has punctuation), break each line into a list of words, and then loop through
 each of the words in the line and count each word using a dictionary.'''
import string

fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print(f"File name {fname} is not found")
    exit()
d = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
print(d)