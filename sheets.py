from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'tareassd-50692aacbcad.json'
SPREADSHEET_ID = '1UmQsV7uib-uS8vN7LS1DxZquCPER6-dSQpIZPV-6jIM'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Debe ser una matriz por eso el doble [[]]
values = [['Prueba!']]
# Llamamos a la api
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range='A1',
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")