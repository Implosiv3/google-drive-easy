from google_drive_easy.share import ShareManager
from google_drive_easy.upload import UploadManager
from google_drive_easy.delete import DeleteManager
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

        self._upload = UploadManager(service)
        self._delete = DeleteManager(service)
        self._share = ShareManager(service)

    def upload_file(
        self,
        filename: str,
        parent: Union[str, None] = None,
        progress_callback: Union[Callable[[float], None], None] = None,
    ):
        return self._upload.upload(
            filename = Path(filename),
            parent = parent,
            progress_callback = progress_callback
        )

    def delete_file(
        self,
        file_id: str,
    ) -> None:
        self._delete.delete(file_id)

    def create_share_link(
        self,
        file_id: str,
    ) -> str:
        return self._share.create_share_link(file_id)