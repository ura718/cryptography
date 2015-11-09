#!/usr/bin/python

#
# Info: 
#   Use RSA private key to decrypt plaintext message
#	the key is retrieved from key.priv file generated 
#   by another program called: gen-rsa-keys.py
#

import ast
from Crypto.PublicKey import RSA



# Open private key file in PEM format
f = open('key.priv','r')
key = RSA.importKey(f.read())





# Open file with ciphertext
f = open('encrypted.txt','r')
ciphertext = f.read()





# Decrypt
decrypted = key.decrypt(ast.literal_eval(str(ciphertext)))
print "encrypted msg: ", decrypted




# Generate file with cipher text
f = open ('decrypted.txt', 'w')
f.write(str(decrypted))
f.close()
