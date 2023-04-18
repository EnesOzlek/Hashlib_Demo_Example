import hashlib

print("Welcome mD5 hash encrypted")


hash = input("user hash input : ")
hash = hash.encode("utf-8")
new_hash = hashlib.md5()
new_hash.update(hash)
print(new_hash.digest())