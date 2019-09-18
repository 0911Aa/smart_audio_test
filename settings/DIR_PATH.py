# -*- coding: utf-8 -*-
import os

DIR_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PC_PATH = "C:\\Users\\pengfy\\PycharmProjects\\smart-audio\\"
web_path = DIR_PATH+'\src\py3_web.py'
result_path = DIR_PATH+'\\settings\\result.txt'
currtxt_path = DIR_PATH+'\\settings\\current_file.txt'
device_log_path = DIR_PATH+"\\logs"
record_file = DIR_PATH+"\\record_files\\"
wake_up_file = PC_PATH+'\\audio\\wake_up\\'
men_handle_file = PC_PATH+'\\audio\\question\\men_question\\handle_class\\'
men_qa_file = PC_PATH+'\\audio\\question\\men_question\\qa_class\\'
women_handle_file = PC_PATH+'\\audio\\question\\women_question\\handle_class\\'
women_qa_file = PC_PATH+'\\audio\\question\\women_question\\qa_class\\'
img_path = DIR_PATH+"\\img\\"
src_path = DIR_PATH+"\\src\\"
log_path = DIR_PATH+"\\logs\\text_all"

def file_path():
    with open(currtxt_path,'r')as f:
        file = f.read().strip()
        return file