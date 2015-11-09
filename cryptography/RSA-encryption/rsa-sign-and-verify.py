#!/usr/bin/python


from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random


# Randomly generate RSA keys 
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)


# Public Key
public_key = key.publickey()


# Plaintext
plaintext = 'Attack at Dawn!!!'




# Signed message in Hash form
hash = SHA256.new(plaintext).digest()
print hash


# Signature of the hash
signature = key.sign(hash, '')
print signature


# Verify message Hash siganture by returning True or False
print public_key.verify(hash, signature)


