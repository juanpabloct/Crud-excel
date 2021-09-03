from openpyxl import load_workbook
import Funciones_globales
hoja='./Libro1.xlsx'
def leer_excel():
    file=load_workbook(hoja)
    page=file['Hoja1']
    rows=page.rows
    datos=[]
    for x, row in enumerate(rows):
        if x==0:
            continue
    record=convert_row_to_dict(row)
leer_excel()