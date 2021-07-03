from page import page_login
from page import page_commit
from page import page_complete


# 模仿工厂设计模式，封装工厂类，专门用于实例化各个页面的对象
class Page(object):
    """实例化页面类"""

    def __init__(self, driver):
        self.driver = driver

    @property
    def get_login_page(self):
        """获取 登录首页对象"""
        return page_login.PageLogin(self.driver)

    @property
    def get_commit_page(self):
        """获取 提交信息页对象"""
        return page_commit.PageCommit(self.driver)

    @property
    def get_complete_page(self):
        """获取 完成页对象"""
        return page_complete.PageComplete(self.driver)
