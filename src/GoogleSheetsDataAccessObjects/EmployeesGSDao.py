from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SPREAD_SHEET_ID = '1aHL76qIxa5p-ZKw4xEwAwE5WnRErDaSLStbBojCxQYQ'
SHEET_NAME = 'Employees'

def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREAD_SHEET_ID, range=SHEET_NAME).execute()
        values = result.get('values', [])
        if not values:
            print('No data found')
            return
        print('Data founded')
        for row in values:
            print('{} {}'.format(row[0], row[1]))

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()