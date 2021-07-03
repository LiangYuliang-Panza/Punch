from selenium.webdriver.support.wait import WebDriverWait
from base.get_logger import GetLogger

# 获取日志器
logger = GetLogger().get_logger()


class BaseObject(object):
    """基类——对象库层"""

    def __init__(self, driver):
        logger.info(f"[base]:正在实例化浏览器驱动对象driver:{driver}")
        self.driver = driver

    def base_find_element(self, feature, timeout=30, freq=0.5):
        """显式等待定位元素方法"""
        logger.info(f"[base]:正在定位元素:<{feature}>，默认超时时间为{timeout}s")
        return WebDriverWait(driver=self.driver,
                             timeout=timeout,
                             poll_frequency=freq).until(
            lambda x: x.find_element(*feature))


class BaseHandle(BaseObject):
    """基类——操作层"""

    def base_click(self, feature):
        """点击操作"""
        logger.info(f"[base]:正在点击元素：<{feature}>")
        self.base_find_element(feature).click()

    def base_input(self, feature, val):
        """输入操作"""
        ele = self.base_find_element(feature)
        logger.info(f"[base]:正在清空元素<{feature}>的内容，准备输入")
        ele.clear()
        ele.clear()
        logger.info(f"[base]:正在向元素<{feature}>输入'{val}'")
        ele.send_keys(val)

    def base_element_is_existed(self, feature):
        """查找元素是否存在"""
        logger.info(f"[base]:正在查询元素：<{feature}>是否存在")
        try:
            self.base_find_element(feature, timeout=10, freq=0.1)
            logger.info(f"[base]:查找的元素<{feature}>存在")
            return True
        except Exception:
            logger.info(f"[base]:未找到元素<{feature}>")
            return False
