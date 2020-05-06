import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configurando a Integração
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('Control/static/credential/entregatecnica.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open_by_key('1yIwqAc7yEedIvqYRaFrjv8p4IcJb4OVez4xOPOubqxg')
worksheet = wks.get_worksheet(0)

# Pega todos os dados da tabela:
def Todos():
    list_of_lists = worksheet.get_all_values()
    return list_of_lists

def Status(status):
    linhas = []
    cell_list = worksheet.findall(status)
    for cell in cell_list:
        linhas.append(worksheet.row_values(cell.row))
    return linhas