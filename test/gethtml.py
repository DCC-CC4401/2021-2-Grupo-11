from urllib.request import Request, urlopen
from lxml import etree
import json, time

def componentesLista(file, modelo, pagenum):
    products=[]
    num = 1
    for i in range(1, pagenum+1):
        url = "https://www.solotodo.cl/"+file+"?page="
        req = Request(url+str(i), headers={'User-Agent': 'Mozilla/5.0'})
        tree = etree.HTML(urlopen(req).read())
        result = tree.xpath('//div[@class="d-flex flex-column category-browse-result"]')[0]
        url_etree = result.xpath('//div[@class="price flex-grow"]//a')
        desc_etree = result.xpath('//div[@class="description-container"]')

        page = 12 if i != pagenum else len(url_etree)
        for i in range(page):
            url_p = url_etree[i].get("href")
            info = result.xpath('//a[@href="'+url_p+'"]/text()')
            name = info[0]
            precio = info[1]
            cat = desc_etree[i].xpath('//dt/text()')
            cat4 = cat[4] if len(cat) >= 5 else "None"
            des = desc_etree[i].xpath('//dd/text()')
            des4 = des[4] if len(cat) >= 5 else "None"
            product = {"model":"Componentes."+modelo,"pk":num,"fields":{"name":name,"url":"https://www.solotodo.cl"+url_p,"precio":precio,"cat0":cat[0],"cat1":cat[1],"cat2":cat[2],"cat3":cat[3],"cat4":cat4,"des0":des[0],"des1":des[1],"des2":des[2],"des3":des[3],"des4":des4}}            
            products.append(product)
            num +=1

    with open(file+'.json', 'w') as outfile:
        json.dump(products, outfile)


# No modificar nada arriba de esto

# Descomentar alguna de las secciones de abajo y ejecutar
# Cada sección demora entre 10 y 20 minutos en ejecutarse

# Build models

#file = ["video_cards","processors","motherboards","rams","storage_drives","solid_state_drives","computer_cases","power_supplies","cpu_coolers"]
#modelo = ["GPU","Procesador","PlacaMadre","RAM","DiscoDuro","SSD","Gabinete","FuentePoder","CoolerCPU"]
#pagenum = [17, 8, 25, 53, 14, 28, 55, 27, 19]      # cantidad de páginas de productos, hay que revisar

# Setup models

#file = ["mouse","keyboards","monitors","headphones","gaming_chairs"]
#modelo = ["Mouse","Teclado","Monitor","Audifonos","SillaGamer"]
#pagenum = [91, 52, 43, 240, 61]                    # cantidad de páginas de productos, hay que revisar

# Main code

start_time = time.time()

for i in range(len(file)):
    componentesLista(file[i], modelo[i], pagenum[i])
    print(f"""Creado JSON para {file[i]}""")

print("--- %s seconds ---" % round(time.time() - start_time, 2))
