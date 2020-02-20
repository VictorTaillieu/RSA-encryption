# RSA encryption

This Python program implements RSA encryption using Crypto library. It has a command-line interface.

## Prerequisities

This application requires [Python 3.8](https://www.python.org/downloads/). Check your python version using:
````
$ python --version
Python 3.8.0
````

To install the requirements, you can use:
```
$ pip install -r requirements.txt
```

## Quickstart

### Generate keys

Generate RSA public/private keys with:
```
$ rsa.py -g 2048
```
You can replace 2048 with another key size like 1024 or 4096 (in bits).
It is possible to add a passphrase to encrypt the private key by adding `-p <passphrase>` after the previous command.

**IMPORTANT: Never share your private key, only publish your public key.**

### Encrypt

Write your message in input.txt and run:
```
$ rsa.py -e
```
The encrypted message will be stored in output.txt.

### Decrypt

Paste the encrypted message in input.txt and run:
```
$ rsa.py -d
```
Don't forget to add `-p <passphrase>` if you specified a passphrase to generate the keys. You will find the original message in output.txt.

## Help

To have a recap of the commands, use:
```
$ rsa.py -h
```
