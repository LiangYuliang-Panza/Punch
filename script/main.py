import unittest
from time import strftime
from tools import HwTestReport

# 创建测试套件
suite = unittest.TestLoader().discover(".", "test*.py")
# 执行测试套件，并将测试结果写入HTML报告，存放到report目录
# （HwTestReport工具是基于TextTestRunner类开发的第三方库，可以驱动测试套件的同时，生成精美的报告）
with open(f"../report/punch_{strftime('%Y_%m_%d %H_%M_%S')}.html", "wb") as f:
    HwTestReport.HTMLTestReport(stream=f,
                                verbosity=2,
                                title=f"自动打卡器——{strftime('%Y_%m_%d')}执行报告",
                                tester="梁宇亮").run(suite)