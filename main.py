import os
import pickle
import shutil
import wget
import git

import PySimpleGUI as sg
import random as r

from pyperclip import copy, paste
from urllib3 import PoolManager
from datetime import date
from socket import gethostname

repo = git.Repo('')