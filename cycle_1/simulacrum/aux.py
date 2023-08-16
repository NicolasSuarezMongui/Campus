import os
from tabulate import tabulate
students = [{'codigo':'216554','nombre':'Nicolas', 'notas':[4.5,4.5,4.5]}]

def message(msg: str) -> None:
    input(f"{msg}\nPresion cualquier tecla para continuar...")


def readFloat(msg: str) -> float:
    try:
        return float(input(f"{msg}? "))
    except ValueError:
        message(f"Error. el dato ingresado debe ser un entero.")
        return readFloat(msg)
    
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
    
def rangeValidator(a: float, b: float, msg: str) -> float:
    option = readFloat(msg)
    if option >= a and option <= b:
        return option
    else:
        message("Fuera de rango.")
        return rangeValidator(a, b, msg)
    
def strInfo(data:dict) -> None:
    print("{:=^60}".format("INFORMACION ESTUDIANTE"))
    print("|{:^12}|{:^10}|{:^10}|{:^10}|{:^10}|".format("Codigo","Nombre","Nota 1","Nota 2","Nota 3"))
    print("-"*58)
    print("|{:^12}|{:^10}|{:^10}|{:^10}|{:^10}|".format(data['codigo'],data['nombre'],data['notas'][0],data['notas'][1],data['notas'][2]))
    # for k,v in data.items():
    #     print(f"{k}:\t{v}")    

def addStudent():
    code = stringValidate("Codigo")
    name = stringValidate("Nombre")
    grades = []
    for i in range(3):
        grade = rangeValidator(0.0, 5.0, f"Nota {i+1}")
        grades.append(grade)
    student = {'codigo':code,'nombre':name,'notas':grades}
    students.append(student)
    message("")
    

def findStudent():
    code = stringValidate("Codigo")
    res = [student for student in students if student['codigo']==code]
    strInfo(res[0]) if len(res)>0 else message("Estudiante no encontrado")
    message("")
    

def deleteStudent():
    code = stringValidate("Codigo")
    res = [student for student in students if student['codigo']==code]
    strInfo(students.pop(students.index(res[0]))) if len(res)>0 else message("Estudiante no encontrado")     
    message("")

def calculateFinal():
    #print ("No hay usuarios registrados") if len(students)==0 else [student.setdefault('definitiva',sum(student['notas'])/3) for student in students]
    if len(students) == 0:
        message("No hay usuarios registrados.")
    else:
        [student.setdefault('definitiva',sum(student['notas'])/3) for student in students]
        message("Definitivas generadas con exito.")

def updateStudent():
    pass

def listStudent():
    if "definitiva" in students[0]:
        print(tabulate([s.values() for s in students],students[0].keys(),tablefmt='fancy_grid'))
        print(f"Promedio: {sum(s['definitiva'] for s in students)/len(students)}")
        message("")
    else:
        message("No se han generado las definitivas.")

def menu():
    os.system("clear")
    print("{:^60}".format("MENU PRINCIPAL"))
    options = ["Agregar un nuevo registro","Buscar un Estudiante", "Actualizar datos del Estudiante", "Borrar un estudiante", "Calcular notas definitivas", "Listar estudiantes con notas definitivas y ver promedio general","Salir"]
    for i, option in enumerate(options):
        print(f"{str(i+1):>6}. {option}")
    
    option = rangeValidator(1, 7, "opcion -> ")

    if option==7:
        return print("\nFin del programa\n")
    
    switch = {1: addStudent, 2: findStudent, 3: updateStudent, 4: deleteStudent, 5: calculateFinal, 6: listStudent}
    switch[option]()
    menu()


menu()
