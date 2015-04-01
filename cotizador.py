#Cotizador
import re
import urllib
import datetime
import sqlite3
import csv
from amazon.api import AmazonAPI
from bottle import route, run, template, static_file, request, auth_basic, response
from bs4 import BeautifulSoup as BS
#from fake_useragent import UserAgent


##
##  Cotizador
##

def check(user, pw):
    if user=='impor' and pw == 'tunas':
        response.set_cookie("visited", "yes")
        return True
    return False

def get_csv(csv_file='rootkey.csv'):
    dic = {}
    with open(csv_file, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            s = row[0].split('=')
            dic[s[0]] = s[1]
    return dic

class MyOpener(urllib.FancyURLopener):
    pass

def get_dollar():
    ban_url = "http://www.dolar.mx/precio-del-dolar-hoy/"
    opener = MyOpener()
    page = BS(opener.open(ban_url).read())
    precios = page.findAll("h2")
    valores = str(precios[3])
    precio = re.findall("- \$(.*?) <br/>", valores)[1]
    return float(precio)

def get_price(url):
    if 'amazon' in url:
        dic = get_csv()
        api = AmazonAPI(dic['AWSAccessKeyId'], dic['AWSSecretKey'], dic['asoc'])
        if '/dp/' in url:
        	id_ = re.search("/dp/(.*?)/", url).group(1)
        elif '/product/' in url:
        	id_ = re.search("/product/(.*?)/", url).group(1)
        else:
        	return 0
        product = api.lookup(ItemId=id_)
        price = str(product.price_and_currency[0])
        price = float(price.translate(None, '$'))
    else:
        opener = MyOpener()
        if 'hottopic' in url:
            page = opener.open(url).read()
            soup = BS(page)
            try:
                price = str(soup.find(class_ = "Now").text)
                price = float(price.translate(None, '$'))
            except:
                print "Articulo no encontrado"
                price = 0
        elif 'toywiz' in url:
            page = opener.open(url).read()
            soup = BS(page)
            try:
                price = str(soup.find(class_ = "itemPriceBlock").text)
                price = float(price.translate(None, '$'))
            except:
                print "Error al querer obtener precio de ToyWiz"
                price = 0
            return price
        elif 'barnes' in url:
            opener = MyOpener()
            page = opener.open(url)
            soup = BS(page)
            try:
                price = str(soup.find(class_ = 'price hilight').text)
                price = float(price.translate(None, '$'))
            except:
                price = 0
        else:
            print "Tienda no implmentada"
    return price

@route('/', method='GET')
@auth_basic(check)
def cot():
    #if not request.get_cookie("visited"):
    #    return 'Por favor, logueate antes de entrar.'
    if request.GET.get('link', ''):
        url = request.GET.get('link', '').strip()
        return template('cotizador.tpl', usd_price=get_price(url),
                        usd_mxn=get_dollar())
    else:
        return static_file('cock.html', root=".")

##
##  Productos
##


@route('/productos', method='GET')
@auth_basic(check)
def prod():
    if not request.get_cookie("visited"):
        return 'Por favor, logueate antes de entrar. Presiona F5 si ya lo hiciste'
    elif request.GET.get('SKU',''):
        data = dict(request.query)
        print data
        conn = sqlite3.connect('tunas.db')
        c = conn.cursor()
        if 'nombre' in data:
            c.execute("INSERT INTO productos ('ID', 'Nombre') values (?,?)", (data['SKU'], data['nombre']))
            #c.execute("INSERT INTO productos_links (ID, link, tienda) values (?,?,?)",
            #        (data['SKU'], data['link'], 'amazon'))
            conn.commit()
            c.close()
            return "Producto agregado con exito!"
        elif "del_SKU" in data:
            c.execute("DELETE FROM productos WHERE ID = (?)", data['SKU'])
            conn.commit()
            c.close()
            return "Borrado D:"
        else:
            return "No implementado :("
            
    else:
        conn = sqlite3.connect('tunas.db')
        c = conn.cursor()
        c.execute("SELECT * FROM productos")
        result = c.fetchall()
        c.close()

        return template('productos.tpl', rows=result)


run(host='0.0.0.0', port=8080, autoreload=True)
