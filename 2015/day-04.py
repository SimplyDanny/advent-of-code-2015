import hashlib

from common import print_results, readline


INPUT = readline(__file__)

def find_suffix(prefix, suffix=0):
    while True:
        md5 = hashlib.md5(str.encode(INPUT + str(suffix)))
        if md5.hexdigest().startswith(prefix):
            return suffix
        suffix += 1

#### Main part.

five = find_suffix('0' * 5)
six = find_suffix('0' * 6, five)

print_results(five, six)
