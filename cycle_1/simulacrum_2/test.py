import json
with open("./PaísCiudad.json","r") as file:
    data = json.load(file)

#print(data["Departamentos"])

print(data["Departamentos"][1]["Ciudades"][0]["imagen"])