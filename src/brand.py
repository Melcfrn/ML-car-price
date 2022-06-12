

class Brand():
    def __init__(self, name, models, country) -> None:
        self.name = name
        self.models = models
        self.country = country
    
    def get_models(self):
        return self.models

    def print_models(self):
        print('{} models available in \'LaCentrale\' are : \n'.format(self.name))
        for modele in self.models:
            print(modele)