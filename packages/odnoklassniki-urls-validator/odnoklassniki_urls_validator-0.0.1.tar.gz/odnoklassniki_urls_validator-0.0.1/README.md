# odnoklassniki_urls_validator

Library for validating [Odnoklasnsiki](https://ok.ru) urls and brings them to one standart.

# How method works?

1. Add prefix "https://"
2. Change all hostnames to "ok.ru"


# Examples

```python
from odnoklassniki_urls_validator import validate_url

validated_url = validate_url(url='www.ok.ru/group/50582132228315/')
# >> https://ok.ru/group/50582132228315

validated_url = validate_url(url='http://ok.ru/group/50582132228315')
# >> https://ok.ru/group/50582132228315
```


# Installing

```commandline
pip3 install odnoklassniki_urls_validator
```
