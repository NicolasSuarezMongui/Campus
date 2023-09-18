import flet as ft
import json

def openFile():
    with open('./PaísCiudad.json', 'r') as file:
        data = json.load(file)
    return data

def rowsData():
    data = openFile()
    res=[]
    for dpt in data['Departamentos']:
        res.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(dpt['idDep'])),
                    ft.DataCell(ft.Text(dpt['nomDepartamento'])),
                ]
            )
        )
    print(res)
    return res

def main(page: ft.Page):
    page.add(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Name"))
            ],
            rows=rowsData()
        ),
    )

ft.app(target=main)