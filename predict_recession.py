import config as c
from get_ffr import *
from get_treasury import *
from send_email import *
from math import *

import datetime

def predict_recession_main():

    date = datetime.date.today()
    fdate = date.strftime('%m/%d/%y')

    effr = -1
    while effr == -1:
        yields = get_yields(fdate, c.TREASURY_URL_PREFIX)
        effr = get_effr(fdate[0:5], c.FFR_URL)
        if effr == -1:
            d = datetime.timedelta(days=-1)
            date += d
            fdate = date.strftime('%m/%d/%y')

    spread = yields['10_year'] - yields['3_month']

    stddev = c.MATH_CONSTANT_A - (c.MATH_CONSTANT_B * spread) + (c.MATH_CONSTANT_C * effr)
    probit = (1.0 + erf(stddev / sqrt(2.0)))/2.0

    msg = '\nDate: ' + fdate + '\nProbit: ' + str(probit) + '\n' \
        + '' + str(yields['3_month']) + '\t' + str(yields['10_year']) + '\t' + str(effr)
    print(msg)
    send_email(msg)

predict_recession_main()