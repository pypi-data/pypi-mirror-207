
from django.core.validators import RegexValidator

__all__ = ['record_identifier_validator', 'record_keygen', 'RECORD_KEY_LENGTH', 'RECORD_KEY_ALPHABET']

"""

H  [month, 1 letter: UBHAMJLGSCVD]
23 [year, three digits]

   4 out of 32 "digits": [ABCDEFGHJKLMNPRSTUVWXYZ123456789]
   32^4 = 2^20 20 bits

XXXX

5 out of 30 digits: [BCDFGHJKLMNPRSTVWXYZ0123456789]

"""

RECORD_KEY_ALPHABET = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
                       'N', 'P', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z',
                       '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

RECORD_KEY_LENGTH = 7


def random_record_key_letter(random):
    return RECORD_KEY_ALPHABET[random.randint(1, len(RECORD_KEY_ALPHABET)) - 1]


def record_keygen():

    import random
    from .models import Record

    for t in range(100):

        key = []

        for i in range(RECORD_KEY_LENGTH):
            key.append(random_record_key_letter(random))

        key = "".join(key)

        try:
            Record.objects.all().get(pk=key)
        except Record.DoesNotExist:
            return key

    raise RuntimeError("Couldn't create record key")


record_identifier_validator = \
    RegexValidator(
       f'^[{"".join(RECORD_KEY_ALPHABET)}]{{{RECORD_KEY_LENGTH}}}$',
       code='invalid_identifier',
       message=f'A valid identifier consists of six letters or digits from the set {" ".join(RECORD_KEY_ALPHABET)}.')
