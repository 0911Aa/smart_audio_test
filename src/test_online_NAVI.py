# -*- coding: utf-8 -*-
from utils.play_aidio import play
import time,subprocess,os
import settings.DIR_PATH as path
from utils import get_device_log as gdl
import uiautomator2 as u
from utils import img_match
import pytest,time,allure,sys
from config import *


GDL = gdl.Get_device_log()

@allure.feature("测试发现")
@pytest.mark.usefixtures('driver_setup')
@pytest.mark.P1
class Wake_ask:

    def test_case1(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("打开导航", path.men_qa_file)
        time.sleep(15)
        result = img_match.picture_match(self.driver,"03.png")

        GDL.get_device_log()
        start_time = self.GDL.get_begin_parse()
        print("atart_time",start_time)
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
            # cmd = "xcopy /D "+path.DIR_PATH+"\\logs\\log "+path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case1\ /e"
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case1\\"
            subprocess.call(cmd)
            # self.driver.pull("sdcard/txz/log",path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case1")

    def test_case2(self):
        play('你好小西', path.wake_up_file)
        time.sleep(2)
        play("导航到家", path.men_qa_file)
        time.sleep(3)
        play("港惠新天地", path.men_qa_file)
        time.sleep(5)
        result = img_match.picture_match(self.driver,"02.png")
        if result:
            print("\033[7;31mcase2测试通过\033[0m")
        else:
            print("\033[7;44mcase2测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case2\\"
            subprocess.call(cmd)
            # cmd = "xcopy /D "+path.DIR_PATH+"\\logs\\log "+path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case2\ /e"
            # subprocess.call(cmd)
            # self.driver.pull("sdcard/txz/log", path.DIR_PATH + "\\report\\error_log\\" + fail_dir_name + "case2\\")

    def test_case3(self):
        play('你好小西', path.wake_up_file)
        time.sleep(2)
        play("到红花湖", path.men_qa_file)
        time.sleep(10)
        play("第一个",path.men_qa_file)
        time.sleep(15)
        play("第二个",path.men_qa_file)
        time.sleep(30)
        self.GDL.get_device_log()
        result = self.GDL.get_last_ret("导航路线")
        if result:
            print("\033[7;31mcase3测试通过\033[0m")
        else:
            print("\033[7;44mcase3测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case3\\"
            subprocess.call(cmd)
            # cmd = "xcopy /D "+path.DIR_PATH+"\\logs\\log "+path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case3\ /e"
            # subprocess.call(cmd)
            # self.driver.pull("sdcard/txz/log", path.DIR_PATH + "\\report\\error_log\\" + fail_dir_name + "case3\\")

    def test_case4(self):
        play('你好小西', path.wake_up_file)
        time.sleep(2)
        play("导航去红花", path.men_qa_file)
        time.sleep(10)
        play("第二个", path.men_qa_file)
        time.sleep(15)
        play("第一个", path.men_qa_file)
        time.sleep(30)
        self.GDL.get_device_log()
        result = self.GDL.get_last_ret("个导航路线")
        if result:
            print("\033[7;31mcase4测试通过\033[0m")
        else:
            print("\033[7;44mcase4测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case4\\"
            subprocess.call(cmd)
            # cmd = "xcopy /D "+path.DIR_PATH+"\\logs\\log "+path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case4\ /e"
            # subprocess.call(cmd)
            # self.driver.pull("sdcard/txz/log", path.DIR_PATH + "\\report\\error_log\\" + fail_dir_name + "case4\\")

    def test_case5(self):
        play('你好小西', path.wake_up_file)
        time.sleep(2)
        play("去红花湖", path.men_qa_file)
        time.sleep(10)
        play("第一个", path.men_qa_file)
        time.sleep(15)
        play("第二个", path.men_qa_file)
        time.sleep(30)
        self.GDL.get_device_log()
        result = self.GDL.get_last_ret("导航路线")
        if result:
            print("\033[7;31mcase5测试通过\033[0m")
        else:
            print("\033[7;44mcase5测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case5\\"
            subprocess.call(cmd)
            # cmd = "xcopy /D "+path.DIR_PATH+"\\logs\\log "+path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case5\ /e"
            # subprocess.call(cmd)
            # self.driver.pull("sdcard/txz/log", path.DIR_PATH + "\\report\\error_log\\" + fail_dir_name + "case5\\")

    def test_case6(self):
        play('你好小西', path.wake_up_file)
        time.sleep(2)
        play("带我去红花", path.men_qa_file)
        time.sleep(10)
        play("第一个", path.men_qa_file)
        time.sleep(15)
        play("第二个", path.men_qa_file)
        time.sleep(30)
        self.GDL.get_device_log()
        result = self.GDL.get_last_ret("个导航路线")
        if result:
            print("\033[7;31mcase6测试通过\033[0m")
        else:
            print("\033[7;44mcase6测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case6\\"
            subprocess.call(cmd)
            # cmd = "xcopy /D "+path.DIR_PATH+"\\logs\\log "+path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case6\ /e"
            # subprocess.call(cmd)
            # self.driver.pull("sdcard/txz/log", path.DIR_PATH + "\\report\\error_log\\" + fail_dir_name + "case6\\")

    def test_case7(self):
        play('你好小西', path.wake_up_file)
        time.sleep(2)
        play("红花湖附近", path.men_qa_file)
        time.sleep(10)
        play("第一个", path.men_qa_file)
        time.sleep(15)
        play("第二个", path.men_qa_file)
        time.sleep(30)
        self.GDL.get_device_log()
        result = self.GDL.get_last_ret("个导航路线")
        if result:
            print("\033[7;31mcase7测试通过\033[0m")
        else:
            print("\033[7;44mcase7测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case7\\"
            subprocess.call(cmd)
            # cmd = "xcopy /D "+path.DIR_PATH+"\\logs\\log "+path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case7\ /e"
            # subprocess.call(cmd)
            # self.driver.pull("sdcard/txz/log", path.DIR_PATH + "\\report\\error_log\\" + fail_dir_name + "case7\\")

    def test_case8(self):
        play('你好小西', path.wake_up_file)
        time.sleep(1.5)
        play("关闭导航", path.men_qa_file)
        time.sleep(10)
        self.GDL.get_device_log()
        # 将为您退出导航,好的，收到，遵命
        result = self.GDL.get_last_ret("退出导航|好的|收到|遵命")
        if result:
            print("\033[7;31mcase8测试通过\033[0m")
        else:
            print("\033[7;44mcase8测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case8\\"
            subprocess.call(cmd)
            # cmd = "xcopy /D "+path.DIR_PATH+"\\logs\\log "+path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case8\ /e"
            # subprocess.call(cmd)
            # self.driver.pull("sdcard/txz/log", path.DIR_PATH + "\\report\\error_log\\" + fail_dir_name + "case1\\")


    # def wake_ask(self):
        # p = pyaudio.PyAudio()
        # GDL = gdl.Get_device_log()
        test_num = 0
        pass_num = 0
        fail_num = 0
        # men_question_list = os.listdir(path.men_qa_file)
        # for i in men_question_list:
        #     file_name = i.split(".")[0]
        #     file_id = file_name.split("q")[1]
        #     print(file_id)
        #     play('man_wake_up', path.wake_up_file)
        #     play(file_name, path.men_qa_file)
        #
        #     wake_finish_time = self.GDL.get_local_time()
        #     print(wake_finish_time)
        #     time.sleep(30)
            # GDL.get_device_log()
            # time.sleep(1)
            # start_time = GDL.get_begin_parse()
            # print("\033[7;31m收到唤醒词的时间：\033[0m",start_time)
            # end_time,new_result = GDL.get_device_wake()
            # print("返回%s的时间是%f"%(new_result,end_time))
            # wait_time = end_time -start_time
            # check_time = abs(wake_finish_time-start_time)
            # print("唤醒耗时",wait_time)
            # print("本地时间误差",check_time)
            # try:
            #     if wait_time >=2 or check_time>=5:
            #         raise Exception("唤醒异常")
            #     else:
            #         pass_num+=1
            # except Exception as e:
            #     print(e)
            #     fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            #     cmd = "xcopy /D "+path.DIR_PATH+"\\logs\\log "+path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"\ /e"
            #     subprocess.call(cmd)
            # print("\033[7;31m总共测试%s次，成功%s次\033[0m"%(test_num,pass_num))


if __name__ == "__main__":
    ask = Wake_ask()
    ask.test_case1()
    ask.test_case2()
    ask.test_case3()
    ask.test_case4()
    ask.test_case5()
    ask.test_case6()
    ask.test_case7()
    ask.test_case8()