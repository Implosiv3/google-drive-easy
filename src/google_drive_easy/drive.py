from google_drive_easy.dataclasses.drive_file import DriveFile
from google_drive_easy.managers.share import _ShareManager
from google_drive_easy.managers.upload import _UploadManager
from google_drive_easy.managers.delete import _DeleteManager
from google_auth_easy import GoogleAuth
from googleapiclient.discovery import build
from pathlib import Path
from typing import Union, Callable


class GoogleDrive:
    """
    Main entry point for the Google Drive API.
    """

    def __init__(
        self,
        auth: GoogleAuth,
    ):
        service = build(
            serviceName = 'drive',
            version = 'v3',
            credentials = auth._unwrap_credentials(),
            static_discovery = False,
        )

        self._upload_manager = _UploadManager(service)
        """
        *For internal use only*

        Shortcut to the manager that is able to
        upload files to Google Drive.
        """
        self._delete_manager = _DeleteManager(service)
        """
        *For internal use only*

        Shortcut to the manager that is able to
        delete files in Google Drive.
        """
        self._share = _ShareManager(service)
        """
        *For internal use only*

        Shortcut to the manager that is able to
        share files in Google Drive.
        """

    def upload_file(
        self,
        filename: str,
        parent: Union[str, None] = None,
        progress_callback: Union[Callable[[float], None], None] = None,
    ) -> DriveFile:
        """
        Upload the file with the `filename` given to Google
        Drive, inside the `parent` folder if provided, and
        executing the `progress_callback` during the upload,
        if given.
        
        The `progress_callback` must expect one parameter
        that will be a float between `0.0` and `1.0`, which is
        the progress.
        """
        return self._upload_manager.upload(
            filename = Path(filename),
            parent = parent,
            progress_callback = progress_callback
        )

    def delete_file(
        self,
        file_id: str,
    ) -> None:
        """
        Delete the file with the `file_id` given from
        Google Drive.
        """
        self._delete_manager.delete(file_id)

    def create_share_link(
        self,
        file_id: str,
    ) -> str:
        """
        Create a shareable link (public to everyone as
        a reader) for the file with the `file_id`
        provided.
        """
        return self._share.create_share_link(file_id)