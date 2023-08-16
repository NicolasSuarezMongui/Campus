def message(msg: str) -> None:
    input(f"{msg}\nPresion cualquier tecla para continuar...")


def readInt(msg: str) -> int:
    try:
        return int(input(f"{msg}? "))
    except ValueError:
        message(f"Error. el dato ingresado debe ser un entero.")
        return readInt(msg)
    
def readString(msg: str) -> str:
    try:
        return input(f"{msg}? ")
    except ValueError:
        message(f"Error. el dato ingresado debe ser una cadena de texto.")
        return readString(msg)
    
def stringValidate(msg: str) -> str:
    data = readString(msg)
    while(data.strip()==''):
        message("El dato ingresado no puede estar vacio")
        data = readString(msg)
    return data
    
def rangeValidator(a: int, b: int, msg: str) -> int:
    option = readInt(msg)
    if option >= a and option <= b:
        return option
    else:
        message("Fuera de rango.")
        return rangeValidator(a, b, msg)
    
"""Simulacro CICLO 1

Elabore un programa Python para gestionar el CRUD del archivo de datos PetShopping.json con las siguientes funcionalidades:

    
1. Mostrar en pantalla todas las mascotas a la venta visualizando: Tipo, Raza, Precio y Servicios

    
2. Crear Nueva mascota con la posibilidad de múltiples ítems de Servicio

    
3. Mostrar los datos de Mascotas por Tipo elegido visualizando: Raza, Precio y Servicios

    
4. Actualizar los datos de una mascota consultada por índice (Mostrar el listado total y elegir por     índice)

    
5. Eliminar una mascota de la tienda (Mostrar el listado total y elegir por índice)"""

import json
import os
from tabulate import tabulate

types=['Perro','Chanchito','Gato','Conejo']
services={'hotel':20_000,'baño':15_000,'juguetes':45_000,'vacunas':15_000,'alimento':25_000}
sizes=["Pequeño",'Mediano','grande']

def openFile():
    with open('PetShopping.json') as file:
        data = json.load(file)
    return data

def updateFile(newData:dict):
    with open('PetShopping.json', 'w', encoding='utf-8') as newFile:
        json.dump(newData, newFile, indent=4)

def show():
    data = openFile()
    print(tabulate([s.values() for s in data['pets']],data['pets'][0].keys(),tablefmt='fancy_grid'))
    message('')

def create():
    data=openFile()
    for i,type in enumerate(types):
        print(f'{str(i+1):>6}. {type}')
    oT = rangeValidator(1,len(types),'Tipo')
    os.system('clear')
    breed = readString('Raza')
    os.system('clear')
    for i,size in enumerate(sizes):
        print(f'{str(i+1):>6}. {size}')
    oSize = rangeValidator(1,len(sizes),'Talla')
    os.system('clear')
    listServices=[]
    price=0
    while True:
        for i,service in enumerate(services.keys()):
            print(f'{str(i+1):>6}. {service}')
        oS = rangeValidator(1,len(services),'Servicio')
        aux = list(services.keys())
        listServices.append(aux[oS-1])
        price += services[aux[oS-1]]
        op = rangeValidator(1,2,'Desea agregar otro servicio\n1.Si 2.No')
        if op==2:
            break
    data['pets'].append({"tipo":types[oT-1],"raza":breed,"talla":sizes[oSize-1],"precio":price,"servicios":listServices})
    updateFile(data)
    message("")
        
def find():
    data=openFile()
    for i,type in enumerate(types):
        print(f'{str(i+1):>6}. {type}')
    oT = rangeValidator(1,len(types),'Tipo')
    print(tabulate([s.values() for s in data['pets'] if s['tipo']==types[oT-1]],data['pets'][0].keys(),tablefmt='fancy_grid'))
    message("")

def update():
    show()
    data=openFile()
    opU = rangeValidator(1,len(data['pets']), f'Indice a actualizar')
    os.system('clear')
    breed = readString('Raza')
    os.system('clear')
    for i,size in enumerate(sizes):
        print(f'{str(i+1):>6}. {size}')
    oSize = rangeValidator(1,len(sizes),'Talla')
    os.system('clear')
    listServices=[]
    price=0
    while True:
        for i,service in enumerate(services.keys()):
            print(f'{str(i+1):>6}. {service}')
        oS = rangeValidator(1,len(services),'Servicio')
        aux = list(services.keys())
        listServices.append(aux[oS-1])
        price += services[aux[oS-1]]
        op = rangeValidator(1,2,'Desea agregar otro servicio\n1.Si 2.No')
        if op==2:
            break
    data['pets'][opU-1]['raza'] = breed
    data['pets'][opU-1]['talla'] = sizes[oSize-1]
    data['pets'][opU-1]['precio'] = price
    data['pets'][opU-1]['servicios'] = listServices
    updateFile(data)
    message("")

def delete():
    data=openFile()
    show()
    opDel = rangeValidator(1,len(data['pets']),'Indice a borrar')
    data['pets'].pop(opDel-1)
    updateFile(data)

def menu():
    os.system("clear")
    print("{:^60}".format("MENU PRINCIPAL"))
    options = ["Mostrar todas las mascotas","Crear nueva mascota", "Mostrar mascotas por tipo", "Actualizar los datos de una mascota", "Eliminar mascota","Salir"]
    for i, option in enumerate(options):
        print(f"{str(i+1):>6}. {option}")
    
    option = rangeValidator(1, 6, "opcion -> ")

    if option==6:
        return print("\nFin del programa\n")
    
    switch = {1: show, 2: create, 3: find, 4: update, 5: delete}
    switch[option]()
    menu()

menu()
list