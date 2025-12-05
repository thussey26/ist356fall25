# Code Challenge 1-1-4¶
'''
Number to Letter grade
Letter grades in a college class are computed as follows:

95 and above is an A
75 and above, but below 95 is a B
50 and above, but below 75 is a C
below 50 is F
Write a program to input the number grade and calculate the letter grade

Re-write to account for "bad" grades > 120 or < 0
'''
try:
    # Get the number grade from the user
    grade = float(input("Enter the student's number grade: "))
    
    # Calculate the letter grade based on the number grade
    if grade < 0 or grade > 120:
        print("Invalid grade. Please enter a grade between 0 and 120.")
    if grade >= 95:
        print("Your letter grade is A")
    elif grade >= 75:
        print("Your letter grade is B")
    elif grade >= 50:
        print("Your letter grade is C")
    else:
        print("Your letter grade is F")

except ValueError:
    print("Invalid input. Please enter a number.")
