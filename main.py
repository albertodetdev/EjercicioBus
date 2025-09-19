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

def selecciona_bus(data_dictionary):
    print_buses(data_dictionary)
    print(f"Su bus actual es: {data_dictionary["flota_buses"].get_bus_by_id(data_dictionary["bus_actual"])}")
    option = input()

    while validate_menu_input_int(option) == False or int(option) >= len(data_dictionary["flota_buses"].get_buses()) + 1:
        option = input()
    option = int(option) - 1
    print(f"Su bus se ha cambiado correctamente a {data_dictionary["flota_buses"].get_bus_by_id(data_dictionary["flota_buses"].get_buses()[option].get_id())}")
    data_dictionary["bus_actual"] = option

def consulta_buses(data_dictionary):
    opcion = -1
    print("BUSES")
    print("-----------")
    print_buses(data_dictionary)
    print("0.- Volver")
    opcion = int(input())
    while opcion != 0:
        if validate_menu_input_int(opcion) == False:
            opcion = int(input())
    print("")

def print_buses(data_dictionary):
    contador = 0
    for bus in data_dictionary["flota_buses"].get_buses():
        contador += 1
        print(f"{contador}.- {bus}")
def vender_billetes(data_dictionary):
    return data_dictionary
def devolver_billetes(data_dictionary):
    return data_dictionary

def interface_menu(data_dictionary):
    print("cls")
    print('''Seleccione una opcion \n
    1.- Crea un bus \n
    2.- Selecciona tu bus \n
    3.- Consulta buses \n
    4.- Vender billete \n
    5.- Devolver billete \n
    0.- Exit''')
    option = input()
    while validate_menu_input_int(option) == False:
        option = input()
    data_dictionary["option"] = option
    return data_dictionary

data_dictionary["flota_buses"] = FlotaBuses()

while data_dictionary["option"] != "0":
    data_dictionary["option"] = interface_menu(data_dictionary)["option"]
    if data_dictionary["option"] == "1":
        data_dictionary["flota_buses"] = create_bus(data_dictionary["flota_buses"])
    elif data_dictionary["option"] == "2":
        selecciona_bus(data_dictionary)
    elif data_dictionary["option"] == "3":
        consulta_buses(data_dictionary)
    elif data_dictionary["option"] == "4":
        data_dictionary = vender_billetes(data_dictionary)
    elif data_dictionary["option"] == "5":
        data_dictionary = devolver_billetes(data_dictionary)