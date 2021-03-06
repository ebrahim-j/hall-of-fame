from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

# try:
#     import argparse
#     flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
# except ImportError:
#     flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'
COHORTS = ['Jan 2017', 'Feb 2017', 'March 2017', 'April 2017', 'May 2017',
           'June 2017', 'June2 2017', 'July 2017', 'August 2017', 'August2 2017']
results = []


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    # if not credentials or credentials.invalid:
    #     flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    #     flow.user_agent = APPLICATION_NAME
    #     if not flags:
    #         credentials = tools.run_flow(flow, store, flags)
    #     else: # Needed only for compatibility with Python 2.6
    #         credentials = tools.run(flow, store)
    #     print('Storing credentials to ' + credential_path)
    return credentials

credentials = get_credentials()
http = credentials.authorize(httplib2.Http())
discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                'version=v4')
service = discovery.build('sheets', 'v4', http=http,
                            discoveryServiceUrl=discoveryUrl)

spreadsheetId = '1RRBsu9-3Pyb_0IepSQ0tfsUvAuHnchY7e867Tsj92hQ'
for cohort in COHORTS:
    cohort_row = []
    rangeName = cohort + '!A5:C'
    cohort_no = cohort + '!A4'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    result2 = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=cohort_no).execute()
    values = result.get('values')
    values.extend(result2.get('values'))

    if not values:
        print('No data found.')
    else:
        for row in values:
            cohort_row.append(row)
    results.append(cohort_row)
    cohort_row = []

def get_emails():
    emails = []
    for cohort in results:
        cohort_no = cohort[-1]
        for fellow in cohort:
            if fellow[0] != cohort_no[0]:
                emails.append([fellow[0], cohort_no[0]])

    return emails

def get_interests():
    interests = []
    for cohort in results:
        for fellow in cohort[:-1]:
            if fellow[1]:
                interests.append(fellow[1])
            else:
                interests.append("Nill")
    return interests

def get_hobbies():
    hobbies = []
    for cohort in results:
        for fellow in cohort[:-1]:
            if fellow[2]:
                hobbies.append(fellow[2])
            else:
                hobbies.append("Nill")
    return hobbies
