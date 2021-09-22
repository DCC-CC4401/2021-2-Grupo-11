from urllib.request import Request, urlopen
from lxml import etree
import re

url = "https://www.solotodo.cl/products/13031-intel-pentium-g3220"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()
tree = etree.HTML(html)

meta = tree.xpath('//meta[@property="og:title"]')[0]
name = re.match(etree.tostring(meta), re.compile('content="(\s+)"'))