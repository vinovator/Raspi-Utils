# find_my_public_ip_py2.py
# Python 2.7.6

import requests
from BeautifulSoup import BeautifulSoup

url = "http://checkip.dyndns.com/"


def get_ip():
    """
    Get the public ip of the server by scraping the http://checkip.dydns.com
    """

    try:
        resp = requests.get(url)

        if resp.ok:
            soup = BeautifulSoup(resp.content)
            return soup.find("body").getText()

    except requests.exceptions.ConnectionError:
        return "Error connecting to the site"

if __name__ == "__main__":
    """ Block to test the library fuction directly """

    print(get_ip())
