import re


def is_valid_us_currency(s):
    pattern = r'^\d{1,3}(,\d{3})*\.\d{2}$'
    return bool(re.fullmatch(pattern, s))


def is_free(amount):
    return amount == 0.00
