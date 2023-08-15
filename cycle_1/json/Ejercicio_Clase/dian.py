import json
with open('Ahorradores.json') as file:
    data = json.load(file)
newData={'cliente':[]}
[newData['cliente'].append({'consecutivo':1 if len(newData['cliente'])==0 else newData['cliente'][-1]['consecutivo']+1,'numCuenta':info['NumCuenta'],'Saldo':info['Saldo']}) for info in data['cliente'] if info['Saldo']>35_000_000]
with open('Dian.json','w') as newFile:
    json.dump(newData,newFile,indent=4)