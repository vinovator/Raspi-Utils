# get_forex_rate_py2.py
# Python 2.7.6

"""
parse the forex rates from fixer api
If the exchange rate is equal or more than a defined constant,
send mail alert to specific email
"""

import requests
from urllib import urlencode

api = "http://api.fixer.io/latest"
base_currency = {"base": "GBP"}
alert_value = 100


def get_GBP_INR_rate():
    """
    Get the exchange rate from GBP to INR
    """

    params = urlencode(base_currency)

    resp = requests.get(api, params=params)  # returns json

    rates = resp.json()

    INR_rate = rates["rates"]["INR"]

    return INR_rate


if __name__ == "__main__":
    """ Block to test the library fuction directly """

    print(get_GBP_INR_rate())
