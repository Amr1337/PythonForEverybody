'''Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.
 Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
'''


def chop(mylist):
    del mylist[0]
    mylist.pop()

def middle(mylist):
    last = len(mylist)-1
    new_list = mylist[1:last]
    return new_list



mylist = [1,2,5,6,7,11]
print(chop(mylist))
print(mylist)
mylist1 = [1,2,51,62,7,111]
t = middle(mylist1)
print(t)