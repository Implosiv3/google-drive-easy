from google_drive_easy._types import DriveService
from google_drive_easy.exceptions import ShareError


class ShareManager:
    """
    Handles Google Drive file sharing.
    """

    def __init__(
        self,
        service: DriveService,
    ):
        self._service = service

    def create_share_link(
        self,
        file_id: str,
    ) -> str:
        """
        Make a file publicly readable and return its
        web view URL. Anyone will be able to read it.
        """
        try:
            self._service.permissions().create(
                fileId = file_id,
                # TODO: Make this customizable
                body = {
                    'type': 'anyone',
                    'role': 'reader',
                },
            ).execute()
        except Exception as exc:
            raise ShareError() from exc

        metadata = self._service.files().get(
            fileId = file_id,
            fields = 'webViewLink,webContentLink'
        ).execute()

        return metadata['webViewLink']