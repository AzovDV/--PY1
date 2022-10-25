import random
import string


def get_random_password() -> str:
    return ''.join(random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, 8))


print(get_random_password())
