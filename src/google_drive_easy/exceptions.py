class GoogleDriveError(Exception):
    """
    Base exception.
    """


class UploadError(GoogleDriveError):
    """
    Unable to upload the file.
    """


class DeleteError(GoogleDriveError):
    """
    Unable to delete the file.
    """


class ShareError(GoogleDriveError):
    """
    Unable to share the file.
    """
