class Usuario:
    __contador_usuarios = 0
    
    def __init__(self, nombre, apellido):
        self.__contador_usuarios += 1
        self.__id = self.__contador_usuarios
        self.__nombre = nombre
        self.__apellido = apellido

    def get_id(self):
        return self.__id

    def editar_usuario(self, nombre=None, apellido=None):
        if nombre is not None:
            self.__nombre = nombre
        if apellido is not None:
            self.__apellido = apellido
    def get_name(self):
        return self.__nombre
    def get_surname(self):
        return self.__apellido
    def get_usuario(self):
        return f"ID: {self.__id}, Nombre: {self.__nombre}, Apellido: {self.__apellido}"