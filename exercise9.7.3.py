'''Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from
each email address, and print the dictionary.'''
'''output:
Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
'''

fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("File name couldn't be found: ",fname)
d = dict()
mail_handle = ""
for line in fhand:
    line.rstrip()
    if line.startswith("From "):
        words = line.split()
        #print(words)
        mail_handle = words[1]
        if mail_handle not in d:
            d[mail_handle] = 1
        else:
            d[mail_handle] += 1
print(d)