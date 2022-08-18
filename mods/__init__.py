import os
import pandas
import pickle

import PySimpleGUI as sg

from random import choice
from urllib3 import PoolManager
from cryptography.fernet import Fernet


class Data:
    http = PoolManager()
    key = Fernet(http.request('GET', 'https://gemgames.w3spaces.com/data-key.txt').data)

    with open('C:/Users/summe/AppData/Local/GEM Games/CodeRandom3/data/Data.pkl', 'rb') as fh:
        data = key.decrypt(pickle.load(fh))

    with open('temp.csv', 'wb') as file:
        file.write(data)

    data = pandas.read_csv('temp.csv', index_col=0, header=None)

    os.remove('temp.csv')
    print(data)


class Layouts:

    sg.theme(choice(sg.theme_list()))

    main_menu1 = [
        [sg.Text('CodeRandom3: The Unwanted Trilogy')]
    ]

    layout = [
        [
            sg.Column(main_menu1, k='main_menu1')
        ]
    ]
