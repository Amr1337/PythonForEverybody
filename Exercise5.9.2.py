'''Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average'''
'''
mylist = [15,44,22,34,52,192,11]
count = 1
max = None
min = None
for itervar in mylist:
    print(f"Number #{count} from list: ",itervar)
    count+=1
    if max == None or itervar > max:
        max = itervar
    elif min == None or itervar < min:
        min = itervar
print(f"Max number in list: {max}, Min number in list: {min}")'''

mylist1 =[]
min = None
max = None
while True:
    number = input("Enter Number: ")
    if number == "done":
        break
    try:
        mylist1.append(int(number))
    except:
        print("print invalid")


    for itervar in mylist1:
        if max == None or itervar > max:
            max = itervar
        elif min == None or itervar < min:
            min = itervar

print(mylist1)
print(min)
print(max)