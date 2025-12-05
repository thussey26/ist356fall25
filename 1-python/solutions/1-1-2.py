# Code Challenge 1-1-2
'''
Let' write a program to divide up the check among diners in a party.

Write a program to input the amount of a restaurant check, tip %, and number of diners

The program should output the total amount with tip, and the amount each diner owes.
'''

amount = float(input("Enter the total check"))
tip = float(input("Enter the tip percent"))
diners = int(input("Enter number of diners: "))

# Calculate the total amount with tip.
tip_amount = amount * (tip / 100)
total_with_tip = amount + tip_amount

# Calculate what each person owes
amount_owed = total_with_tip / diners

# Output the results, formatted to two decimal places for currency.
print(f"Total camount: ${amount:.2f}")
print(f"Tip amount ({tip}%): ${tip_amount:.2f}")
print(f"Total with tip: ${total_with_tip:.2f}")
print(f"Amount owed: ${amount_owed:.2f}")
