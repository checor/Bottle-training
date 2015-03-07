#Cotizador
from bottle import route, run, template, static_file, request

@route('/', method='GET')
def home():
	if request.GET.get('link', ''):
		penes = request.GET.get('link', '').strip()
		return "<b>Arigatou Duri san %s</b>" % penes
	else:
		return static_file('cock.html', root="C:/Users/checor/Documents/Bitbucket/botella/")

run(host='localhost', port=8080, debug='on')