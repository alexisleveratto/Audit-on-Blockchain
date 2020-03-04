import random


def get_random_string(
    length=24,
    allowed_chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
):
    return "".join(random.choice(allowed_chars) for i in range(length))
