from estadoVentas import EstadoVentas

class Bus:
    __contador_buses = 0

    def __init__(self, plazas):
        self.__id = self.__contador_buses
        self.__contador_buses += 1
        self.__cantidad_plazas = plazas
        self.__estado_ventas = EstadoVentas()
    def get_estado_ventas(self):
        return self.__estado_ventas
    