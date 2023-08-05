# youtube_urls_validator

Library for validating YouTube urls and brings them to one standart.

# How method works?

1. Add prefix "https://"
2. Change all hostnames to "www.youtube.com"


# Examples

```python
from youtube_urls_validator import validate_url

validated_url = validate_url(url='youtube.com/youtube/')
# >> https://youtube.com/youtube

validated_url = validate_url(url='youtu.be/youtube')
# >> https://youtube.com/youtube
```


# Installing

```commandline
pip3 install youtube_urls_validator
```
