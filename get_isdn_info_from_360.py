import requests
from lxml import etree
import time

import sys

if len(sys.argv) < 2:
    print "pls input the isdn file."
else:
    isdn = sys.argv[1]


def getISDN(isdn):
    if len(isdn) < 11:
        tmp = "0760"+isdn
	isdn = tmp
    url = "https://www.so.com/s?q=" + isdn

    s = requests.Session()
    html_context = s.get(url).content

    isdn_info = etree.HTML(html_context)
    isdn_home = isdn_info.xpath('//p[@class="mh-detail"]/text()')
    if len(isdn_home) >= 1:
        aa = isdn_home[0].encode('utf-8')
        a = aa[11:22]
        b = aa[59:65]
        c = aa[77:83]
        d = aa[119:125]
        print a, b, c, d

    isdn_homev2 = isdn_info.xpath('//div[@class="gclearfix mh-detail"]/span/text()')
    if len(isdn_homev2) >= 1:
        aa = isdn_homev2[0].encode('utf-8')
        bb = isdn_homev2[1].encode('utf-8')
        print aa[10:21], bb[20:26], bb[37:43], bb[76:82]


    table = isdn_info.xpath("//span[@style]/text()")
    if len(table) > 4:
        num = isdn_info.xpath("//b/text()")
        aa = table[1] + num[0] + table[2] + table[3]
        print isdn.strip() + " " + aa.strip()
    else:
        print isdn.strip() + "  "


for line in open(sys.argv[1]):
    getISDN(line)
#    time.sleep(1)
