import validators


def is_valid(url):
    return validators.url(url)
