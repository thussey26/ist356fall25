'''

Let's make the code in 1-4-2 more resusable!!! 

move your functions into a module names `dateutils.py`

import your functions from `dateutils.py` into `1-4-3.py`


'''


from datetime import datetime
from dateutils import parsedate_mdy, formatdate_ymd

'''
#Main Code
text = input('Enter date m/d/y: ') #12/30/2000
date = parsedate_mdy(text)
date_str = formatdate_ymd(date)
print(date_str) #2000-12-30
'''

# Testing Code
'''
date = "12/30/2000"
date_dt_expect = datetime(2000, 12, 30)
date_dt_actual = parsedate_mdy(date)
assert date_dt_expect == date_dt_actual
'''

# For testing with pytest need to make functions
def test_formatdate_ymd():
    date_dt = datetime(2000, 12, 30)
    date_str_expect = "2000-12-30"
    date_str_actual = formatdate_ymd(date_dt)
    assert date_str_expect == date_str_actual


