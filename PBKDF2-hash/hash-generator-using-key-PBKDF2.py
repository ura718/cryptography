#!/usr/bin/python



#
# Docs: http://bityard.blogspot.com/2012/08/symmetric-crypto-with-pycrypto-part-3.html
#
# PBKDF2: Password-Based Key Derivation Function, version 2
#

import os
from Crypto.Protocol.KDF import PBKDF2
  
password = 'uSh{ei3aiV'
iterations = 5000
key = ''
salt = os.urandom(32)   # 32 bytes salt, but in bits its 256 bits

#
# dkLen = length of the key in bits
# count = how many iterations to perform
# salt = length of the salt in bits
key = PBKDF2(password, salt, dkLen=32, count=iterations) 
    
print 'Random salt (in hex):'
print salt.encode('hex')
print 'PBKDF2-derived key (in hex) of password after %d iterations: ' % iterations
print key.encode('hex')
