class Billete:
    __contador_billetes = 0
    __precio = 100
    
    def __init__(self):
        self.__contador_billetes += 1
        self.__id = Billete.__contador_billetes
        
    def get_billete(self):
        return f"ID: {self.__id}, Precio: {self.__precio} pesos"
    
    def get_id(self):
        return self.__id
    
    def get_precio(self):
        return self.__precio