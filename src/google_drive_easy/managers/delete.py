from google_drive_easy._types import DriveService
from google_drive_easy.exceptions import DeleteError


class _DeleteManager:
    """
    *For internal use only*
    
    Handle deleting files in Google Drive.
    """

    def __init__(
        self,
        service: DriveService,
    ):
        self._service: DriveService = service

    def delete(
        self,
        file_id: str,
    ) -> None:
        """
        Delete a file from Google Drive.
        """
        try:
            self._service.files().delete(
                fileId = file_id,
            ).execute()
        except Exception as exc:
            raise DeleteError() from exc
        