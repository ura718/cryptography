#!/usr/bin/python

#
# Yuri Medvinsky
# Date: 11-05-2015
# Info: 
#   Use RSA public key to encrypt plaintext message
#	the key is retrieved from key.pub file generated 
#   by another program caled: gen-rsa-keys.py
#


from Crypto.PublicKey import RSA



# Open public key file in PEM format
f = open('key.pub','r')
publickey = RSA.importKey(f.read())




plaintext='Attack at Dawn!!!'



# Encrypt 
encrypted = publickey.encrypt(plaintext, 32)	# Number 32 is a random parameter used by RSA algorithm to encrypt data.
print "encrypted msg: ", encrypted





# Generate file with cipher text
f = open ('encrypted.txt', 'w')
f.write(str(encrypted))
f.close()
