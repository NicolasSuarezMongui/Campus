import os
import json

def message(msg: str) -> None:
    input(f"{msg}\nPresion cualquier tecla para continuar...")

def openFile():
    with open('manuales.json','r') as file:
        data = json.load(file)
    return data

def updateFile(data):
    with open('manuales.json','w', encoding='utf-8') as file:
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

def validarTema(data,lenguaje):
    temas = [tema for tema in data["manuales"][lenguaje]["temas"]]
    titulo = stringValidate("titulo")
    while titulo in temas:
        message("Ese tema ya existe")
    return titulo

# Auxiliar funcionts

def volver():
    mainMenu()

# Create functions

def menuCrear():
    crearOptions = ["Crear Manual","Crear Tema","Volver","Salir"]
    crearFunctions = {1:crearManual,2:crearTema,3:volver}
    menu(crearOptions,crearFunctions,"CREAR")

def crearManual():
    data = openFile()
    os.system("clear")
    lenguaje = stringValidate("Lenguaje").capitalize()
    manuales = [lenguaje for lenguaje,temas in data["manuales"].items()]
    while lenguaje in manuales:
        message("Lenguaje ya existe")
        lenguaje = stringValidate("Lenguaje").capitalize()
    autor = stringValidate("Autor")
    paginas = readInt("paginas")
    data["manuales"][lenguaje]={"autor":autor,"paginas":str(paginas)}
    updateFile(data)
    message("Manual creado con exito")

def crearTema():
    data = openFile()
    os.system("clear")
    lenguaje = opcionLenguajes(data)
    nuevoTema = stringValidate("Tema").capitalize()
    if "temas" in data["manuales"][lenguaje]:
        temas = [tema for tema in data["manuales"][lenguaje]["temas"]]
        while nuevoTema in temas:
            message("Tema ya existe")
            nuevoTema = stringValidate("Tema").capitalize()
    opClas = opcionCalificacion()
    if "temas" in data["manuales"][lenguaje]:
        data["manuales"][lenguaje]["temas"].append({"titulo":nuevoTema,"clasificacion":opClas})
    else:
        data["manuales"][lenguaje]["temas"]=[{"titulo":nuevoTema,"clasificacion":opClas}]
    updateFile(data)
    message("Tema creado con exito")

# Modify functions

def menuModificar():
    crearOptions = ["Modificar Manual","Modificar Tema","Volver","Salir"]
    crearFunctions = {1:modificarManual,2:modificarTema,3:volver}
    menu(crearOptions,crearFunctions,"MODIFICAR")

def modificarManual():
    data = openFile()
    os.system("clear")
    lenguaje = opcionLenguajes(data) 
    opcionesModificar = ["autor","paginas","cancelar"]
    for i,opcion in enumerate(opcionesModificar):
        print(f"{i+1:>6}. {opcion}")
    opMod = rangeValidator(1,len(opcionesModificar),"Opcion")
    match opMod:
        case 1:
            autor = stringValidate("Autor")
            data["manuales"][lenguaje]["autor"]=autor
        case 2:
            paginas = readInt("paginas")
            data["manuales"][lenguaje]["paginas"]=str(paginas)
        case 3:
            menuModificar()
    if opMod!=3:
        updateFile(data)
        message("Modificacion Realizada Correctamente")

def modificarTema():
    data = openFile()
    os.system("clear")
    lenguaje = opcionLenguajes(data)
    if "temas" in data["manuales"][lenguaje]: 
        mTema = opcionTemas(data,lenguaje)
        opcionesModificar = ["titulo","clasificacion","cancelar"]
        for i,opcion in enumerate(opcionesModificar):
            print(f"{i+1:>6}. {opcion}")
        opMod = rangeValidator(1,len(opcionesModificar),"Opcion")
        match opMod:
            case 1:
                titulo = validarTema(data, lenguaje)
                data["manuales"][lenguaje]["temas"][mTema]["titulo"]=titulo
            case 2:
                opClas = opcionCalificacion()
                data["manuales"][lenguaje]["temas"][mTema]["clasificacion"]=opClas
            case 3:
                return menuModificar()
        if opMod!=3:
            updateFile(data)
            message("Modificacion Realizada Correctamente")
    else:
        message("Primero debes crear un tema")
        return menuCrear()

# List Functions

def menuListar():
    listarOptions = ["Listar Manuales","Listar Temas","Volver","Salir"]
    listarFunctions = {1:listarManuales,2:listarTemas,3:volver}
    menu(listarOptions,listarFunctions,"MODIFICAR")

def listarManuales():
    data = openFile()
    os.system("clear")
    print("{:=^68}".format(f"LISTADO DE MANUALES"))
    manuales:dict = data["manuales"]
    print(" {:^6}|{:^20}|{:^30}|{:^7}|".format("","Lenguaje","Autor","#Pg"))
    print(" {}|{}|{}|{}|".format("-"*6,"-"*20,"-"*30,"-"*7))
    for i, lenguaje in enumerate(manuales.keys()):
        print("|{:^6}|{:^20}|{:^30}|{:^7}|".format(str(i+1) if (i+1)>=10 else "0"+str(i+1),lenguaje,manuales[lenguaje]["autor"],manuales[lenguaje]["paginas"]))
    print("="*68)
    message("")

def listarTemas():
    data = openFile()
    os.system("clear")
    print("{:=^56}".format(f"LISTADO DE TEMAS"))
    manuales:dict = data["manuales"]
    idx=1
    print(" {:^6}|{:^20}|{:^5}|{:^20}|".format("","Titulo","Cls","Lenguaje"))
    print(" {}|{}|{}|{}|".format("-"*6,"-"*20,"-"*5,"-"*20))
    for k,v in manuales.items():
        if "temas" in v:
            for tema in v["temas"]:
                print("|{:^6}|{:^20}|{:^5}|{:^20}|".format(str(idx) if idx>=10 else "0"+str(idx),tema["titulo"],str(tema["clasificacion"]),k))
                idx+=1
    print("="*56)
    message("")

def opcionLenguajes(data:dict) -> str:
    print("{:=^40}".format(f"LENGUAJES"))
    manuales = [lenguaje for lenguaje,temas in data["manuales"].items()]
    for i,lenguaje in enumerate(manuales):
        print(f"{i+1:>6}. {lenguaje}")
    print("="*40)
    op = rangeValidator(1,len(manuales),"Lenguaje")
    return manuales[op-1]

def opcionTemas(data:dict,lenguaje:str) -> int:
    print("{:=^40}".format(f"TEMAS"))
    temas = [tema for tema in data["manuales"][lenguaje]["temas"]]
    for i,tema in enumerate(temas):
        print(f"{i+1:>6}. {tema['titulo']}")
    print("="*40)        
    op = rangeValidator(1,len(temas),"Tema")
    return op-1

def opcionCalificacion() -> int:
    print("{:=^40}".format(f"CLASIFICACION"))
    clasificacion=["Básicos","Intermedios","Avanzados"]
    for i,clasTema in enumerate(clasificacion):
        print(f"{i+1:>6}. {clasTema}")
    print("="*40)
    op = rangeValidator(1,len(clasificacion),"Clasificacion")
    return op
# Delete Functions

def menuEliminar():
    eliminarOptions = ["Eliminar Manual","Eliminar Tema","Volver","Salir"]
    eliminarFunctions = {1:eliminarManual,2:eliminarTema,3:volver}
    menu(eliminarOptions,eliminarFunctions,"MODIFICAR")

def eliminarManual():
    data:dict = openFile()
    os.system("clear")
    lenguaje = opcionLenguajes(data)
    del data["manuales"][lenguaje]
    updateFile(data)
    message("Manual eliminado con exito")

def eliminarTema():
    data = openFile()
    os.system("clear")
    lenguaje = opcionLenguajes(data)
    if "temas" in data["manuales"][lenguaje]:
        opTema = opcionTemas(data,lenguaje)
        data["manuales"][lenguaje]["temas"].pop(opTema-1)
        if len(data["manuales"][lenguaje]["temas"])==0:
            data["manuales"][lenguaje].pop("temas")
        updateFile(data)
        message("Tema eliminado con exito")
    else:
        message("Primero debes crear un tema")
        return menuCrear()

# Create .txt

def generarTXT():
    data = openFile()
    res=""
    for lenguaje in data["manuales"].keys():
        c1,c2,c3=0,0,0
        res+=f"Manual {lenguaje}:\n"
        if "temas" in data["manuales"][lenguaje]:
            for tema in data["manuales"][lenguaje]["temas"]:
                if tema["clasificacion"]==1:
                    c1+=1
                if tema["clasificacion"]==2:
                    c2+=1
                if tema["clasificacion"]==3:
                    c3+=1
        res+=f"\tTemas Básicos: {c1}\n\tTemas Intermedios: {c2}\n\tTemas Avanzados: {c3}\n"
    with open("datos.txt","w",encoding="utf-8") as file:
        file.write(res)
    message("Archivo Generado Con Exito")

def menu(options:list, functions:dict, title:str):
    os.system("clear")
    print("{:=^40}".format(f"MENU {title}"))
    for i,option in enumerate(options):
        print(f"{i+1:>6}. {option}")
    print("="*40)
    op = rangeValidator(1,len(options),"Opción")
    if op == len(options):
        print("\nFin del programa\n")
        quit()
    functions[op]()
    menu(options,functions,title)


def mainMenu():
    mainOptions = ["Crear","Modificar","Eliminar","Listar","Generar informe de datos.txt","Salir"]
    mainFunctions = {1:menuCrear,2:menuModificar,3:menuEliminar,4:menuListar,5:generarTXT}
    menu(mainOptions,mainFunctions,"PRINCIPAL")

mainMenu()