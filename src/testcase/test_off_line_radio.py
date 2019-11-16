from utils.play_aidio import play
import time,subprocess,os
import settings.DIR_PATH as path
from utils import get_device_log as gdl
import uiautomator2 as u
from utils import img_match,get_mic_status
from utils.img2str import get_str
from utils.get_img_ROI import get_ROIimg
from utils import check_time_and_result as ck
from utils.driver import Driver
from config import *
import pytest,time,allure,sys

@pytest.mark.P1
@allure.feature("电台测试")
class Test_offline_radio:
    def setup_class(cls):
        dr = Driver()
        cls.driver = dr.init_driver(device_name)
        cls.GDL = gdl.Get_device_log()

    def teardown(self):
        print("this case finishd")
        time.sleep(2)
        cmd = 'del /F /S /Q D:\\text_all_new'
        os.system(cmd)

    @allure.story('0001.打开收音机')
    def test_case1(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        get_mic_status.get_mic_status(self.driver)   #获取麦克风图标状态
        play("打开收音机", path.men_qa_file)          #播放问题
        time.sleep(1)
        self.driver.screenshot(path.Cache_img_path2)
        time.sleep(9)
        result = img_match.picture_match(self.driver,["radio.png"],0.95)
        print('result',result)
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        ck.check(check_time,result,'radio_case1')

    @allure.story('0002.调幅九百')
    def test_case2(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        get_mic_status.get_mic_status(self.driver)
        play("调幅九百", path.men_qa_file)
        time.sleep(0.5)
        self.driver.screenshot(path.Cache_img_path2)
        time.sleep(9)
        self.driver.screenshot(path.src_path + "file.png")
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
        ck.check(check_time, result, 'radio_case2')

    @allure.story('0003.调频88')
    def test_case3(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        get_mic_status.get_mic_status(self.driver)
        play("调频88", path.men_qa_file)
        time.sleep(0.5)
        self.driver.screenshot(path.Cache_img_path2)
        time.sleep(9)
        result = img_match.picture_match(self.driver,["radio88.png"],0.99)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        ck.check(check_time, result, 'radio_case3')

    @allure.story('0004.下一个频道，大于88')
    def test_case4(self):
        self.driver.screenshot(path.src_path + "file.png")
        get_ROIimg()
        time.sleep(1)
        ret_bef = get_str()
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        get_mic_status.get_mic_status(self.driver)
        print("wake_finish_time",wake_finish_time)
        time.sleep(0.5)
        self.driver.screenshot(path.Cache_img_path2)
        time.sleep(9)
        self.driver.screenshot(path.src_path + "file.png")
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
        ck.check(check_time, result, 'radio_case4')

    @allure.story('0005.下一台，大于88.3')
    def test_case5(self):
        self.driver.screenshot(path.src_path + "file.png")
        get_ROIimg()
        time.sleep(wake_time)
        ret_bef = get_str()
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        get_mic_status.get_mic_status(self.driver)
        play("下一台", path.men_qa_file)
        time.sleep(0.5)
        self.driver.screenshot(path.Cache_img_path2)
        time.sleep(9)
        self.driver.screenshot(path.src_path + "file.png")
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
        ck.check(check_time, result, 'radio_case5')

    @allure.story('0006.下一台，大于88.3')
    def test_case6(self):
        self.driver.screenshot(path.src_path + "file.png")
        get_ROIimg()
        time.sleep(wake_time)
        ret_bef = get_str()
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        get_mic_status.get_mic_status(self.driver)
        play("下一个电台", path.men_qa_file)
        time.sleep(0.5)
        self.driver.screenshot(path.Cache_img_path2)
        time.sleep(9)
        self.driver.screenshot(path.src_path + "file.png")
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
        ck.check(check_time, result, 'radio_case6')




    @allure.story('0007.换台')
    def test_case7(self):
        self.driver.screenshot(path.src_path + "file.png")
        get_ROIimg()
        time.sleep(1)
        ret_bef = get_str()
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        get_mic_status.get_mic_status(self.driver)
        play("换台", path.men_qa_file)
        time.sleep(0.5)
        self.driver.screenshot(path.Cache_img_path2)
        time.sleep(9)
        self.driver.screenshot(path.src_path + "file.png")
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
        ck.check(check_time, result, 'radio_case7')

    @allure.story('0008.上一个广播')
    def test_case8(self):
        self.driver.screenshot(path.src_path + "file.png")
        get_ROIimg()
        time.sleep(1)
        ret_bef = get_str()
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        get_mic_status.get_mic_status(self.driver)
        play("上一个广播", path.men_qa_file)
        time.sleep(0.5)
        self.driver.screenshot(path.Cache_img_path2)
        time.sleep(9)
        self.driver.screenshot(path.src_path + "file.png")
        get_ROIimg()
        time.sleep(1)
        ret_aft = get_str()
        print(ret_bef,ret_aft)
        if float(ret_aft)<float(ret_bef) and ret_aft!="0" and ret_bef!="0":
            result = True
        else:
            result = False
        # result = img_match.picture_match(self.driver,"radio88.png",0.99)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        ck.check(check_time, result, 'radio_case8')

    @allure.story('0009.上一个电台')
    def test_case9(self):
        self.driver.screenshot(path.src_path + "file.png")
        get_ROIimg()
        time.sleep(1)
        ret_bef = get_str()
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        get_mic_status.get_mic_status(self.driver)
        play("上一个电台", path.men_qa_file)
        time.sleep(0.5)
        self.driver.screenshot(path.Cache_img_path2)
        time.sleep(9)
        self.driver.screenshot(path.src_path + "file.png")
        get_ROIimg()
        time.sleep(1)
        ret_aft = get_str()
        print(ret_bef,ret_aft)
        if float(ret_aft)<float(ret_bef) and ret_aft!="0" and ret_bef!="0":
            result = True
        else:
            result = False
        # result = img_match.picture_match(self.driver,"radio88.png",0.99)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        ck.check(check_time, result, 'radio_case9')

#
# if __name__ == "__main__":
#     ask = Music_ask()
#     ask.test_case1()
#     ask.test_case2()
#     ask.test_case3()
#     ask.test_case4()
#     ask.test_case5()
#     ask.test_case6()
#     ask.test_case7()
#     ask.test_case8()