import json
import os

def message(msg: str) -> None:
    input(f"{msg}\nPresion cualquier tecla para continuar...")


def readInt(msg: str) -> int:
    try:
        return int(input(f"{msg}? "))
    except ValueError:
        message(f"Error. el dato ingresado debe ser un entero.")
        return readInt(msg)

def rangeValidator(a: int, b: int, msg: str) -> int:
    option = readInt(msg)
    if option >= a and option <= b:
        return option
    else:
        message("Fuera de rango.")
        return rangeValidator(a, b, msg)

os.system("cls")
def leerDatos():
    with open('AutoShopping.json', encoding="utf-8") as miAlmacen:
        misDatos = json.load(miAlmacen)
        miListadeAutos = misDatos["autostore"]["autos"]
    i=0
    for auto in miListadeAutos:
        i+=1
        print (i, " ", auto, "\n")

def mostrarUno(i):
    i-=1
    with open('AutoShopping.json', encoding="utf-8") as miAlmacen:
            misDatos = json.load(miAlmacen)
            miAuto = misDatos["autostore"]["autos"][i]
    print(miAuto)

def mostrarEquipamiento(i):
    i-=1
    with open('AutoShopping.json', encoding="utf-8") as miAlmacen:
            misDatos = json.load(miAlmacen)
            miAuto = misDatos["autostore"]["autos"][i]["equipamiento"]
    print(miAuto)

def agregarAuto():
    auto = {
        "marca":"Chevrolet",
        "linea": "Monza",
        "modelo": "2000",
        "precio": "9000"
    }
    n=int(input("Cuántos elementos ?"))
    if (n==0):
        auto["equipamiento"] = "Sin Equipamiento "
    else:
        if (n==1):
            equipamiento=input("Ingrese el equipo: ")
        else:
            equipamiento=[]
            for i in range (n):
                equipamiento.add(input("Ingrese el equipo: "))
    auto["equipamiento"]=equipamiento          


# agregarAuto()


def buscarRegistro(cedula_b):
    for i in range(len(misDatos['empleados'])):
        if misDatos['empleados'][i]['numDoc'] == str(cedula_b):
            print("Encontrado")
            # print(misDatos['empleados'][i])
            return(misDatos['empleados'][i])
            # misDatos['empleados'][i]

def borrarRegistro(cedula_b):
    i = 0
    # for i in range(len(misDatos['empleados'])):
    encontrado = False
    while not encontrado and i < len(misDatos['empleados']):
        if misDatos['empleados'][i]['numDoc'] == str(cedula_b):
            print("Encontrado")
            encontrado = True
            print(misDatos['empleados'][i])
            respuesta =input("Desea eliminar el registro encontrado? (S/N):")
            if respuesta.upper() == "S":
                misDatos['empleados'].pop(i)
        i = i + 1
    if not encontrado:
        print("No se encontró el registro")


def menu():
    os.system("clear")
    print("{:^60}".format("MENU PRINCIPAL"))
    options = ["Mostrar todas las autos","Crear nueva registro", "Buscar registro", "Actualizar registro", "Eliminar registro","Salir"]
    for i, option in enumerate(options):
        print(f"{str(i+1):>6}. {option}")
    
    option = rangeValidator(1, 6, "opcion -> ")

    if option==6:
        return print("\nFin del programa\n")
    
    switch = {1: leerDatos, 2: agregarAuto, 3: buscarRegistro, 4: update, 5: borrarRegistro}
    switch[option]()
    menu()

##PROGRAMA PRINCIPAL
# os.system("cls")
# misDatos = {}
# leerDatos()

# print(misDatos['empleados'])
# ced = str(input("Digite la Cédula a BUSCAR: "))
# registro = buscarRegistro(ced)
# print(registro)

# print(misDatos['empleados'])
# print()
# ced = str(input("Digite la Cédula del a BORRAR: "))
# borrarRegistro(ced)
# print(misDatos['empleados'])

menu()
