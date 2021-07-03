from time import sleep
from selenium.webdriver.common.by import By
from base.base import BaseHandle
from base.get_logger import GetLogger


logger = GetLogger().get_logger()


class PageComplete(BaseHandle):
    """完成页类——操作层"""
    success_prompt_text = By.XPATH, "//*[text()='您已完成今天的健康状态申报')]"

    def page_punch_is_successful(self):
        """判断打卡是否成功"""
        logger.info("[page_complete]正在判断打卡是否成功")
        sleep(1)
        return "complete" in self.driver.current_url
