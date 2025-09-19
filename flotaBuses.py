from bus import Bus

class FlotaBuses:
    __flotaBuses = []
    
    def __init_(self):
        pass
    def get_bus_by_id(self, id):
        bus_to_return = None
        for bus in self.__flotaBuses:
            if bus.get_id() == id:
                bus_to_return = bus
        return bus_to_return
    def get_buses(self):
        return self.__flotaBuses
    def add_bus(self, cantidad, linea):
        new_bus = Bus(cantidad, linea)
        self.__flotaBuses.append(new_bus)