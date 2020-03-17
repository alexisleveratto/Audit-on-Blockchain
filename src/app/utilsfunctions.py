import random

ALLOWED_EXTENSIONS = set(["pdf", "zip", "xlsx"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def get_random_string(
    length=24,
    allowed_chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
):
    return "".join(random.choice(allowed_chars) for i in range(length))
