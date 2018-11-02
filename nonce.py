import random
import string
import hashlib
from random import *
min_char = 8
max_char = 32

starthash = "teambtcc0000000848f780f4da9809fdf2b9301e9836c90422d9cd7ee055f6203012b306"


def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
    
allchar = string.ascii_letters + string.digits
nonce = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
finalhash = starthash+nonce
hasho = encrypt_string(finalhash)

while True:
    allchar = string.ascii_letters + string.digits
    nonce = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    finalhash = starthash+nonce
    hasho = encrypt_string(finalhash)
    if hasho.startswith("0000000"):
        break
print nonce
