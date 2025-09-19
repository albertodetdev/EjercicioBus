from bus import Bus

class FlotaBus:
    __flotaBuses = []
    
    def __init_(self):
        pass
    def get_bus_by_id(self, id):
        return self.__flotaBuses[id]
    def get_buses(self):
        return self.__flotaBuses
    def add_bus(self, bus):
        self.__flotaBuses.append(bus)