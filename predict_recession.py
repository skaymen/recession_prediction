import config as c
from get_ffr import *
from get_treasury import *
from send_email import *
from math import *

import datetime


date = datetime.date.today().strftime('%m/01/%y')

def predict_recession_main():
    yields = get_yields(date, c.TREASURY_URL_PREFIX)
    effr = get_effr(date[0:5], c.FFR_URL)
    stddev = c.MATH_CONSTANT_A + (c.MATH_CONSTANT_B * yields) + (c.MATH_CONSTANT_C * effr)
    #FIXME Fairly sure this accurately calculates the probit, but it doesn't match the excel document.
    probit = (1.0 + erf(stddev / sqrt(2.0)))/2.0
#   print(probit)

    msg = 'fuck you Stanley. Probit: ' + str(probit)
    send_email(msg)

predict_recession_main()

# print(yields)
# print(effr)