import json
import os

def message(msg: str) -> None:
    input(f"{msg}\nPresion cualquier tecla para continuar...")

def openFile():
    with open('info.json','r') as file:
        data = json.load(file)
    return data

def updateFile(data):
    with open('info.json','w', encoding='utf-8') as file:
        json.dump(data,file, indent=4)

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

def findUser(userId:str) -> []:
    data = openFile()
    for i, user in enumerate(data['students']):
        if user['id']==userId:
            return 'students',i
        
    for i, user in enumerate(data['teachers']):
        if user['id']==userId:
            return 'teachers',i

def menu(options:list, role:str) -> int:
    os.system('clear')
    print(f"{role:^60}")
    for i, option in enumerate(options):
        print(f"{str(i+1):>6}. {option}")
    option = rangeValidator(1,len(options),"Option")
    if option==len(options):
        return print("{:*^60}".format("Fin del programa"))
    return option
    

def login():
    data = openFile()
    user = readString("Username")
    while findUser(user)==None:
        message("invalid user")
        user=readString("Username")
    client,i = findUser(user)
    password = readString("Password")
    while data[client][i]['password'] != password:
        message("invalid password")
        password = readString("Password")
    return user


def main():
    user = login()
    client, pos = findUser(user)
    optionsTeachers = ['Enter Student','Modified Student','Find Student','Delete Student','Exit']
    op = menu(optionsTeachers,client)
    return op
#menu(["Mostrar todas las mascotas","Crear nueva mascota", "Mostrar mascotas por tipo", "Actualizar los datos de una mascota", "Eliminar mascota","Salir"], "Principal")

if __name__ == '__main__':
    main()
    