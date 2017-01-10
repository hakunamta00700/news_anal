

# -*- coding: utf-8 -*-
from grab import Grab
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__file__)


def get_page(url):
    print(url)
    g = Grab(timeout=5000)
    resp = g.go(url)
    soup = resp.select("#cbox_module")
    pprint.pprint(soup)


def main(url):
    get_page(url)


if __name__ == '__main__':
    import sys
    url = sys.argv[1]
    main(url)
