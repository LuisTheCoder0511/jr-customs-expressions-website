import random
import string


def generate(length: int):
    if length < 6:
        print("Length must be at least 6 or greater")
        return None

    value = []
    index = 0
    while index < length:
        characters = string.ascii_letters + string.digits
        random_character = random.choice(characters)
        value.append(random_character)
        index += 1
    return ''.join(value)
