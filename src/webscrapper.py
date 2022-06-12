############################################################
# Packages                                                 #
############################################################

import requests
from bs4 import BeautifulSoup

############################################################
# Classe                                                   #
############################################################

class WebScrapper():
    def __init__(self, url_brands, url_models) -> None:
        self.url_brands = url_brands
        self.url_models = url_models

    def get_brands(self):
        response = requests.get(self.url_brands)
        soup=BeautifulSoup(response.content, 'html.parser')
        s = soup.find('section', class_= 'containerGlobal')
        mainlist = s.find('div', class_='mainList')
        content = mainlist.find_all('a')
        brands = list()
        for brand in content:
            if len(brand) > 0:
                brands.append(brand.text)
        return brands
    
    def get_models(self):
        response = requests.get(self.url_models)
        soup=BeautifulSoup(response.content, 'html.parser')
        s = soup.find('section', class_= 'containerGlobal')
        mainlist = s.find('div', class_='mainList')
        content = mainlist.find_all('a')
        models = list()
        for model in content:
            if len(model) > 0:
                models.append(model.text)
        return models
    
    def disperse_models(self):
        brands = self.get_brands()
        models = self.get_models()
        cars_dict = dict()
        for brand in brands:
            cars_dict[brand] = list() #Changer en dictionnaire pour ajouter des informations ?
            for model in models:
                if brand in model:
                    cars_dict[brand].append(model.replace(brand + ' ', ''))
        return cars_dict

    def get_announces(self, brand=None, ):
        pass