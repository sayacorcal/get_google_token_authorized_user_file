import sys
import argparse
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import errors
from googleapiclient.discovery import build

parser = argparse.ArgumentParser()
parser.add_argument("--token", type=str, required=True, help="The token argument")
parser.add_argument("--credential", type=str, required=True, help="The credential argument")
parser.add_argument("--scopes", nargs="+", type=str, help="The scopes argument")
args = parser.parse_args()

token_file = args.token
credentials_file = args.credential
SCOPES = args.scopes
# Print input variables
print("Token: "     ,   token_file)
print("Credential: ",   credentials_file)
print("Scopes: "    ,   SCOPES)

creds = None

# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.

if os.path.exists(token_file):
    creds = Credentials.from_authorized_user_file(token_file, SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
  if creds and creds.expired and creds.refresh_token:
    creds.refresh(Request())
  else:
    flow = InstalledAppFlow.from_client_secrets_file( CLIENT_SECRET , scopes=SCOPES ) # 'credentials.json', SCOPES)
    authorization_url, state = flow.authorization_url(
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type='offline',
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes='true')
    
    creds = flow.run_local_server(port=0)
  # Save the credentials for the next run
  with open(token_file, 'w') as token:
      token.write(creds.to_json())
