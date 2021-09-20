from itertools import product
import hashlib

def crack(hash):
    try_hash = ""
    iter_object = product(range(10), repeat=5)

    while try_hash != hash:
        strng = "".join([str(x) for x in next(iter_object)])
        try_hash = hashlib.md5(strng.encode('utf-8')).hexdigest()

    try:
        return strng

    except ValueError:
        return "No hash found"

print(crack("827ccb0eea8a706c4c34a16891f84e7b"))


