import hashlib
str1 = "study python"
hashdeval=hashlib.sha256(str.encode(str1))
print(hashdeval)
p = hashdeval.hexdigest()
print(p)
print(len(p))
print(p[0:6])

str2 = "Study GIT"
hashdeval2 = hashlib.sha256(str.encode(str2))
print(hashdeval2)
q = hashdeval2.hexdigest()
print(q)
print(len(q))
print(q[0:6])