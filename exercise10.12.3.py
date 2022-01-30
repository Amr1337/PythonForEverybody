import string

fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("File is not found:",fname)
counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.lower()
    line = line.translate(line.maketrans('','',string.punctuation))
    line = line.translate((line.maketrans('','',string.whitespace)))
    line = line.translate((line.maketrans('','',string.digits)))
    words = line.split()
    for word in words:
        for char in word:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
lst = list()

for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst:
    print(
        val, key
    )