#Challenge 1-2-3¶
'''
Write a sentinel controlled loop to input a color until "quit" is entered. add each color to a list 
only when the color is not already in the list print the list each time in the loop.
'''


colors = []
while True:
    color = input("Enter a color: ")
    if color == "quit":
        print("Exiting")
        break
    if color not in colors:
        colors.append(color)
        op = 'added to'
    else:
        op = 'already in'
    print(f"{color} is {op} the list")