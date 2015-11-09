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
#   key[128-bits] xor (nonce+counter)[128-bits] = cipher[128-bits]
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


# Input file that is to be decrypted
i_file = 'junk'


# Output File 
o_file='myfile'


# Chunksize is a random block size of the file that is divisible by 16. Just used to make sure file has data
chunksize=64*1024





# Decrypt 
def decrypt(key, nonce, i_file, o_file, chunksize):
    decryptor = AES.new(key, AES.MODE_CTR, counter=Counter.new(64, prefix=nonce))


    with open(o_file, 'rb') as infile:
        original_size = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]    # take filesize + filename

        with open(i_file, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)  # read file by chunks
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk)) 

            outfile.truncate(original_size)


# Run Encryption Function
if not os.path.isfile(i_file):
    print "File: \"%s\", does not exist" % i_file
else:
    decrypt(key, nonce, i_file, o_file, chunksize)
    print "file exists"






