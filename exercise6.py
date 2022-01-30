'''Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay
 which takes two parameters (hours and rate).'''

def compute_pay(hours, rate):
    if hours > 40:
        overtime = hours - 40
        pay = (40 * rate) + (overtime * (1.5 * rate))
    else:
        pay = hours * rate
    return pay

try:
    hours = int(input("Enter Hours: "))
    rate = int(input("Enter rate: "))
except:
    print("Please enter a numeric!")
print(compute_pay(hours, rate))
