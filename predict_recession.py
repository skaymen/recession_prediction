import config as c
from get_ffr import *
from get_treasury import *

import datetime


date = datetime.date.today().strftime('%m/%d/%y')

yields = get_yields(date, c.TREASURY_URL_PREFIX)
effr = get_effr(date, c.FFR_URL)
