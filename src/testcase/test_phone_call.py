# -*- coding: utf-8 -*-
from utils.play_aidio import play
import settings.DIR_PATH as path
from utils import get_device_log as gdl
from utils import img_match
import pytest,time,allure
from utils import check_time_and_result as ck
from utils.driver import Driver
from config import *
from utils import get_mic_status

@allure.feature("通话测试")
@pytest.mark.P2
class Test_Call:
    def setup_class(cls):
        dr = Driver()
        cls.driver = dr.init_driver(device_name)
        cls.GDL = gdl.Get_device_log()

    def teardown(self):
        print("this case finishd")
        time.sleep(2)
        cmd  = 'del /F /S /Q D:\\text_all_new'
        os.system(cmd)

    @allure.story('0001.拨打10086')
    def test_case1(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        get_mic_status.get_mic_status(self.driver)
        play("拨打100", path.men_qa_file)
        time.sleep(10)
        play("第一个", path.men_qa_file)
        time.sleep(7)
        result = img_match.picture_match(self.driver,["phone_call.png","phone_call1.png","phone_call2.png"],0.9)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        time.sleep(60)
        ck.check(check_time, result, 'phone_call_case1')

    @allure.story('0002.给10086打电话')
    def test_case2(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        get_mic_status.get_mic_status(self.driver)
        play("给妖铃铃八", path.men_qa_file)
        time.sleep(10)
        play("第一个", path.men_qa_file)
        time.sleep(7)
        result = img_match.picture_match(self.driver,["phone_call.png","phone_call1.png","phone_call2.png"],0.9)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        time.sleep(60)
        ck.check(check_time, result, 'phone_call_case2')

    @allure.story('0003.打电话给张三')
    def test_case3(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        get_mic_status.get_mic_status(self.driver)
        play("打电话给张", path.men_qa_file)
        time.sleep(10)
        play("第一个", path.men_qa_file)
        time.sleep(7)
        result = img_match.picture_match(self.driver,["phone_call.png","phone_call1.png","phone_call2.png"],0.9)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        time.sleep(60)
        ck.check(check_time, result, 'phone_call_case3')

    @allure.story('0004.我想打个电话给王老师')
    def test_case4(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        get_mic_status.get_mic_status(self.driver)
        play("我想打个电", path.men_qa_file)
        time.sleep(10)
        play("第一个", path.men_qa_file)
        time.sleep(7)
        result = img_match.picture_match(self.driver,["phone_call.png","phone_call1.png","phone_call2.png"],0.9)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        time.sleep(60)
        ck.check(check_time, result, 'phone_call_case4')

    @allure.story('0005.帮我打电话给张三')
    def test_case5(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        get_mic_status.get_mic_status(self.driver)
        play("帮我打电话", path.men_qa_file)
        time.sleep(10)
        play("第一个", path.men_qa_file)
        time.sleep(7)
        result = img_match.picture_match(self.driver,["phone_call.png","phone_call1.png","phone_call2.png"],0.9)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        time.sleep(60)
        ck.check(check_time, result, 'phone_call_case5')

    @allure.story('0006.呼叫邓伦')
    def test_case6(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        get_mic_status.get_mic_status(self.driver)
        play("帮我打电话", path.men_qa_file)
        time.sleep(10)
        play("第一个", path.men_qa_file)
        time.sleep(7)
        result = img_match.picture_match(self.driver,["phone_call.png","phone_call1.png","phone_call2.png"],0.9)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        time.sleep(60)
        ck.check(check_time, result, 'phone_call_case6')

    @allure.story('0007.拨打王老师的电话')
    def test_case7(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        get_mic_status.get_mic_status(self.driver)
        play("拨打王老师", path.men_qa_file)
        time.sleep(10)
        play("第一个", path.men_qa_file)
        time.sleep(7)
        result = img_match.picture_match(self.driver,["phone_call.png","phone_call1.png","phone_call2.png"],0.9)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        time.sleep(60)
        ck.check(check_time, result, 'phone_call_case7')

    @allure.story('0008.我想给邓伦打个电话')
    def test_case8(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        get_mic_status.get_mic_status(self.driver)
        play("我想给邓伦", path.men_qa_file)
        time.sleep(10)
        play("第一个", path.men_qa_file)
        time.sleep(7)
        result = img_match.picture_match(self.driver,["phone_call.png","phone_call1.png","phone_call2.png"],0.9)

        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        time.sleep(60)
        ck.check(check_time, result, 'phone_call_case8')

    # @allure.story('0009.call一下马云马老板')
    # def test_case9(self):
    #     play('你好小西', path.wake_up_file)
    #     wake_finish_time = self.GDL.get_local_time()
    #     print("wake_finish_time",wake_finish_time)
    #     time.sleep(2)
    #     play("call一", path.men_qa_file)
    #     time.sleep(10)
    #     play("第一个", path.men_qa_file)
    #     time.sleep(10)
    #     result = img_match.picture_match(self.driver,["phone_call.png"])
    #
    #     self.GDL.get_device_log()
    #     start_time, new_result = self.GDL.get_device_wake()
    #     print("start_time",start_time)
    #     check_time = abs(wake_finish_time-start_time)
    #     print(check_time)
    #     time.sleep(60)
    #     ck.check(check_time, result, '电话case9')

    # def test_case3(self):
    #     play('你好小西', path.wake_up_file)
    #     wake_finish_time = self.GDL.get_local_time()
    #     print("wake_finish_time", wake_finish_time)
    #     time.sleep(2)
    #     play("接听", path.men_qa_file)
    #     time.sleep(10)
    #     # play("第一个", path.men_qa_file)
    #     # time.sleep(10)
    #     result = img_match.picture_match(self.driver, "phone_call.png")
    #
    #     self.GDL.get_device_log()
    #     start_time, new_result = self.GDL.get_device_wake()
    #     print("start_time", start_time)
    #     check_time = abs(wake_finish_time - start_time)
    #     print(check_time)
    #     if check_time >= 5:
    #         print("\033[7;44mcase1唤醒失败\033[0m")
    #     else:
    #         print("\033[7;31mcase1唤醒成功\033[0m")
    #     if result:
    #         print("\033[7;31mcase1测试通过\033[0m")
    #     else:
    #         print("\033[7;44mcase1测试失败\033[0m")
    #         fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
    #         cmd = "adb pull sdcard/txz/log " + path.DIR_PATH + "\\report\\error_log\\" + fail_dir_name + "case1\\"
    #         subprocess.call(cmd)