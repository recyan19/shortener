import random
import string
from shorter.models import Url


def get_short_code_for_url():
    length = 6
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase

    while True:
        url_id = ''.join(random.choice(chars) for x in range(length))
        try:
            tmp = Url.objects.get(pk=url_id)
        except Url.DoesNotExist:
            return url_id

