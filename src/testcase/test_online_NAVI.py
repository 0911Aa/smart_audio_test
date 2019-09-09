# -*- coding: utf-8 -*-
from utils.play_aidio import play
import time,subprocess,os
import settings.DIR_PATH as path
from utils import get_device_log as gdl
import uiautomator2 as u
from utils import img_match
import pytest,time,allure,sys
from utils import check_time_and_result as ck
from utils.driver import Driver
from config import *

@allure.feature("导航测试")
@pytest.mark.P2
@pytest.mark.run(order=1)
class Test_online_NAVI:
    def setup_class(cls):
        dr = Driver()
        cls.driver = dr.init_driver(device_name)
        cls.GDL = gdl.Get_device_log()

    def teardown(self):
        cmd = 'del /F /S /Q C:\\Users\pengfy\PycharmProjects\smart-audio\logs\\text_all_new'
        os.system(cmd)

    @allure.story('0001.打开导航')
    def test_case1(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(1.5)
        play("打开导航", path.men_qa_file)
        time.sleep(25)
        result = img_match.picture_match(self.driver,["03.png","04.png","05.png"])
        print('result',result)
        self.GDL.get_device_log()
        start_time = self.GDL.get_begin_parse()
        print("atart_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print('check_time',check_time)
        ck.check(check_time,result,'导航case1')

    @allure.story('0002.导航到家，港惠新天地')
    def test_case2(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time", wake_finish_time)
        time.sleep(1.5)
        play("导航到家", path.men_qa_file)
        time.sleep(3)
        play("港惠新天地", path.men_qa_file)
        time.sleep(30)
        # result = img_match.picture_match(self.driver,"02.png")
        self.GDL.get_device_log()
        result = self.GDL.get_last_ret("导航路线")
        start_time = self.GDL.get_begin_parse()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print('check_time',check_time)
        ck.check(check_time,result,'导航case2')

    @allure.story('0003.到红花湖怎么走')
    def test_case3(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time", wake_finish_time)
        time.sleep(2)
        play("到红花湖", path.men_qa_file)
        time.sleep(20)
        play("第一个",path.men_qa_file)
        time.sleep(20)
        play("第二个",path.men_qa_file)
        time.sleep(20)
        self.GDL.get_device_log()
        result = self.GDL.get_last_ret("导航路线")
        start_time = self.GDL.get_begin_parse()
        print("atart_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print('check_time',check_time)
        ck.check(check_time,result,'导航case3')

    @allure.story('0004.导航去红花湖')
    def test_case4(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time", wake_finish_time)
        time.sleep(2)
        play("导航去红花", path.men_qa_file)
        time.sleep(20)
        play("第二个", path.men_qa_file)
        time.sleep(20)
        play("第一个", path.men_qa_file)
        time.sleep(20)
        self.GDL.get_device_log()
        result = self.GDL.get_last_ret("个导航路线")
        start_time = self.GDL.get_begin_parse()
        print("atart_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print('check_time',check_time)
        ck.check(check_time,result,'导航case4')

    @allure.story('0005.去红花湖')
    def test_case5(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time", wake_finish_time)
        time.sleep(2)
        play("去红花湖", path.men_qa_file)
        time.sleep(20)
        play("第一个", path.men_qa_file)
        time.sleep(20)
        play("第二个", path.men_qa_file)
        time.sleep(20)
        self.GDL.get_device_log()
        result = self.GDL.get_last_ret("导航路线")
        self.GDL.get_device_log()
        start_time = self.GDL.get_begin_parse()
        print("atart_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print('check_time',check_time)
        ck.check(check_time,result,'导航case5')

    @allure.story('0006.带我去红花湖')
    def test_case6(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time", wake_finish_time)
        time.sleep(2)
        play("带我去红花", path.men_qa_file)
        time.sleep(20)
        play("第一个", path.men_qa_file)
        time.sleep(20)
        play("第二个", path.men_qa_file)
        time.sleep(30)
        self.GDL.get_device_log()
        result = self.GDL.get_last_ret("导航路线")
        start_time = self.GDL.get_begin_parse()
        print("atart_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print('check_time',check_time)
        ck.check(check_time,result,'导航case6')

    @allure.story('0007.红花湖附近的停车场')
    def test_case7(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time", wake_finish_time)
        time.sleep(2)
        play("红花湖附近", path.men_qa_file)
        time.sleep(20)
        play("第一个", path.men_qa_file)
        time.sleep(20)
        play("第二个", path.men_qa_file)
        time.sleep(20)
        self.GDL.get_device_log()
        result = self.GDL.get_last_ret("个导航路线")
        start_time = self.GDL.get_begin_parse()
        print("atart_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print('check_time',check_time)
        ck.check(check_time,result,'导航case7')

    @allure.story('0008.关闭导航')
    def test_case8(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time", wake_finish_time)
        time.sleep(1.5)
        play("关闭导航", path.men_qa_file)
        time.sleep(10)
        self.GDL.get_device_log()
        # 将为您退出导航,好的，收到，遵命
        result = self.GDL.get_last_ret("退出导航|好的|收到|遵命")
        start_time = self.GDL.get_begin_parse()
        print("atart_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print('check_time',check_time)
        ck.check(check_time,result,'导航case8')



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


# if __name__ == "__main__":
#     ask = Test_Wake_ask()
#     # ask.test_case1()
#     ask.test_case2()
#     ask.test_case3()
#     ask.test_case4()
#     ask.test_case5()
#     ask.test_case6()
#     ask.test_case7()
#     ask.test_case8()