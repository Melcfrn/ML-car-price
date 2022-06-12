from brand import Brand
from webscrapper import WebScrapper

test = WebScrapper(url_brands='https://www.lacentrale.fr/occasion-voiture.html',
                   url_models='https://www.lacentrale.fr/occasion-voiture-modele.html')
brands = test.get_brands()
models = test.get_models()
cars = test.disperse_models()
rep = input('Please, Fill the brand you want...').upper()
brand = Brand(rep, cars[rep], None)
brand.print_models()
