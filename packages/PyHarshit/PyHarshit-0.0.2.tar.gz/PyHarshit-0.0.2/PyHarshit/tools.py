import urllib
from urllib.request import urlopen


def internet_available():
    """
    Query internet using python
    :return:
    """
    try:
        urlopen('https://www.google.com', timeout=1)
        return True
    except urllib.error.URLError as Error:
        print(Error)
        return False
