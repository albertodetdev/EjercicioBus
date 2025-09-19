from billete import Billete

class EstadoVentas:
    def __init__(self, plazas_totales):
        self.__diccionario_ventas = {
            "plazas_totales" : plazas_totales,
            "plazas_libres" : plazas_totales,
            "plazas_ocupadas" : 0
        }
        self.__registro_ventas = {}
        pass

    def get_plazas_totales(self):
        return self.__diccionario_ventas["plazas_totales"]
    
    def get_plazas_libres(self):
        return self.__diccionario_ventas["plazas_libres"]
    
    def get_plazas_ocupadas(self):
        return self.__diccionario_ventas["plazas_ocupadas"]
    
    def get_registro_ventas(self):
        return self.__registro_ventas
    
    def get_billete_by_ID(self, id):
        return self.__registro_ventas[id]
    
    def get_billetes_by_user_id(self, id):
        billetes_usuario = []
        for billete_id, usuario_id in self.__registro_ventas.items():
            if usuario_id == id:
                billetes_usuario.append(self.__registro_ventas[billete_id])
        return billetes_usuario

    def venta_billete(self, usuario_id, cantidad = 1):
        billetes_vendidos = 0 
        if cantidad <= self.get_plazas_libres:
            for i in range(cantidad):
                billete = Billete()
                self.__registro_ventas[billete.get_id()] = usuario_id
                billetes_vendidos += 1
            self.__diccionario_ventas["plazas_ocupadas"] += cantidad
            self.__diccionario_ventas["plazas_libres"] -= cantidad
        return billetes_vendidos

    def devolucion_billetes(self, usuario_id, billetes):
        cantidad_devuelta = 0
        for billete in billetes:
            billete_id = billete.get_id()
            if billete_id in self.__registro_ventas and self.__registro_ventas[billete_id] == usuario_id:
                del self.__registro_ventas[billete_id]
                cantidad_devuelta += 1
        self.__diccionario_ventas["plazas_ocupadas"] -= cantidad_devuelta
        self.__diccionario_ventas["plazas_libres"] += cantidad_devuelta
        return cantidad_devuelta
