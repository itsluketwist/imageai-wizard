from urllib.error import URLError
from urllib.request import urlopen


def is_string_url(string: str) -> bool:
    """
    Quickly check if a provided string is a valid URL or not.

    Parameters
    ----------
    string: str
        The string that should be checked if it's a url.

    Returns
    -------
    bool
        True if the string is a url, False otherwise..
    """
    try:
        urlopen(string)
        return True
    except URLError:
        return False
