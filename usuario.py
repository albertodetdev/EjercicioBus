class Usuario:
    __contador_usuarios = 0
    
    def __init__(self, nombre, apellido):
        Usuario.__contador_usuarios += 1
        self.__id = Usuario.__contador_usuarios
        self.__nombre = nombre
        self.__apellido = apellido
        self.__billetes = []

    def get_id(self):
        return self.__id

    def editar_usuario(self, nombre=None, apellido=None):
        if nombre is not None:
            self.__nombre = nombre
        if apellido is not None:
            self.__apellido = apellido

    def get_usuario(self):
        return f"ID: {self.__id}, Nombre: {self.__nombre}, Apellido: {self.__apellido}"
    
    def get_billetes(self):
        return self.__billetes.copy()
    
    def agregar_billete(self, billete):
        self.__billetes.append(billete)
    
    def remover_billetes(self, billetes):
        for billete in billetes:
            if billete in self.__billetes:
                self.__billetes.remove(billete)