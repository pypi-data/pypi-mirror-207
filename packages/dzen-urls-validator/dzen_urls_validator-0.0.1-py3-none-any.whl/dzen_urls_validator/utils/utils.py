from typing import List, Optional

import string

ALLOWED_CHARACTERS = string.digits + string.ascii_uppercase + string.ascii_lowercase + '.'


def get_hostname(hostname: str, hostnames: List[str]) -> Optional[str]:
    for prefix in hostnames:
        if hostname.startswith(prefix):
            return prefix
    return None
