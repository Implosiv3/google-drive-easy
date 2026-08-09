"""
Interact with Google Drive, easy.

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
"""
from google_drive_easy.drive import GoogleDrive


__all__ = [
    'GoogleDrive',
]