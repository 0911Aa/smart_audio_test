# -*- coding: utf-8 -*-
from utils.play_aidio import play
import time,subprocess,os
import settings.DIR_PATH as path
from utils import get_device_log as gdl
import uiautomator2 as u
import pytest,time,allure
from utils import check_time_and_result as ck
from utils.driver import Driver
from config import *

@allure.feature("天气问答测试")
@pytest.mark.P1
class Test_online_weather:
    def setup_class(cls):
        dr = Driver()
        cls.driver = dr.init_driver(device_name)
        cls.GDL = gdl.Get_device_log()

    def teardown(self):
        cmd = 'del /F /S /Q ' + path.log_path + "\\test_all_new"
        os.system(cmd)

    @allure.story('0001.明天雨大不大')
    def test_case1(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("明天雨大不", path.men_handle_file)
        time.sleep(40)
        # play("第一个", path.men_qa_file)
        # time.sleep(10)
        # result = img_match.picture_match(self.driver,"phone_call.png")
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("惠州明天|天气情况")
        ck.check(check_time, result, 'weather_case1')

    @allure.story('0002.后天会下雨吗')
    def test_case2(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("后天会下雨", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("惠州后天|天气情况")
        ck.check(check_time, result, 'weather_case2')

    @allure.story('0003.明天有没有雨')
    def test_case3(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("明天有没有", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("惠州后天|天气情况")
        ck.check(check_time, result, 'weather_case3')

    @allure.story('0004.后天啥天气')
    def test_case4(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("后天啥天气", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("惠州后天|天气情况")
        ck.check(check_time, result, 'weather_case4')

    @allure.story('0005.明天天气怎么样')
    def test_case5(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("明天天气怎", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("惠州明天|天气情况")
        ck.check(check_time, result, 'weather_case5')

    @allure.story('0006.后天有雨吗')
    def test_case6(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("后天有雨吗", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("惠州后天|天气情况")
        ck.check(check_time, result, 'weather_case6')

    @allure.story('0007.帮我查一下**的天气')
    def test_case7(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("帮我查一下", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("南昌今天天气情况")
        ck.check(check_time, result, 'weather_case7')

    @allure.story('0008.北京的天气怎么样')
    def test_case8(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("北京的天气", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("北京今天天气情况")
        ck.check(check_time, result, 'weather_case8')

    @allure.story('0009.查看上海的天气')
    def test_case9(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("查看上海的", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("上海今天天气情况")
        ck.check(check_time, result, 'weather_case9')

    @allure.story('0010.请问徐州的天气怎么样')
    def test_case10(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("请问徐州的", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("徐州今天天气情况")
        ck.check(check_time, result, 'weather_case10')

    @allure.story('0011.请问徐州的天气怎么样')
    def test_case11(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("深圳明天的", path.men_handle_file)
        time.sleep(40)
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("深圳明天的温度|深圳明天天气情况")
        ck.check(check_time, result, 'weather_case11')

    @allure.story('0012.深圳天气')
    def test_case12(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("深圳天气", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("深圳明天天气情况")
        ck.check(check_time, result, 'weather_case12')

    @allure.story('0013.深圳后天气温多少')
    def test_case13(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("深圳后天气", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("深圳后天的温度")
        ck.check(check_time, result, 'weather_case13')

    @allure.story('0014.深圳明天气温')
    def test_case14(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("深圳明天气", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("深圳明天的温度|深圳明天天气情况")
        ck.check(check_time, result, 'weather_case14')

    @allure.story('0015.北京明天天气')
    def test_case15(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("北京明天天", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("北京明天天气情况")
        ck.check(check_time, result, 'weather_case15')

    @allure.story('0016.北京后天气温')
    def test_case16(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("北京后天气温", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("北京后天天气情况|北京后天的温度")
        ck.check(check_time, result, 'weather_case16')

    @allure.story('0017.北京明天温度')
    def test_case17(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("北京明天温度", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("北京明天的温度")
        ck.check(check_time, result, 'weather_case17')

    @allure.story('0018.北京后天下雨吗')
    def test_case18(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("北京后天下雨", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("北京后天|天气情况")
        ck.check(check_time, result, 'weather_case18')

    @allure.story('0018.上海明天下雨吗')
    def test_case19(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("上海明天下雨", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("上海明天|天气情况")
        ck.check(check_time, result, 'weather_case19')

    @allure.story('0020.上海后天有雨吗')
    def test_case20(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("上海后天有雨", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("上海后天|天气情况")
        ck.check(check_time, result, 'weather_case20')

    @allure.story('0021.上海明天会下雨')
    def test_case21(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("上海明天会下雨", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("上海明天|天气情况")
        ck.check(check_time, result, 'weather_case21')

    @allure.story('0022.武汉明天天气')
    def test_case22(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("武汉明天天气", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("武汉明天天气情况")
        ck.check(check_time, result, 'weather_case22')

    @allure.story('0023.武汉后天天气')
    def test_case23(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("武汉后天天气", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("武汉后天天气情况")
        ck.check(check_time, result, 'weather_case23')

    @allure.story('0024.成都明天冷不冷')
    def test_case24(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("成都明天冷不冷", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("冷|最低温度|成都明天天气情况是")
        ck.check(check_time, result, 'weather_case24')

    @allure.story('0025.成都后天最低温度')
    def test_case25(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("成都后天最低温度", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("成都后天的温度是|成都后天天气情况是")
        ck.check(check_time, result, 'weather_case25')

    @allure.story('0026.成都明天多少度')
    def test_case26(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("成都明天多少度", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("成都明天的温度是|成都明天天气情况是")
        ck.check(check_time, result, 'weather_case26')

    @allure.story('0027.成都后天温度')
    def test_case27(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("成都后天的温度", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("成都后天的温度是|成都后天天气情况是")
        ck.check(check_time, result, 'weather_case27')

    @allure.story('0028.青岛明天的天气')
    def test_case28(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("青岛明天的天气", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("青岛明天天气情况是")
        ck.check(check_time, result, 'weather_case28')

    @allure.story('0029.青岛后天气温')
    def test_case29(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("青岛后天气温", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("青岛后天的温度是|青岛后天天气情况是")
        ck.check(check_time, result, 'weather_case29')

    @allure.story('0030.青岛明天会刮风')
    def test_case30(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("青岛明天会刮风", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("青岛明天|天气情况是")
        ck.check(check_time, result, 'weather_case30')

    @allure.story('0031.青岛后天是高温吗')
    def test_case31(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("青岛后天是高温", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("青岛后天的温度是|青岛后天天气情况是")
        ck.check(check_time, result, 'weather_case31')

    @allure.story('0032.我明天切乌鲁木齐要带伞吗')
    def test_case32(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("我明天去乌", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("乌鲁木齐明天|乌鲁木齐明天天气情况是")
        ck.check(check_time, result, 'weather_case32')

    @allure.story('0033.今天多少号')
    def test_case33(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("今天多少号", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("今天是二零..年")
        ck.check(check_time, result, 'weather_case33')

    @allure.story('0034.今天日期多少')
    def test_case34(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("今天日期多", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("今天是二零..年")
        ck.check(check_time, result, 'weather_case34')

    @allure.story('0035.今天星期几')
    def test_case35(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("今天星期几", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("今天是星期")
        ck.check(check_time, result, 'weather_case35')

    @allure.story('0036.查一下我的位置')
    def test_case36(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("查一下我的", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("您当前的位置是：广东省惠州市惠城区")
        ck.check(check_time, result, 'weather_case36')

    @allure.story('0037.我现在在哪')
    def test_case37(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("我现在在哪", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("您当前的位置是：广东省惠州市惠城区")
        ck.check(check_time, result, 'weather_case37')

    @allure.story('0038.我在哪里')
    def test_case38(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("我在哪里", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("您当前的位置是：广东省惠州市惠城区")
        ck.check(check_time, result, 'weather_case38')

    # @pytest.mark.P0
    @allure.story('0039.讲个笑话')
    def test_case39(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("讲个笑话", path.men_handle_file)
        time.sleep(40)
        # 孙子说:“爷爷，水牛是啥样子?”爷爷说：“水牛跟普通牛长的差不多，不同的是它喜欢在水中生活。”孙子说：“噢，我懂啦，它一定是喜欢吃鱼吧。,,,,
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("..................................")
        ck.check(check_time, result, 'weather_case39')

    # @pytest.mark.P0
    @allure.story('0040.红烧肉怎么做')
    def test_case40(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("红烧肉怎么", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，weather_情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("五花肉切|干净后")
        ck.check(check_time, result, 'weather_case40')

    # @pytest.mark.P0
    @allure.story('0041.中果最高的山')
    def test_case41(self):
        play('你好小西', path.wake_up_file)
        wake_finish_time = self.GDL.get_local_time()
        print("wake_finish_time",wake_finish_time)
        time.sleep(2)
        play("中国最高的", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("中国最高的山：珠穆朗玛峰")
        ck.check(check_time, result, 'weather_case41')
# if __name__ == "__main__":
#     ask = Music_ask()
    # ask.test_case1()
    # ask.test_case2()
    # ask.test_case3()
    # ask.test_case4()
    # ask.test_case5()
    # ask.test_case6()
    # ask.test_case7()
    # ask.test_case8()
    # ask.test_case9()
    # ask.test_case10()
    # ask.test_case11()
    # ask.test_case12()
    # ask.test_case13()
    # ask.test_case14()
    # ask.test_case15()
    # ask.test_case16()
    # ask.test_case17()
    # ask.test_case18()
    # ask.test_case19()
    # ask.test_case20()
    # ask.test_case21()
    # ask.test_case22()
    # ask.test_case23()
    # ask.test_case24()
    # ask.test_case25()
    # ask.test_case26()
    # ask.test_case27()
    # ask.test_case28()
    # ask.test_case29()
    # ask.test_case30()
    # ask.test_case31()
    # ask.test_case32()
    # ask.test_case33()
    # ask.test_case34()
    # ask.test_case35()
    # ask.test_case36()
    # ask.test_case37()
    # ask.test_case38()
    # ask.test_case39()
    # ask.test_case40()
    # ask.test_case41()