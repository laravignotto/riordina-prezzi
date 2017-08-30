#guida su http://docs.python-guide.org/en/latest/scenarios/scrape/
from lxml import html
import requests

page = requests.get('https://myshop.carrefour.it/spesa-ritiro-negozio/udine-viale-tricesimo-14917/frutta_277?sort=sold')
tree = html.fromstring(page.content)

#crea una lista di prodotti
#prodotto = tree.xpath('//h3[@itemprop="name"]/text()')
#crea una lista di prezzi al chilo:
prezzo_al_kg = tree.xpath('//div[@class="product-meta"]/text()')

#print 'Prodotto: ', prodotto
#print 'Prezzo al kg: ', prezzo_al_kg

#aggiusto prezzo_al_kg in modo da avere solo il prezzo
for i in prezzo_al_kg:
	a = list(i)
	print ''.join(a[:4])
	
#print 'Prezzo al kg: ', prezzo_al_kg


