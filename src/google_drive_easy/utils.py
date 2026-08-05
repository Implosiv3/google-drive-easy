from urllib.parse import urlparse


def shareable_link_to_direct_file_link(
    share_link: str,
) -> str:
    """
    Transform a shareable Google Drive link into
    a direct link to the file.

    This is an example of a shareable link:
    - https://drive.google.com/file/d/1DpxGxtqXXXXXXXXXJgon6i9gOvJMBON/view?usp=drive_link

    And this is the corresponding direct link:
    - https://drive.google.com/uc?export=download&id=1DpxGxtqXXXXXXXXXJgon6i9gOvJMBON
    """
    file_id = urlparse(share_link).path.split('/')[3]

    return f'https://drive.google.com/uc?export=download&id={file_id}'