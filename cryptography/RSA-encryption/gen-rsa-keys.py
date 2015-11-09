#!/usr/bin/python


#
# Yuri Medvinsky
# Date: 11-05-2015
# Info: Randomly generate Public and Private keys in PEM format 
#       Save Public key to  key.pub
#       Save Private key to key.priv
#


from Crypto import Random
from Crypto.PublicKey import RSA


random_generator = Random.new().read		# Generate random string
key = RSA.generate(1024, random_generator)	# Generate public and private keys
print key
print key.exportKey('PEM')


pub_key = key.publickey()
print pub_key.exportKey('PEM')



# create private key file
f = open ('key.priv', 'w')
f.write(key.exportKey('PEM'))
f.close()


# create public key file
f = open ('key.pub', 'w')
f.write(pub_key.exportKey('PEM'))
f.close()
