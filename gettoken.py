import subprocess

# Define input arguments
token = "token.json"
credential = "credentials.json"
scopes = ["https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/spreadsheets.readonly"]

# Run other_code.py and pass input arguments
subprocess.run(["python", "get_google_token_authorized_user_file.py", "--token", token, "--credential", credential, "--scopes"] + scopes)
