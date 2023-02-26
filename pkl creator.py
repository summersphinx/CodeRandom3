import pickle
import os

from urllib3 import PoolManager
from PySimpleGUI import PopupGetFile
from cryptography.fernet import Fernet

http = PoolManager()
key = Fernet(http.request('GET', 'https://gemgames.w3spaces.com/data-key.txt').data)


def make(name, data):
    print(data)
    if not os.path.isdir('C:/Users/summe/AppData/Local/GEM Games/CodeRandom3/data'):
        os.makedirs('C:/Users/summe/AppData/Local/GEM Games/CodeRandom3/data')
    with open('C:/Users/summe/AppData/Local/GEM Games/CodeRandom3/data/' + name + '.pkl', 'wb') as fh:
        pickle.dump(data, fh)
    with open('C:/Users/summe/Documents/PycharmProjects/CR3-Stuff/data/' + name + '.pkl', 'wb') as fh:
        pickle.dump(data, fh)


if __name__ == '__main__':
    with open(PopupGetFile('Select File to be pickled...'), 'rb') as file:
        make(input('Name of File'), key.encrypt(file.read()))
