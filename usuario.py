class Usuario:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        self.billetes = []

    def editar_usuario(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def get_usuario(self):
        return f"Nombre: {self.__nombre}, Apellido: {self.__apellido}"
    
    def get_billetes(self):
        return self.billetes