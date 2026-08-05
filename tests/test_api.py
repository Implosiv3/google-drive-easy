import pytest


@pytest.mark.additional
def test_file():
    """
    Upload a file, get the shareable link and
    delete it.
    """
    from google_drive_easy import GoogleDrive
    from google_drive_easy.utils import shareable_link_to_direct_file_link
    from google_auth_easy import GoogleAuth
    from google_auth_easy.config import GoogleAuthConfig
    from google_auth_easy.scopes import Scope

    auth = GoogleAuth(
        GoogleAuthConfig(
            client_secret_file = 'client_secret.json',
        )
    )

    auth.authenticate(
        Scope.DRIVE,
    )

    drive = GoogleDrive(auth)

    file = drive.upload_file('test_video.mp4')

    print('File uploaded')
    print(file)

    link = drive.create_share_link(file.id)

    print('File is now shareable')
    print(link)
    print(shareable_link_to_direct_file_link(link))

    drive.delete_file(file.id)

    print('File deleted')




