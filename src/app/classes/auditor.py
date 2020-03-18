class Auditor:
    def __init__(
        self, numero_legajo, tipo_documento, nombre, apellido, fecha_nacimiento, email
    ):
        self.numero_legajo = numero_legajo
        self.tipo_documento = tipo_documento
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.email = email
        self.clientes = []

    def get_auditor(self):
        return self.numero_legajo

    def editar_auditor(
        self, numero_legajo, tipo_documento, nombre, apellido, fecha_nacimiento, email
    ):
        self.numero_legajo = numero_legajo
        self.tipo_documento = tipo_documento
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.email = email

    def verificar_auditor(self, numero_legajo):
        return False

    def set_categoria(self, id_categoria):
        self.id_categoria = id_categoria

    def editar_categoria(self, id_categoria):
        self.id_categoria = id_categoria

    def add_cliente(self, id_cliente):
        self.clientes.append(id_cliente)

    def delete_cliente(self, id_cliente):
        self.clientes.remove(id_cliente)

    def get_clientes(self):
        return self.clientes
