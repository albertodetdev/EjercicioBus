from bus import Bus

class FlotaBus:
    flotaBuses = []
    
    def __init_(self):
        pass
    def get_bus_by_id(self, id):
        return self.flotaBuses[id]
    def get_buses(self):
        return self.flotaBuses
    def add_bus(self, bus):
        self.flotaBuses.append(bus)