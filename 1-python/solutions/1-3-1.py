## Challenge 1-3-1
'''
Write a function called `average` which takes a list of numbers as input then outputs the average of the numbers sum / count

Call your function with an arbitrary list of numbers you create.

'''



    
def average(list_nums:list)->int:
    '''
    This function that a takes items in a list of numbers 
    and calculates average. 
    This returns an estimate rounded down integer. 
    
    '''
    # do something
    total = sum(list_nums)
    count = len(list_nums)
    return total//count

nums = [10, 20, 10, 5]
avg = average(nums)
print(f"Average of {nums} is {avg}")


# Another approach 

def average2 (list_of_numbers:list)->float:
    
    '''
    This function that a takes items in a list of numbers 
    and calculates average. 
    This returns a float. 
    
    '''
    total = 0
    count = 0

    for number in list_of_numbers:
        total += number
        count += 1
    return total/count


nums = [10, 20, 10, 5]
avg = average2(nums)
print(f"Average of {nums} is {avg}")