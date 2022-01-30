'''Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, printout the contents of your dictionary.
python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}'''

fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except:
    print("file name could not be found: ", fname)
d = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        mail_address = words[1]
        mail_address = mail_address.split('@')
        mail_domain = mail_address[1]
        if mail_domain not in d:
            d[mail_domain] = 1
        else:
            d[mail_domain] += 1
print(d)