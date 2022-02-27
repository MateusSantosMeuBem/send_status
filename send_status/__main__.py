import argparse
import os
from positions import *
import pyautogui
from time import sleep

def moveAndClick(
                position: tuple,
                button: str = 'left'):

    pyautogui.moveTo(position)
    pyautogui.click(button = button)

parse = argparse.ArgumentParser(description='Executes send_status.', usage='python .\send_status -fp "C:/Users/Video/video_folder"',)

parse.add_argument('-fp', '--folder_path', help = 'Folder where are the videos to be sent.',type = str, action = 'store', default = None)

args: dict = parse.parse_args().__dict__

if args['folder_path'] is None:
    print('No folder path given. Exiting.')
    exit()
if not os.path.isdir(args['folder_path']):
    print('Folder path is not valid.')
    exit()

pyautogui.PAUSE = 0.3

MOVIE_PATH = args['folder_path']
MOVIE_PARTS = sorted(os.listdir(MOVIE_PATH))

pyautogui.alert('Please, make sure you are in the right window.')
moveAndClick(EXTENTIONS)
moveAndClick(WHAT_WEB_EXTENTION)

for movie_part in MOVIE_PARTS[0:]:
    moveAndClick(STATUS_OP)
    moveAndClick(CHOSE_FILE)
    moveAndClick(TOP_BAR, button = 'right')
    moveAndClick(MAXIMIXE_WINDOW)
    moveAndClick(NAME_FILE_BAR)
    pyautogui.typewrite(f'{MOVIE_PATH}\{movie_part}')
    moveAndClick(OPEN_FILE)
    moveAndClick(SEND_FILE)
    print(f'{movie_part} sent')
    sleep(15)
