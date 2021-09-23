from urllib.request import Request, urlopen
from lxml import etree
import json
import re

modelo = "Componentes.CoolerCPU"
lastpage = 8

def componentesLista(url, numpage):
    products=[]
    num = 1
    for i in range(1, numpage+1):
        req = Request(url+str(i), headers={'User-Agent': 'Mozilla/5.0'})
        tree = etree.HTML(urlopen(req).read())
        result = tree.xpath('//div[@class="d-flex flex-column category-browse-result"]')[0]
        page = 12 if i != numpage else lastpage
        for i in range(page):
            url_etree = result.xpath('//div[@class="price flex-grow"]//a')[i]
            url_p = url_etree.get("href")
            name = result.xpath('//a[@href="'+url_p+'"]/text()')[0]
            product={"model": modelo, "pk": num, "fields":{"name":name, "url":"https://www.solotodo.cl"+url_p}}            
            products.append(product)
            num +=1

    with open('data.json', 'w') as outfile:
        json.dump(products, outfile)

url = "https://www.solotodo.cl/cpu_coolers?page="
componentesLista(url, 19)





