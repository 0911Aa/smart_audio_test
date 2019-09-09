from utils.play_aidio import play
import time,subprocess,os
import settings.DIR_PATH as path
from utils import get_device_log as gdl
import uiautomator2 as u
from utils import img_match
from utils.img2str import get_str
from utils.get_img_ROI import get_ROIimg
from utils import check_time_and_result as ck
from config import *

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
        result = img_match.picture_match(self.driver,["radio.png"],0.95)

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
        time.sleep(6)
        self.driver.screenshot("file.png")
        get_ROIimg()
        time.sleep(1)
        ret = get_str()
        print(ret)
        if ret == "900":
            result = True
        else:
            result = False
        # result = img_match.picture_match(self.driver,"radio900.png",0.99)

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
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case2\\"
            subprocess.call(cmd)

    def test_case3(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("调频88", path.men_qa_file)
        time.sleep(10)
        result = img_match.picture_match(self.driver,["radio88.png"],0.99)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        if check_time>=5:
            print("\033[7;44mcase3唤醒失败\033[0m")
        else:
            print("\033[7;31mcase3唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase3测试通过\033[0m")
        else:
            print("\033[7;44mcase3测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case3\\"
            subprocess.call(cmd)


    def test_case4(self):
        self.driver.screenshot("file.png")
        get_ROIimg()
        time.sleep(1)
        ret_bef = get_str()
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(wake_time)
        play("下一个频道", path.men_qa_file)
        time.sleep(10)
        self.driver.screenshot("file.png")
        get_ROIimg()
        time.sleep(1)
        ret_aft = get_str()
        print(ret_bef,ret_aft)
        if float(ret_aft)>float(ret_bef) and ret_aft!="0" and ret_bef!="0":
            result = True
        else:
            result = False
        # result = img_match.picture_match(self.driver,"radio88.png",0.99)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        ck.check(check_time, result, '电台case4')

    def test_case5(self):
        self.driver.screenshot("file.png")
        get_ROIimg()
        time.sleep(1)
        ret_bef = get_str()
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("下一台", path.men_qa_file)
        time.sleep(10)
        self.driver.screenshot("file.png")
        get_ROIimg()
        time.sleep(1)
        ret_aft = get_str()
        print(ret_bef,ret_aft)
        # result = img_match.picture_match(self.driver,"radio88.png",0.99)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        if check_time>=5:
            print("\033[7;44mcase5唤醒失败\033[0m")
        else:
            print("\033[7;31mcase5唤醒成功\033[0m")
        if float(ret_aft)>float(ret_bef) and ret_aft!="0" and ret_bef!="0":
            print("\033[7;31mcase5测试通过\033[0m")
        else:
            print("\033[7;44mcase5测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case5\\"
            subprocess.call(cmd)

    def test_case6(self):
        self.driver.screenshot("file.png")
        get_ROIimg()
        time.sleep(1)
        ret_bef = get_str()
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("上一个广播", path.men_qa_file)
        time.sleep(10)
        self.driver.screenshot("file.png")
        get_ROIimg()
        time.sleep(1)
        ret_aft = get_str()
        print(ret_bef,ret_aft)
        # result = img_match.picture_match(self.driver,"radio88.png",0.99)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        if check_time>=5:
            print("\033[7;44mcase6唤醒失败\033[0m")
        else:
            print("\033[7;31mcase6唤醒成功\033[0m")
        if float(ret_aft)<float(ret_bef) and ret_aft!="0" and ret_bef!="0":
            print("\033[7;31mcase6测试通过\033[0m")
        else:
            print("\033[7;44mcase6测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case6\\"
            subprocess.call(cmd)

    def test_case7(self):
        self.driver.screenshot("file.png")
        get_ROIimg()
        time.sleep(1)
        ret_bef = get_str()
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("上一个电台", path.men_qa_file)
        time.sleep(10)
        self.driver.screenshot("file.png")
        get_ROIimg()
        time.sleep(1)
        ret_aft = get_str()
        print(ret_bef,ret_aft)
        # result = img_match.picture_match(self.driver,"radio88.png",0.99)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        if check_time>=5:
            print("\033[7;44mcase7唤醒失败\033[0m")
        else:
            print("\033[7;31mcase7唤醒成功\033[0m")
        if float(ret_aft)<float(ret_bef) and ret_aft!="0" and ret_bef!="0":
            print("\033[7;31mcase7测试通过\033[0m")
        else:
            print("\033[7;44mcase7测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case7\\"
            subprocess.call(cmd)

    def test_case8(self):
        self.driver.screenshot("file.png")
        get_ROIimg()
        time.sleep(1)
        ret_bef = get_str()
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("换台", path.men_qa_file)
        time.sleep(10)
        self.driver.screenshot("file.png")
        get_ROIimg()
        time.sleep(1)
        ret_aft = get_str()
        print(ret_bef,ret_aft)
        # result = img_match.picture_match(self.driver,"radio88.png",0.99)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        if check_time>=5:
            print("\033[7;44mcase8唤醒失败\033[0m")
        else:
            print("\033[7;31mcase8唤醒成功\033[0m")
        if float(ret_aft)>float(ret_bef) and ret_aft!="0" and ret_bef!="0":
            print("\033[7;31mcase8测试通过\033[0m")
        else:
            print("\033[7;44mcase8测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case8\\"
            subprocess.call(cmd)

    # def test_case6(self):
    #     self.driver.screenshot("file.png")
    #     get_ROIimg()
    #     time.sleep(1)
    #     ret_bef = get_str()
    #     play('你好小西', path.wake_up_file)
    #     wake_finish_time = self.GDL.get_local_time()
    #     print("wake_finish_time",wake_finish_time)
    #     time.sleep(2)
    #     play("上一个广播", path.men_qa_file)
    #     time.sleep(10)
    #     self.driver.screenshot("file.png")
    #     get_ROIimg()
    #     time.sleep(1)
    #     ret_aft = get_str()
    #     print(ret_bef,ret_aft)
    #     # result = img_match.picture_match(self.driver,"radio88.png",0.99)
    #
    #     self.GDL.get_device_log()
    #     start_time, new_result = self.GDL.get_device_wake()
    #     print("start_time",start_time)
    #     check_time = abs(wake_finish_time-start_time)
    #     print(check_time)
    #     if check_time>=5:
    #         print("\033[7;44mcase6唤醒失败\033[0m")
    #     else:
    #         print("\033[7;31mcase6唤醒成功\033[0m")
    #     if float(ret_aft)>float(ret_bef) and ret_aft!="0" and ret_bef!="0":
    #         print("\033[7;31mcase6测试通过\033[0m")
    #     else:
    #         print("\033[7;44mcase6测试失败\033[0m")
    #         fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
    #         cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case6\\"
    #         subprocess.call(cmd)

if __name__ == "__main__":
    ask = Music_ask()
    ask.test_case1()
    ask.test_case2()
    ask.test_case3()
    ask.test_case4()
    ask.test_case5()
    ask.test_case6()
    ask.test_case7()
    ask.test_case8()