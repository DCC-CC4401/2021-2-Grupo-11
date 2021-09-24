from urllib.request import Request, urlopen
from lxml import etree
import json
import re

# Aquí se ponen todos los datos
file = "cpu_coolers"               # nombre url solotodo
modelo = "Componentes.CoolerCPU"   # nombre modelo django
pagenum = 19     # cantidad de páginas
lastpage = 9    # elementos última página - de 1 a 12, hay que revisar
descnum = 5     # numero de descripciones - fuente poder tiene 4

# No modificar nada aquí abajo

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
            desc_etree = result.xpath('//div[@class="description-container"]')[i]
            desc = desc_etree.xpath('//dd/text()')
            desc4 = desc[4] if descnum == 5 else ""
            product={"model": modelo, "pk": num, "fields":{"name":name, "url":"https://www.solotodo.cl"+url_p, "desc0": desc[0], "desc1": desc[1], "desc2": desc[2], "desc3": desc[3], "desc4": desc4}}            
            products.append(product)
            num +=1

    with open(file+'.json', 'w') as outfile:
        json.dump(products, outfile)

url = "https://www.solotodo.cl/"+file+"?page="
componentesLista(url, pagenum)





