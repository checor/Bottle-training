#Cotizador
import csv, re
from amazon.api import AmazonAPI
from bottle import route, run, template, static_file, request

def get_csv(csv_file='rootkey.csv'):
    dic = {}
    with open(csv_file, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            s = row[0].split('=')
            dic[s[0]] = s[1]
    return dic

def get_price(url, store='Amazon'):
    if store == 'Amazon':
        dic = get_csv()
        api = AmazonAPI(dic['AWSAccessKeyId'], dic['AWSSecretKey'], dic['asoc'])
        id_ = re.search("/dp/(.*?)/", url).group(1)
        product = api.lookup(ItemId=id_)
        price = str(product.price_and_currency[0])
        price = float(price.translate(None, '$'))
        return price


@route('/', method='GET')
def home():
	if request.GET.get('link', ''):
		url = request.GET.get('link', '').strip()
                print url
                print "\n\n\n\n\n"
                return template('cotizador.tpl', usd_price=get_price(url),
                        usd_mxn=15.3)
	else:
		return static_file('cock.html', root=".")

run(host='localhost', port=8080)
