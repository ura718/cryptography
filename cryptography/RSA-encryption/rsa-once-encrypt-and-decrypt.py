#!/usr/bin/python


#
# Yuri Medvinsky
# Date: 11-05-2015
# Info: Randomly generate RSA public and private keys and perform encryption and decryption
#




import Crypto
import ast
from Crypto.PublicKey import RSA
from Crypto import Random




random_generator = Random.new().read		# Generate random string
key = RSA.generate(1024, random_generator)	# Generate public and private key
publickey = key.publickey() 				# Grab public key to be exported for exchange



plaintext='Attack at Dawn!'



# Encrypt message
encrypted = publickey.encrypt(plaintext, 32)	# Uses public key to encrypt
print "encrypted message: \n", encrypted




# Generate a file with cipher text
#f = open ('encryption.txt', 'w')
#f.write(str(encrypted)) 
#f.close()





# Decrypt message

# Read file content
#f = open('encryption.txt', 'r')
#message = f.read()




print
decrypted = key.decrypt(ast.literal_eval(str(encrypted)))	# Uses private key to decrypt
print "Decrypted message:  \n" + decrypted




# Generate file with decrypted message
#f = open ('encryption.txt', 'w')
#f.write(str(message))
#f.write(str(decrypted))
#f.close()



