class City:
    def __init__(self, zip_code, city_name):
        self.zip_code = zip_code
        self.city_name = city_name

    def set_pais(self, id_pais):
        self.id_pais = id_pais

    def get_pais(self):
        return self.id_pais
