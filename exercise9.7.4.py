'''Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and
the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find
 who has the most messages and print how many messages the person has.
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
 '''
fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("File name couldn't be found: ", fname)
d = dict()
mail_handle = ""
for line in fhand:
    line.rstrip()
    if line.startswith("From "):
        words = line.split()
        # print(words)
        mail_handle = words[1]
        if mail_handle not in d:
            d[mail_handle] = 1
        else:
            d[mail_handle] += 1
largest = None
for item in d.values():
    if item > largest:
        largest = item
for key in d:
    if d[key] == largest:
        print(key, largest)