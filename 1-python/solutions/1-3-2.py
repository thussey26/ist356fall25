'''
Write a function called `cleanup` which takes a string as input and returns a "cleaned string" meaning:
 - remove any ? , . or !
 - strip off the whitespace from the ends
 - return text in lower case
 
 write code to call your function and test it

'''
def cleanup(dirtystr:str)->str:
    for ch in '?,.!':
        if ch in dirtystr:
            dirtystr=dirtystr.replace(ch,'')
            
            
    return dirtystr.strip().lower()



#main program 

dirtystr = "  Hello, World!  "
cleanedstr = cleanup(dirtystr) 
print(cleanedstr)  # Output should be "hello world" 
        
        
