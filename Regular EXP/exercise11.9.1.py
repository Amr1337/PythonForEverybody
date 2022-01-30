'''Exercise 1: Write a simple program to simulate the operation of the
grep command on Unix. Ask the user to enter a regular expression and
count the number of lines that matched the regular expression'''
import re

usr_input = input("Enter a regular expression: ")
count = 0
fhand = open("../mbox.txt")
for line in fhand:
    line = line.rstrip()
    x = re.findall(usr_input, line)
    if len(x) > 0:
        count += 1
print(f"mbot.txt had {count} lines that matched {usr_input}")