#Challenge 1-2-2¶
'''
Write a program to accept numbers until the user enters: 0

The program should count the number of positive and negative numbers entered, and print those values after the 0 is entered.
'''

count = 0
pos = 0
neg = 0


while True:
    number = float(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    count = count +1
    if number > 0:
        pos = pos +1
    else:
        neg = neg +1
        
print("You entered", count, "numbers")
print("Positive numbers:", pos) 
print("Negative numbers:", neg)