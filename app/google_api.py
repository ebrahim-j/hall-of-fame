from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

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
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
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
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

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
        for fellow in cohort:
            emails.append(fellow[0])
    return emails

def get_interests():
    interests = []
    for cohort in results:
        for fellow in cohort:
            interests.append(fellow[1])
    return interests

def get_hobbies():
    hobbies = []
    for cohort in results:
        for fellow in cohort:
            hobbies.append(fellow[1])
    return hobbies

print(get_hobbies())