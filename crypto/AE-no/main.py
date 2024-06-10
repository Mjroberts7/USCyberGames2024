#!/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from os import urandom
from secret import flag

def encrypt(msg, key, iv):
  cipher = AES.new(key, AES.MODE_CBC, iv) 
  enc = cipher.encrypt(pad(msg,16))
  return enc

def decrypt(enc, key, iv)
  cipher = AES.new(key, AES.MODE_CBC, iv)
  dec = unpad(cipher.decrypt(enc), 16)
  return dec
  
def main():
  iv = urandom(16)
  key = b'SecretKey1234567'
  msg = b'Here is the flag for you: ' + flag
  enc =  96a0299d6c60cd0f40218b73ab5fc4b710b8951bd0ed8977a1382328454a2ce68106660bb48808c2fa7a141ac863732f66f9032d00cf2c0ecc3a6871683911a6#encrypt(msg, key, iv)
  
  '''
  cipher = AES.new(key, AES.MODE_CBC, iv)
  enc = cipher.encrypt(pad(msg,16))
  '''
  print("Key: SecretKey1234567") #+ key.decode()) 
  print("Encoded Flag: 96a0299d6c60cd0f40218b73ab5fc4b710b8951bd0ed8977a1382328454a2ce68106660bb48808c2fa7a141ac863732f66f9032d00cf2c0ecc3a6871683911a6") #+ enc.hex())
  dec = decrypt(enc, key, iv)
  print("Decoded Flag: " + dec.decode()) 

if __name__ == '__main__': main()
