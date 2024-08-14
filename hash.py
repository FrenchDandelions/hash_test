from passlib.hash import argon2

# generate new salt, hash password
h = argon2.hash("password")
print(h)
# '$argon2i$v=19$m=512,t=2,p=2$aI2R0hpDyLm3ltLa+1/rvQ$LqPKjd6n8yniKtAithoR7A'

# the same, but with an explicit number of rounds
argon2.using(rounds=4).hash("password")
# '$argon2i$v=19$m=512,t=4,p=2$eM+ZMyYkpDRGaI3xXmuNcQ$c5DeJg3eb5dskVt1mDdxfw'

# verify password
print(argon2.verify("password", h))
print(argon2.verify("passwordd", h))
print(argon2.verify("passwor", h))
print(argon2.verify("passworc", h))
print(argon2.verify("passwore", h))
print(argon2.verify("wrong", h))