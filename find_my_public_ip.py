# find_my_public_ip.py
# Python 3.5

import requests
from bs4 import BeautifulSoup

url = "http://checkip.dyndns.com/"


def get_ip():
    """
    Get the public ip of the server by scraping the http://checkip.dydns.com
    """

    try:
        resp = requests.get(url)

        if resp.ok:
            soup = BeautifulSoup(resp.content, "lxml")
            return soup.find("body").getText()

    except requests.exceptions.ConnectionError as e:
        return "Error connecting to the site" + str(e)

if __name__ == "__main__":
    """ Block to test the library fuction directly """

    print(get_ip())
