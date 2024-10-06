import random
import string

def get_random_string(size=6):
    letters = string.ascii_letters + string.digits
    return "".join(random.choice(letters) for _ in range(size))