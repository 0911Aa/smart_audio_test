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
        if check_time>=5:
            print("\033[7;44mcase1唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase1唤醒成功\033[0m")

        if result:
            print("\033[7;31mcase1测试通过\033[0m")
            play("我代表中央", path.men_handle_file)
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
        play("后天会下雨", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("惠州后天|天气情况")
        if check_time>=5:
            print("\033[7;44mcase2唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase2唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase2测试通过\033[0m")
            play("我代表中央", path.men_handle_file)
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
        play("明天有没有", path.men_handle_file)
        time.sleep(40)
        # 惠州明天会下雨，天气情况是：暴雨转雷阵雨，25至29℃，微风(无持续风向)。雨天请您带好雨具，路面湿滑，出行注意安全。
        self.GDL.get_device_log()
        start_time, new_result = self.GDL.get_device_wake()
        print("start_time",start_time)
        check_time = abs(wake_finish_time-start_time)
        print(check_time)
        result = self.GDL.get_last_4_ret("惠州后天|天气情况")
        if check_time>=5:
            print("\033[7;44mcase3唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase3唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase3测试通过\033[0m")
            play("我代表中央", path.men_handle_file)
        else:
            print("\033[7;44mcase3测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case3\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase4唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase4唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase4测试通过\033[0m")
            play("我代表中央", path.men_handle_file)
        else:
            print("\033[7;44mcase4测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case4\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase5唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase5唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase5测试通过\033[0m")
            play("我代表中央", path.men_handle_file)
        else:
            print("\033[7;44mcase5测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case5\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase6唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase6唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase6测试通过\033[0m")
            play("我代表中央", path.men_handle_file)
        else:
            print("\033[7;44mcase6测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case6\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase7唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase7唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase7测试通过\033[0m")
            play("我代表中央", path.men_handle_file)
        else:
            print("\033[7;44mcase7测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case7\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase8唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase8唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase8测试通过\033[0m")
            play("我代表中央", path.men_handle_file)
        else:
            print("\033[7;44mcase8测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case8\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase9唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase9唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase9测试通过\033[0m")
            play("我代表中央", path.men_handle_file)
        else:
            print("\033[7;44mcase9测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case9\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase10唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase10唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase10测试通过\033[0m")
            play("我代表中央", path.men_handle_file)
        else:
            print("\033[7;44mcase10测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case10\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase11唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase11唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase11测试通过\033[0m")
        else:
            print("\033[7;44mcase11测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case11\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase12唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase12唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase12测试通过\033[0m")
        else:
            print("\033[7;44mcase12测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case12\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase13唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase13唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase13测试通过\033[0m")
        else:
            print("\033[7;44mcase13测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case13\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase14唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase14唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase14测试通过\033[0m")
        else:
            print("\033[7;44mcase14测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case14\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase15唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase15唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase15测试通过\033[0m")
        else:
            print("\033[7;44mcase15测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case15\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase16唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase16唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase16测试通过\033[0m")
        else:
            print("\033[7;44mcase16测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case16\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase17唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase17唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase17测试通过\033[0m")
        else:
            print("\033[7;44mcase17测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case17\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase18唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase18唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase18测试通过\033[0m")
        else:
            print("\033[7;44mcase18测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case18\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase19唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase19唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase19测试通过\033[0m")
        else:
            print("\033[7;44mcase19测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case19\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase20唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase20唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase20测试通过\033[0m")
        else:
            print("\033[7;44mcase20测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case20\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase21唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase21唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase21测试通过\033[0m")
        else:
            print("\033[7;44mcase21测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case21\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase22唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase22唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase22测试通过\033[0m")
        else:
            print("\033[7;44mcase22测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case22\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase23唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase23唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase23测试通过\033[0m")
        else:
            print("\033[7;44mcase23测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case23\\"
            subprocess.call(cmd)

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
        if check_time>=5:
            print("\033[7;44mcase24唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase24唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase24测试通过\033[0m")
        else:
            print("\033[7;44mcase24测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case24\\"
            subprocess.call(cmd)

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
        result = self.GDL.get_last_4_ret("最低温度|成都后天天气情况是")
        if check_time>=5:
            print("\033[7;44mcase25唤醒失败\033[0m")
            result = False
        else:
            print("\033[7;31mcase25唤醒成功\033[0m")
        if result:
            print("\033[7;31mcase25测试通过\033[0m")
        else:
            print("\033[7;44mcase25测试失败\033[0m")
            fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " +path.DIR_PATH+"\\report\\error_log\\"+fail_dir_name+"case25\\"
            subprocess.call(cmd)

if __name__ == "__main__":
    ask = Music_ask()
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
    ask.test_case25()