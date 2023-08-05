# dzen_urls_validator

Library for validating [Dzen](https://dzen.ru) urls and brings them to one standart.

# How method works?

1. Add prefix "https://"
2. Change all hostnames to "dzen.ru"


# Examples

```python
from dzen_urls_validator import validate_url

validated_url = validate_url(url='dzen.ru/id/5ce671035b6e3000b303d27a/')
# >> https://dzen.ru/id/5ce671035b6e3000b303d27a

validated_url = validate_url(url='zen.yandex.ru/id/5ce671035b6e3000b303d27a')
# >> https://dzen.ru/id/5ce671035b6e3000b303d27a
```


# Installing

```commandline
pip3 install dzen_urls_validator
```
