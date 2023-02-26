from os import path, getcwd, system, remove, getenv
from pickle import load
from webbrowser import open as wbopen
from random import choice

import PySimpleGUI as sg
from pandas import read_csv
from tkinter import Tk
from PIL import Image, ImageColor, ImageOps
from cryptography.fernet import Fernet
from urllib3 import PoolManager

try:
    terminate = False
    from git import Repo

except ImportError:
    ans = sg.Window('Continue?',
                    [[sg.T('Do you want to continue?')], [sg.Yes(s=10), sg.No(s=10), sg.Button('More Info')]],
                    disable_close=True).read(close=True)
    if ans == 'Yes':
        system('winget install --id Git.Git -e --source winget')
        from git import Repo
    if ans == 'No':
        terminate = True
    if ans == 'More Info':
        wbopen('https://git-scm.com/')

user = getcwd().split('\\')[2]


def Download(update=False):
    # 'C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom3'
    if not update:
        commit = Repo.clone_from('https://github.com/summersphinx/CR3-Stuff',
                                 'C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom3')


class Update:
    pass


class Bugs:
    try:
        with open('bug_info.txt') as fh:
            


class Data:

    http = PoolManager()
    key = Fernet(http.request('GET', 'https://gemgames.w3spaces.com/data-key.txt').data)

    if not path.isdir('C:/Users/{}/AppData/Local/GEM Games/CodeRandom3/data'.format(user)):
        Download()

    with open('C:/Users/{}/AppData/Local/GEM Games/CodeRandom3/data/Data.pkl'.format(user), 'rb') as fh:
        data = key.decrypt(load(fh))

    with open('temp.csv', 'wb') as file:
        file.write(data)

    data = read_csv('temp.csv', index_col=0, header=None)

    remove('temp.csv')

    with open('C:/Users/{}/AppData/Local/GEM Games/CodeRandom3/data/Settings.pkl'.format(user), 'rb') as fh:
        settings_data = key.decrypt(load(fh))

    with open('temp.csv', 'wb') as file:
        file.write(settings_data)

    settings = read_csv('temp.csv', index_col=0, header=None)
    sd = read_csv('temp.csv', index_col=None, header=None).values.tolist()
    print(settings)

    remove('temp.csv')

    if settings[1]['theme'] not in sg.theme_list():
        theme = choice(sg.theme_list())
    else:
        theme = settings[1]['theme']

    # Images
    img_path = getenv('LOCALAPPDATA') + '/GEM Games/CodeRandom3/img/'

    # Button Images
    img_start = Image.open(img_path + 'start.png').convert("L")
    print(type(img_start.save()))
    img_settings = Image.open(img_path + 'settings.png')# .convert("L")
    img_quit = Image.open(img_path + 'quit.png')# .convert("L")
    img_check = Image.open(img_path + 'check.png')# .convert("L")
    img_return = Image.open(img_path + 'return.png')# .convert("L")

    imgs = [img_return, img_check, img_settings, img_quit, img_start]

    for img in range(len(imgs)):
        pass
        # print(type(sg.theme_text_color()))
        # imgs[img] = ImageOps.colorize(imgs[img], ImageColor.getrgb(sg.theme_button_color()), ImageColor.getrgb(sg.theme_button_color_background()))

    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    supported_screens = ['1280x720', '1280x800', '1360x768', '1366x768', '1400x900', '1600x900', '1600x1024',
                         '1680x1050', '1920x1080', '2560x1440']


def make_settings():
    value = [[sg.Text('CodeRandom3: The Unwanted Trilogy', font='Default 24 bold')],
             [sg.Text('For values that are True/False, enter 1/0 respectively to enable or disable.')]]
    for i in Data.sd:
        value.append([sg.Frame('', [
            [sg.Text(i[0].replace("_", ' ').title(), s=(10, 1), tooltip=i[2]), sg.InputText(default_text=i[1], tooltip=i[2], s=(10, 1))]])])
    print(value)
    return value


class Layouts:
    sg.theme(Data.theme)

    main_menu_bottom = [
        [sg.Button('', k='Play', font='Default 24 bold', s=(9, 1), image_source=Data.img_start.tobytes(), button_color=None, ),
         sg.Button('', k='Settings', font='Default 24 bold', s=(9, 1), image_source=Data.img_settings.tobytes(),
                   button_color=None, ),
         sg.Button('', k='Quit', font='Default 24 bold', s=(9, 1), image_source=Data.img_quit.tobytes())]
    ]

    main_menu_middle = [
        []
    ]

    main_menu1 = [
        [sg.Text('CodeRandom3: The Unwanted Trilogy', font='Default 24 bold')],
        [sg.Text('Version: {}'.format(Data.data[1]['version']), font='Default 9')],
        [sg.Column([[sg.Text('', expand_x=True, expand_y=True)]], expand_y=True, expand_x=True,
                   size=(int(Data.width), int(Data.height) - 250))],
        [sg.Column(main_menu_bottom, justification='right', element_justification='right')]
    ]

    settings_bottom = [[
        sg.Button('', k='Save', font='Default 24 bold', s=(9, 1), image_source=Data.img_check.tobytes(), button_color=None),
         sg.Button('', k='Return', font='Default 24 bold', s=(9, 1), image_source=Data.img_return.tobytes(), button_color=None)]
    ]

    settings = make_settings()
    settings.append([sg.Frame('', settings_bottom, expand_y=True, expand_x=True, element_justification='center', vertical_alignment='bottom', border_width=0, k='settings_bottom')])

    layout = [
        [
            sg.Column(main_menu1, k='main_menu1'),
            sg.Column(settings, k='settings', visible=False, expand_x=True, expand_y=True)
        ]
    ]


if __name__ == '__main__':
    # print(Data.data[1]['theme'])
    print(make_settings())
