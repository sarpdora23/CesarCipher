# CesarCipher
Python script for encrypt-decrypt Cesar Cipher

Not: For encryption and decryption process based on only a-z.

usage: Cesar Cipher Encrypt/Decrypt [-h] -m METHOD -t TEXT [TEXT ...] [-n NUMBER] [-w WORDLIST]

You can encrypt and decrypt your text.

options:
  -h, --help            show this help message and exit
  -m METHOD, --method METHOD
                        decrypt or encrypt
  -t TEXT [TEXT ...], --text TEXT [TEXT ...]
                        Your plain text
  -n NUMBER, --number NUMBER
                        Shift number
  -w WORDLIST, --wordlist WORDLIST
                        Bruteforce wordlist
Example: python main.py -m encrypt -t deneme -n 3
         python main.py -m decrypt -t Wevt Hsve -w test.txt
