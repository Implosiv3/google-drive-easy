# Google Drive with Python, but easy

The easiest way to interact with the Google Drive API to perform the tasks you need.

# Important
If you don't know how to connect with the Google API by using Oauth2, check the `google-auth-easy` dependency and the instructions to connect. You can find the project in Pypi and the code in Github (https://github.com/Implosiv3/google-drive-easy).

# Instructions
1. Go to the Google Developers console: https://console.cloud.google.com.
2. Make sure you have enabled the Google Drive API.


# Usage
```
from google_drive_easy import GoogleDrive
from google_auth_easy import GoogleAuth
from google_auth_easy.config import GoogleAuthConfig
from google_auth_easy.scopes import Scope

# Authenticate in Google
auth = GoogleAuth(
    GoogleAuthConfig(
        client_secret_file = 'client_secret.json',
    )
)

auth.authenticate(
    Scope.DRIVE,
)

# Connect to Google Drive
drive = GoogleDrive(auth)

# Upload file
file = drive.upload_file('test_files/test.txt')

# Share Google Drive resource
link = drive.create_share_link(file.id)

# Delete file
drive.delete_file(file.id)
```