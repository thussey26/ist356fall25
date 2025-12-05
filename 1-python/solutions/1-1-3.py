# Code Challenge 1-1-3¶

'''
a presssure sensor determines whether or not to open a door

When the pressure is larger than 10 we want the door open

otherwise we want it closed

write code to simulate this
'''

sensor = float(input("Enter the pressure reading: "))

# Check if the pressure is greater than 10.
if sensor > 10:
    print(f"Pressure is {sensor:.2f}. The door is OPEN.")
else:
    print(f"Pressure is {sensor:.2f}. The door is CLOSED.")
    
