# -*- coding: utf-8 -*-
from utils.play_aidio import play
import pyaudio
import time,subprocess,os
import settings.DIR_PATH as path
from utils import get_device_log as gdl

def wake_ask():
    # p = pyaudio.PyAudio()
    GDL = gdl.Get_device_log()
    test_num = 0
    pass_num = 0
    fail_num = 0
    men_question_list = os.listdir(path.men_question_file)
    for i in men_question_list:
        file_name = i.split(".")[0]
        file_id = file_name.split("q")[1]

        play('woman_wake_up', path.wake_up_file)
        play(file_name, path.men_question_file)


        wake_finish_time = GDL.get_local_time()
        print(wake_finish_time)
        time.sleep(30)
        GDL.get_device_log()
        time.sleep(1)
        start_time = GDL.get_begin_parse()
        print("\033[7;31m收到唤醒词的时间：\033[0m",start_time)
        end_time,new_result = GDL.get_device_wake()
        print("返回%s的时间是%f"%(new_result,end_time))
        wait_time = end_time -start_time
        check_time = abs(wake_finish_time-start_time)
        print("唤醒耗时",wait_time)
        print("本地时间误差",check_time)
        try:
            if wait_time >=2 or check_time>=5:
                raise Exception("唤醒异常")
            else:
                pass_num+=1
        except Exception as e:
            print(e)
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "xcopy /D "+path.DIR_PATH+"\\logs\\log "+path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"\ /e"
            subprocess.call(cmd)
        # print("\033[7;31m总共测试%s次，成功%s次\033[0m"%(test_num,pass_num))


if __name__ == "__main__":
    wake_ask()
