from time import sleep

from selenium.webdriver.common.by import By

from base.base import BaseHandle
from base.get_logger import GetLogger

logger = GetLogger().get_logger()


class PageLogin(BaseHandle):
    """登录页类——操作层"""
    student_num_editor = By.CSS_SELECTOR, "#zh"
    password_editor = By.CSS_SELECTOR, "#passw"
    login_btn = By.CSS_SELECTOR, ".btn"

    def page_input_student_num(self, username):
        """输入账户名"""
        logger.info(f"[page_login]:正在输入账号：'{username}'")
        self.base_input(self.student_num_editor, username)

    def page_input_password(self, pwd):
        """输入密码"""
        logger.info(f"[page_login]:正在输入密码：'{pwd}'")
        self.base_input(self.password_editor, pwd)

    def page_click_login(self):
        """点击登录"""
        logger.info(f"[page_login]:正在点击登录按钮")
        self.base_click(self.login_btn)
        sleep(1)
