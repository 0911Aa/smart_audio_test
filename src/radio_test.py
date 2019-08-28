# -*- coding: utf-8 -*-
from utils.play_aidio import play
import time,subprocess,os
import settings.DIR_PATH as path
from utils import get_device_log as gdl
import uiautomator2 as u
from utils import img_match

class Music_ask:
    def __init__(self):
        cmd1 = "adb connect 192.168.0.2:5555"
        cmd2 = "python -m uiautomator2 init"
        subprocess.call(cmd1, shell=True)
        subprocess.call(cmd2, shell=True)
        self.GDL = gdl.Get_device_log()
        self.driver = u.connect("192.168.0.2:5555")

    def test_case1(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("打开收音机", path.men_qa_file)
        time.sleep(10)
        # play("第一个", path.men_qa_file)
        # time.sleep(10)
        result = img_match.picture_match(self.driver,"radio.png",0.95)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        if check_time>=5:
            print("\033[7;44mcase1唤醒失败\033[0m")
        else:
            print("\033[7;31mcase1唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase1测试通过\033[0m")
        else:
            print("\033[7;44mcase1测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case1\\"
            subprocess.call(cmd)


    def test_case2(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("调幅九百", path.men_qa_file)
        time.sleep(10)
        result = img_match.picture_match(self.driver,"radio900.png",0.99)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        if check_time>=5:
            print("\033[7;44mcase2唤醒失败\033[0m")
        else:
            print("\033[7;31mcase2唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase2测试通过\033[0m")
        else:
            print("\033[7;44mcase2测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case1\\"
            subprocess.call(cmd)

    def test_case3(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("调频88", path.men_qa_file)
        time.sleep(10)
        result = img_match.picture_match(self.driver,"radio88.png",0.99)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        if check_time>=5:
            print("\033[7;44mcase2唤醒失败\033[0m")
        else:
            print("\033[7;31mcase2唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase2测试通过\033[0m")
        else:
            print("\033[7;44mcase2测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case1\\"
            subprocess.call(cmd)

if __name__ == "__main__":
    ask = Music_ask()
    ask.test_case1()
    ask.test_case2()
    ask.test_case3()