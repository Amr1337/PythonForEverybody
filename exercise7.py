'''Exercise 7: Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.'''


def computegrade(score):
    if score >= 0.9:
        grade = "A"
    elif 0.9 >= score >= 0.8:
        grade = "B"
    elif 0.8 >= score >= 0.7:
        grade = "C"
    elif 0.7 >= score >= 0.6:
        grade = "D"
    elif score < 0.6:
        grade = "F"
    else:
        "Something is not right!"
    return grade

try:
    score = float(input("Enter score: "))
    print(computegrade(score))
except:
    print("Something went wrong")


