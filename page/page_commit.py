from selenium.webdriver.common.by import By

from base.base import BaseHandle
from base.get_logger import GetLogger

logger = GetLogger().get_logger()


class PageCommit(BaseHandle):
    """信息提交页——操作层"""
    temperature_editor = By.CSS_SELECTOR, "#temperature"
    healthy_radio = By.CSS_SELECTOR, "[for='150']"
    unhealthy_radio = By.CSS_SELECTOR, "[for='250']"
    at_home_radio = By.CSS_SELECTOR, "[for='1500']"
    at_school_radio = By.CSS_SELECTOR, "[for='3500']"
    room_number = By.CSS_SELECTOR, "#person_c4"
    promise_checkbox = By.CSS_SELECTOR, r"#\31 0000"
    commit_btn = By.CSS_SELECTOR, "#tj"

    def page_input_temperature(self, temp):
        """输入今日体温"""
        logger.info(f"[page_commit]:正在输入今日体温：'{temp}℃'")
        self.base_input(self.temperature_editor, temp)

    def page_click_radio(self, text):
        """根据文本选择单选框"""
        radio = By.XPATH, f"//*[@text()='{text}']"  # TODO:检查这里是不是BUG源头
        logger.info(f"[page_commit]:正在点击单选框：'{text}'")
        self.base_click(radio)

    def page_click_promise_checkbox(self):
        """检查 “本人承诺上述真实”复选框 是否已被选择"""
        logger.info(f"[page_commit]:正在检查“本人承诺上述情况真实”的复选框是否已点选")
        promise = self.base_find_element(self.promise_checkbox)
        if not promise.is_selected():
            logger.info(f"[page_commit]:“本人承诺上述情况真实”的复选框未点选，正在点击")
            promise.click()
        else:
            logger.info(f"[page_commit]:“本人承诺上述情况真实”的复选框已点选")

    def page_click_commit(self):
        """点击提交"""
        logger.info(f"[page_commit]:已填写完所有信息，正在点击提交按钮")
        self.base_click(self.commit_btn)

    def page_click_is_healthy(self, text):
        """点击 身体状况 单选框"""
        if text == "正常":
            logger.info(f"[page_commit]:正在点击'正常'单选框")
            self.base_click(self.healthy_radio)
        else:
            logger.info(f"[page_commit]:正在点击'不适'单选框")
            self.base_click(self.unhealthy_radio)

    def page_click_address(self, text):
        """点击 所在地 单选框"""
        if text == "在家":
            logger.info(f"[page_commit]:正在点击'在家'单选框")
            self.base_click(self.at_home_radio)
        else:
            logger.info(f"[page_commit]:正在点击'在校'单选框")
            self.base_click(self.at_school_radio)

    def page_input_the_room(self, room):
        """从其它状态更改为在校状态时输入房号"""
        self.base_input(self.room_number, room)
