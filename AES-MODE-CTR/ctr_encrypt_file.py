#!/usr/bin/python

# Import modules
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter
import binascii
import base64
import os 
import struct


# Important Notes:
# The nonce + counter = 128 bits. Therefore, we first take a random nonce of 64 bits. We then
# take Counter.new() of also 64 bits. And lastly we combine the nonce(64)+counter(64) to get
# 128 bits in total. We then take a 16 byte key which is also 128 bits. 
#
#   key xor (nonce+counter) = cipher.
#   
#
# - In order to decrypt successfully the nonce needs to be the same as the one used to encrypt. 
#
# - But for encryption to be secure you must generate a random nonce for every new encryption.
#





# Get random 8 bytes which equals to 64 bits
#nonce = Random.new().read(8)


# Static nonce - Use just for testing purposes
nonce = '12345678'


# The key is 16 bytes which equals to 128 bits
key = binascii.unhexlify('c6e60b68ce37e90e5ea08930b381af38')


# Input file that is to be encrypted
i_file = 'myfile'


# Output File - Well need to randomize it
o_file='junk'


# Chunksize is a random block size of the file that is divisible by 16. Just used to make sure file has data
chunksize=64*1024







# Important Facts
# nonce = 64 bits, and counter.new() = 64 bits, we combine nonce+counter=128 bits with 128 bit key.
# key + (nonce+counter) = cipher

# Encrypt 
def encrypt(key, nonce, filesize, i_file, o_file, chunksize):
    encryptor = AES.new(key, AES.MODE_CTR, counter=Counter.new(64, prefix=nonce))


    with open(i_file, 'rb') as infile:
        with open(o_file, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
        
            while True:
                chunk = infile.read(chunksize)  # read up to 64*1024 bytes
                if len(chunk) == 0: 
                    break
                elif len(chunk) % 16 != 0:      # if file is not empty 
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))



# Run Encryption Function
if not os.path.isfile(i_file):
    print "File: \"%s\", does not exist" % i_file
else:
    # Same as file size from ls -l output
    filesize = os.path.getsize(i_file)  

    encrypt(key, nonce, filesize, i_file, o_file, chunksize)
    print "file exists"

