from datetime import date
from socket import gethostname
from time import time

import PySimpleGUI as sg
from urllib3 import PoolManager

import mods
from mods import Data, Layouts, terminate

host = gethostname()
http = PoolManager()

date = date.today()
start_game_time = time()


if not terminate:
    wn = sg.Window('CodeRandom3 - The Unwanted Trilogy', Layouts.layout, finalize=True, size=(int(Data.width), int(Data.height)))
    active = 'main_menu1'
    wn.maximize()


while not mods.terminate:
    event, values = wn.read()

    if event in ('Quit', sg.WIN_CLOSED):
        break
    if event == 'Settings':
        wn[active].Update(visible=False)
        active = 'settings'
        wn[active].Update(visible=True)
    if event in ('Save', 'Return'):
        wn[active].Update(visible=False)
        active = 'main_menu1'
        wn[active].Update(visible=True)

wn.close()

