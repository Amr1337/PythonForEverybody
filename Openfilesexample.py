fname = input("Enter file name: ")
count =0
try:
    fhand = open(fname)
except:
    print("File can't be opened: ",fname)
    exit()
for line in fhand:
    line = line.rstrip()
    if line.startswith("Subject"):
        count +=1
print("There were ",count,"Subjects in",fname)