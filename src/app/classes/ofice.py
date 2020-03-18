class Oficina:
    def __init__(self, id, address):
        self.id = id
        self.address = address

    def set_ciudad(self, id_ciudad):
        self.id_ciudad = id_ciudad

    def get_ciudad(self):
        return self.id_ciudad
