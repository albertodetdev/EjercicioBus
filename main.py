from flotaBuses import FlotaBuses
data_dictionary = {
    "option": -1,
    "flota_buses": FlotaBuses,
    "bus_actual": 0
}
user_dictionary = {
    "user_name": "",
    "user_surname": ""
}

def validate_menu_input_int(input):
    if input.isdigit():
        return True
    else:
        print("input erroneo, intentelo otra vez")
        return False

def enter_user_data(user_dictionary):
    print("Introduzca su nombre")
    user_dictionary["user_name"] = input()
    print("Introduzca un apellido")
    user_dictionary["user_surname"] = input()

def create_bus(flota_buses):
    print("Introduzca la cantidad de plazas del bus")
    cantidad = input()
    while validate_menu_input_int(cantidad) == False:
        cantidad = input()
    print("Introduzca el nombre de la linea del bus")
    linea = input()
    flota_buses.add_bus(cantidad, linea)
    return flota_buses

def print_all_buses(flota_buses):
    all_buses = flota_buses.get_buses()
    for bus in all_buses:
        print(bus)


def selecciona_bus(data_dictionary):
    print_all_buses(data_dictionary["flota_buses"])
    print(f"Su bus actual es: {data_dictionary["flota_buses"].get_bus_by_id(data_dictionary["bus_actual"])}")
    option = input()

    while validate_menu_input_int(option) == False or option >= len(data_dictionary["flota_buses"]):
        option = input()
        
    print("Su bus se ha cambiado correctamente")
    data_dictionary["bus_actual"] = option 

def interface_menu(data_dictionary):
    print("Seleccione una opcion" \
    "1.- Crea un bus" \
    "2.- Selecciona tu bus" \
    "3.- Consulta buses" \
    "0.- Exit")
    data_dictionary["option"] = input()
    while validate_menu_input_int(data_dictionary["option"]) == False:
        data_dictionary["option"] = int(input())
    return data_dictionary

data_dictionary["flota_buses"] = FlotaBuses()

while data_dictionary["option"] != 0:
    data_dictionary["option"] = interface_menu(data_dictionary)
    if data_dictionary["option"] == 1:
        create_bus(data_dictionary["flota_buses"])
    elif data_dictionary["option"] == 2:
        selecciona_bus(data_dictionary)