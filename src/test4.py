# -*- coding: utf-8 -*-
'''
Created on 2018年11月20日

@author: uidq1501
'''

from utils.play_aidio import play
import settings.DIR_PATH as path
from utils import get_device_log as gdl
from utils import img_match
import pytest,time,allure
from utils import check_time_and_result as ck
from utils.driver import Driver
from config import *
from utils import get_mic_status
from src.wake_up_rate_function2 import single_wake_rate
@allure.feature("通话测试")
@pytest.mark.P2
class Test_wake:
    
    # @classmethod
    # def setUpClass(cls):
    #     log.logging.info('***************请注意，测试开始***************')
    #
    # @classmethod
    # def tearDownClass(cls):
    #     log.logging.info('***************请开心，所有case测试结束***************')
    #
    # def setUp(self):
    #     pass
    #
    # def clear(self):
    #     print ('this is clear')
    #
    # def tearDown(self):
    #     log.logging.info('******本条case测试结束******')

    def action(self,arg1):
        run = single_wake_rate(arg1)
#     def action(self,arg1,arg2):
#         pass

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.action(arg1)
        return func

def __generateTestCases():
        
    for args in range(10):
        setattr(Test_wake, 'test_func_%s'%(args),Test_wake.getTestFunc(args))



if __name__ =='__main__':
    __generateTestCases()