from selenium import webdriver


class GetDriver(object):
    """单例设计模式——获取浏览器驱动对象类"""
    driver = None

    @classmethod
    def get_driver(cls, url):
        if not cls.driver:
            cls.driver = webdriver.Firefox()
            cls.driver.maximize_window()
            cls.driver.get(url)
        return cls.driver

    @classmethod
    def driver_quit(cls):
        """关闭浏览器驱动对象"""
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
