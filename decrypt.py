import os, sys
from cryptography.fernet import Fernet
import getpass

def decode(f):
    with open(f, 'rb') as file:
        txt = fnt.decrypt(file.read())
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
                decode(f)
            except:
                pass

#os.chdir('C:\\Users\\'+getpass.getuser()+'\\Documents')
with open('key.txt', 'rb') as f:
    key = f.read()
fnt = Fernet(key)
print('Working...')
dirs('./')
print('Done')
