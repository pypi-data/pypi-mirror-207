from urllib.parse import urlparse

from dzen_urls_validator.utils import exceptions, utils

MAIN_HOST = 'dzen.ru'
POSSIBLE_HOSTS = ['dzen.ru', 'zen.yandex.ru']


def validate_url(url: str) -> str:
    """
    Validate Dzen URL

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
        parsed_url = urlparse(url=url)
    else:
        parsed_url = urlparse(url=f'https://{url}')

    if parsed_url.hostname is None:
        raise exceptions.CantFindHostnameError(url=url)

    hostname = utils.get_hostname(hostname=parsed_url.hostname, hostnames=POSSIBLE_HOSTS)
    if hostname is None:
        raise exceptions.HostNotInPossibleHostsError(url=url, possible_hosts=POSSIBLE_HOSTS)

    return f'https://{MAIN_HOST}{parsed_url.path}'.strip('/').strip()
