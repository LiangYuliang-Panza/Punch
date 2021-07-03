from time import sleep
from unittest import TestCase
from parameterized import parameterized
from base.get_data import get_data
from base.get_driver import GetDriver
from base.get_logger import GetLogger
from page import page

# 获取日志器
logger = GetLogger().get_logger()
res = []


class TestCommit(TestCase):
    """提交测试类——业务层"""

    def setUp(self):
        """初始化浏览器驱动对象"""
        try:
            self.driver = GetDriver().get_driver(
                url="https://stuhealth.jnu.edu.cn/#/login")
        except Exception as e:
            logger.error(msg=f"异常：{e}")

    def tearDown(self):
        """关闭浏览器驱动"""
        try:
            GetDriver().driver_quit()
        except Exception as e:
            logger.error(msg=f"异常：{e}")

    @parameterized.expand(get_data())
    def test_case_001(self, args):
        """业务流程及断言"""
        try:
            # 获取 登录页 页面对象
            login_page = page.Page(self.driver).get_login_page
            # 登录
            login_page.page_input_student_num(args["student_num"])
            login_page.page_input_password(args["password"])
            login_page.page_click_login()
            # 判断用户今日是否已进行过打卡操作，如果是完成页则不进行提交操作
            if "complete" not in self.driver.current_url:
                # 获取 提交页 页面对象
                commit_page = page.Page(self.driver).get_commit_page
                # 输入 今日体温
                commit_page.page_input_temperature(args["today_temperature"])
                # 点击 健康状况单选框
                commit_page.page_click_is_healthy(args["today_health_status"])
                # 点击 所在地单选框
                commit_page.page_click_address(args["current_location"])
                # 如果更新为在校状态，输入房号
                if args["current_location"] == "在校":
                    commit_page.page_input_the_room(args["room"])
                # 点击 个人承诺复选框
                commit_page.page_click_promise_checkbox()
                # 点击提交
                commit_page.page_click_commit()
            else:
                logger.warning(f"[script]:用户'{args['name']}'今日已打卡")
                res.append(f"用户'{args['name']}'今日已打卡")
                return
            # 获取 完成页 页面对象
            complete_page = page.Page(self.driver).get_complete_page
            # 断言是否成功提交
            result = complete_page.page_punch_is_successful()
            logger.info(
                f"[script]:正在断言用户{args['name'], args['student_num']}是否打卡成功")
            self.assertTrue(result)
            logger.info(
                f"[script]:用户{args['name'], args['student_num']}打卡{'成功' if result else '失败'}")
            res.append(
                f"用户{args['name'], args['student_num']}打卡{'成功' if result else '失败'}")
        except Exception as e:
            logger.error(msg=f"异常：{e}")
            res.append(f"用户{args['name'], args['student_num']}打卡异常：{e}")

    @classmethod
    def tearDownClass(cls):
        for i in res:
            print(i)
