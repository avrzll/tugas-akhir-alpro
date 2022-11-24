import random
import string

def random_id():
    random_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(7))
    return random_id