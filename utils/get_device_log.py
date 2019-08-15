# -*- coding: utf-8 -*-
import subprocess
import settings.DIR_PATH as path
import re,time,os

class Get_device_log:
    def get_local_time(self):
        local_time = time.strftime("%X")
        print(local_time)
        ret_time = int(local_time.split(":")[1]) * 60 + float(local_time.split(":")[2])
        return ret_time

    def get_device_log(self):
        """
        获取车机的log，推送到本地
        :return:
        """
        cmd = "adb pull sdcard/txz/log "+path.device_log_path
        subprocess.call(cmd,shell=True)
        # p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        file_list = os.listdir(path.device_log_path+"\\log")
        # print(file_list)
        if "text_all_1" in file_list:
            with open(path.device_log_path+"\\log\\text_all_1",'r',encoding="utf-8") as f1:
                # data1 = f1.readlines()
                data1 = f1.read()
            with open(path.device_log_path+"\\log\\text_all",'r',encoding="utf-8") as f2:
                data2 = f2.read()
            with open(path.device_log_path+"\\text_all_new",'w',encoding="utf-8") as f3:
                # f3.writelines(data1[-500:])
                f3.write(data1)
                time.sleep(1)
                f3.write(data2)
        else:
            with open(path.device_log_path+"\\log\\text_all",'r',encoding="utf-8") as f2:
                data2 = f2.read()
            with open(path.device_log_path+"\\text_all_new",'w',encoding="utf-8") as f3:
                time.sleep(1)
                f3.write(data2)


    def get_begin_parse(self):
        """
        获取log中收到唤醒词的时间
        :return:
        """
        with open(path.device_log_path+"\\text_all_new","r",encoding="utf-8") as f:
            data = f.readlines()
            parse_list = []
            for line in data:
                if "mWakeup onWakeUp text" in line:
                    # print(line)
                    parse_list.append(line)
            # print(parse_list)
            last_line = parse_list[-1]
            result_time = last_line.split(" ")[1].split("]")[0]
            ret_time = int(result_time.split(":")[1]) * 60 + float(result_time.split(":")[2])
            return ret_time

    def get_device_wake(self):
        """
        从log中获取车机被唤醒后的反馈
        :return:
        """

        with open(path.device_log_path+"\\text_all_new","r",encoding="utf-8") as f:
            data = f.readlines()
            result_list = []
            for line in data:
                if "speakText end:" in line:
                    # print(line)
                    result = re.findall("哈喽|您好|在呢",line)
                    if result:
                        # print(line)
                        result_list.append(line)
            # print(result_list)
            last_line = result_list[-1]
            # print(last_line)
            result_time = last_line.split(" ")[1].split("]")[0]
            new_result = last_line.split("text=")[1]
            ret_time = int(result_time.split(":")[1])*60+float(result_time.split(":")[2])
            # print(ret_time,new_result)
            return ret_time,new_result


if __name__ == "__main__":
    gl = Get_device_log()
    # gl.get_device_log()
    end_time = gl.get_device_wake()
    print(end_time)
    start_time = gl.get_begin_parse()
    print(start_time)
