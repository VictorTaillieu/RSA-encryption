from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode, b64encode
from sys import argv, exit
from getopt import getopt, GetoptError


def generateKey(size, password):
    print("Generating RSA public/private keys...")
    key = RSA.generate(size)

    private_key = key.export_key(passphrase=password)  # PEM format
    with open("private.pem", "wb") as private_file:
        private_file.write(private_key)

    public_key = key.publickey().exportKey()
    with open("public.pem", "wb") as public_file:
        public_file.write(public_key)


def importKey(key_file, password):
    try:
        key = RSA.import_key(open(key_file).read(), password)
    except ValueError:
        print("Incorrect password")
        exit()
    return PKCS1_OAEP.new(key)  # padding


def encrypt():
    public_key = importKey("public.pem", password)

    with open("input.txt", "r") as input_file:
        message = input_file.read().encode()  # UTF-8

    print("Encrypting the message...")
    encrypted_text = public_key.encrypt(message)

    with open("output.txt", "wb") as output_file:
        output_file.write(b64encode(encrypted_text))


def decrypt(password):
    private_key = importKey("private.pem", password)

    with open("input.txt", "rb") as input_file:
        encrypted_text = input_file.read()

    print("Decrypting the message...")
    message = private_key.decrypt(b64decode(encrypted_text))

    with open("output.txt", "wb") as output_file:
        output_file.write(message)


def help():
    print("rsa.py (-g <key_size>) -e/d (-p <password>)")
    exit()


try:
    opts, args = getopt(argv[1:], "hg:edp:")
except GetoptError:
    help()

password = None
for opt, arg in opts:
    if opt == "-p":
        password = arg

for opt, arg in opts:
    if opt == "-h":
        help()
    elif opt == "-g":
        size = int(arg)
        generateKey(size, password)
    elif opt == "-e":
        encrypt()
    elif opt == "-d":
        decrypt(password)
