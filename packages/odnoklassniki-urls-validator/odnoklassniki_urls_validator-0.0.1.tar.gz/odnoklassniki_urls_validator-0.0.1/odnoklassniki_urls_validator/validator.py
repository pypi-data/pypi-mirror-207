from urllib.parse import urlparse

from odnoklassniki_urls_validator.utils import exceptions

MAIN_HOST = 'ok.ru'
POSSIBLE_HOSTS = ['ok.ru', 'www.ok.ru', 'www.odnoklassniki.ru', 'odnoklassniki.ru']


def validate_url(url: str) -> str:
    """
    Validate Odnoklassniki URL

    Parameters:
        url (``str``):
            Url to validate

    Returns:
        :obj:`str`: validated URL

    Raises:
        CantFindHostnameError:
            Can't find URL's hostname.

        HostNotInPossibleHostsError:
            URL's host not in possible hosts.
    """
    if url.startswith('https://') or url.startswith('http://'):
        parsed_url = urlparse(url=url.replace('http://', 'https://'))
    else:
        parsed_url = urlparse(url=url)
        if parsed_url.scheme:
            raise exceptions.InvalidSchemeError(url=url)

        parsed_url = urlparse(url=f'https://{url}')

    if parsed_url.hostname not in POSSIBLE_HOSTS:
        raise exceptions.HostNotInPossibleHostsError(url=url, possible_hosts=POSSIBLE_HOSTS)

    return f'https://{MAIN_HOST}{parsed_url.path}'.strip().strip('/')
