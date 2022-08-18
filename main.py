import os
import pickle
import shutil
import wget
import time
import pandas

import PySimpleGUI as sg
import random as r

from pyperclip import copy, paste
from urllib3 import PoolManager
from datetime import date
from socket import gethostname
from mods import Layouts

http = PoolManager()
print(date.today())
print(time.time())

wn = sg.Window('CodeRandom3', Layouts.layout, finalize=True)

time.sleep(3)

wn.close()
