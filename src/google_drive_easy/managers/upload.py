from google_drive_easy.exceptions import UploadError
from google_drive_easy.dataclasses.drive_file import DriveFile
from googleapiclient.http import MediaFileUpload
from pathlib import Path
from typing import Union, Callable



class _UploadManager:
    """
    *For internal use only*

    Handle uploading files to Google Drive.
    """

    def __init__(
        self,
        service,
    ):
        self._service = service

    def upload(
        self,
        filename: Path,
        parent: Union[str, None] = None,
        progress_callback: Union[Callable[[float], None], None] = None,
    ) -> DriveFile:
        """
        Upload a file to Google Drive, inside the
        `parent` folder if provided, and executing
        the `progress_callback` during the upload,
        if provided.

        The `progress_callback` must expect one
        parameter that will be a float between `0.0`
        and `1.0`, which is the progress.
        """
        filename = Path(filename)

        if not (
            filename.exists() or
            filename.is_file()
        ):
            raise FileNotFoundError

        media = MediaFileUpload(
            filename = str(filename),
            resumable = True,
        )

        # Build body
        body = {
            'name': filename.name,
        }

        if parent is not None:
            body['parents'] = [parent]

        # Send request
        try:
            request = self._service.files().create(
                body = body,
                media_body = media,
                fields = 'id,name,mimeType,size',
            )
        except Exception as exc:
            raise UploadError() from exc

        response = None

        while response is None:
            status, response = request.next_chunk()

            if (
                status is not None and
                progress_callback is not None
            ):
                # progress is a float between 0.0 and 1.0
                progress_callback(status.progress())

        return DriveFile(
            id = response['id'],
            name = response['name'],
            mime_type = response['mimeType'],
            size = (
                int(response['size'])
                if 'size' in response else
                None
            ),
        )