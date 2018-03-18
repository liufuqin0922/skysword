import requests
from lxml import etree

import sys

if len(sys.argv) < 2:
    print "pls input the isdn file."
else:
    isdn = sys.argv[1]


def getISDN(isdn):
    url = "https://www.so.com/s?q=" + isdn

    s = requests.Session()
    html_context = s.get(url).content

    isdn_info = etree.HTML(html_context)

    table = isdn_info.xpath("//span[@style]/text()")
    if len(table) > 4:
        num = isdn_info.xpath("//b/text()")
        aa = table[1] + num[0] + table[2] + table[3]
        print isdn.strip() + " " + aa.strip()
    else:
        print isdn.strip() + "  "


for line in open(sys.argv[1]):
    getISDN(line)
