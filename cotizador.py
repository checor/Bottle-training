#Cotizador
import csv, re
import urllib
import datetime
import sqlite3
from amazon.api import AmazonAPI
from bottle import route, run, template, static_file, request, auth_basic, response
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent


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

def get_price(url, store='Amazon'):
    if store == 'Amazon':
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
        return 'Por favor, logueate antes de entrar.'
    elif request.GET.get('SKU',''):
        return "Esto fue lo que me mandaron putos: %s" % request.query.decode()
    else:
        conn = sqlite3.connect('tunas.db')
        c = conn.cursor()
        c.execute("SELECT * FROM productos")
        result = c.fetchall()
        c.close()

        return template('productos.tpl', rows=result)


run(host='0.0.0.0', port=8080, autoreload=True)
