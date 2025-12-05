'''
Let's make the code in 1-4-1 more resusable 

re-write the date parse into a function `parsedate_mdy(text: str) -> datetime:`   
re-write the date format into a function `formatdate_ymd(date: datetime) -> str:`  
re-write the main program to use both functions. input -> parsedate -> formatdate -> output


'''


from datetime import datetime

def parsedate_mdy(text: str) -> datetime:
    """
    Parses a date in the format mm/dd/yyyy and returns a datetime object.
    """
    return datetime.strptime(text, '%m/%d/%Y')

def formatdate_ymd(date: datetime) -> str:
    """
    Takes a datetime object and returns a string in the format yyyy-mm-dd.
    """
    return date.strftime("%Y-%m-%d")

# Main code
test = input("Enter date m/d/y: ")  # Example input: 12/30/2000
date = parsedate_mdy(test)
date_str = formatdate_ymd(date)
print(date_str)  # Output: 2000-12-30


