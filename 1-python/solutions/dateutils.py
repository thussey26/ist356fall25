from datetime import datetime

def parsedate_mdy(text: str) -> datetime:
    """
    Parses a date in the format mm/dd/yyyy and returns a datetime object.
    """
    return datetime.strptime(text, '%m/%d/%Y')

def formatdate_ymd(date: datetime):
    """
    Takes a datetime object and returns a string in the format yyyy-mm-dd.
    """
    return date.strftime("%Y-%m-%d")


if __name__ == "__main__":
#Main Code
# main code
    text = input('Enter date m/d/y: ') #12/30/2000
    date = parsedate_mdy(text)
    date_str = formatdate_ymd(date)
    print(date_str) #2000-12-30
    text = input('Enter date m/d/y: ') #12/30/2000
    date = parsedate_mdy(text) 
    date_str = formatdate_ymd(date)
    print(date_str) #2000-12-30

def test_parsedate_mdy():
    # Test the parsedate_mdy function
    assert parsedate_mdy("12/31/2020") == datetime(2020, 12, 31)
    assert parsedate_mdy("03/06/2020") == datetime(2020, 3, 6)

def test_formatdate_ymd():
    # Test the formatdate_ymd function
    assert formatdate_ymd(datetime(2020, 12, 31)) == "2020-12-31"
    assert formatdate_ymd(datetime(2020, 3, 6)) == "2020-03-06"
