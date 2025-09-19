from estadoVentas import EstadoVentas

class Bus:
    __contador_buses = 0

    def __init__(self, plazas, linea):
        self.__id = self.__contador_buses
        self.__contador_buses += 1
        self.__cantidad_plazas = plazas
        self.__estado_ventas = EstadoVentas(plazas)
        self.__nombre_linea = linea
    def get_estado_ventas(self):
        return self.__estado_ventas
    def get_id(self):
        return self.__id
    def __str__(self):
        return f"Linea: {self.__nombre_linea}, plazas: {self.__cantidad_plazas}"
    