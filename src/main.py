from brand import Brand
from webscrapp import WebScrapper

test = WebScrapper(url_brands='https://www.lacentrale.fr/occasion-voiture.html',
                   url_models='https://www.lacentrale.fr/occasion-voiture-modele.html')
brands = test.get_brands()
models = test.get_models()
cars = test.disperse_models()
print(cars['PEUGEOT'])
