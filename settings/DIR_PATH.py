# -*- coding: utf-8 -*-
import os

DIR_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
web_path = DIR_PATH+'\src\py3_web.py'
result_path = DIR_PATH+'\\settings\\result.txt'
currtxt_path = DIR_PATH+'\\settings\\current_file.txt'
device_log_path = DIR_PATH+"\\logs"
record_file = DIR_PATH+"\\record_files\\"
wake_up_file = DIR_PATH+'\\audio\\wake_up\\'
men_question_file = DIR_PATH+'\\audio\\question\\men_question\\'
women_question_file = DIR_PATH+'\\audio\\question\\women_question\\'

def file_path():
    with open(currtxt_path,'r')as f:
        file = f.read().strip()
        return file