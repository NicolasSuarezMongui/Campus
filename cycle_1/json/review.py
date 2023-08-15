import json
with open('datos.txt','r') as file:
    data = file.readlines()

dataJSON = {'Vendedores':[]}

# Optimization
#[dataJSON['Vendedores'].append({'Apellido':res.replace('\n','').split(', ')[0],'Id':res.replace('\n','').split(', ')[1],'Ventas':[int(elem) for elem in res.replace('\n','').split(', ')[2:]]}) for res in data[1:]]

for d in data[1:]:
    res = d.replace('\n','').split(', ')
    dataJSON['Vendedores'].append({'Apellido':res[0],'Id':res[1],'Ventas':[int(elem) for elem in res[2:]]})

with open('datos.json','w') as newFile:
    json.dump(dataJSON,newFile,indent=4)