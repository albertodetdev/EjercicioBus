class Billete:
    __contador_billetes = 0
    __precio = 100
    def __init__(self):
        self.__id = self.__contador_billetes
        self.__contador_billetes += 1
        
    def get_billetes(self):
        return f"ID: {self.__id}, Precio: {self.__precio} pesos"