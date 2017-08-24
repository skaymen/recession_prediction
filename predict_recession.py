import config as c
from get_ffr import *
from get_treasury import *

import datetime


date = datetime.date.today().strftime('%m/%d/%y')

print(get_yields(date, c.TREASURY_URL_PREFIX))
print(get_effr(date, c.FFR_URL))

#Testing committ