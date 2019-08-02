# -*- coding: utf-8 -*-
import os

DIR_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
web_path = DIR_PATH+'\src\py3_web.py'
result_path = DIR_PATH+'\\settings\\result.txt'
currtxt_path = DIR_PATH+'\\settings\\current_file.txt'
record_file = DIR_PATH+"\\record_files\\"
play_file = DIR_PATH+'\\sources\\'

def file_path():
    with open(currtxt_path,'r')as f:
        file = f.read().strip()
        return file