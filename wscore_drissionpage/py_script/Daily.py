from DrissionPage import ChromiumPage, ChromiumOptions
from csTime.wscore_drissionpage.py_script.__init__ import read_chrome_options
import time as time


class Daily:
    def __init__(self):
        read_chrome_options(self)
        self.co = ChromiumOptions().set_paths(browser_path=f"{self.browser_path}",
                                              user_data_path=f"{self.user_data_dir}",
                                              local_port=9999
                                              )
        self.page = ChromiumPage(self.co)

    def HeyWhale(self):  # 和鲸上线经验
        self.page.get('https://www.heywhale.com/home')
        time.sleep(1.5)
        # 待补充的其他功能

    # open('https://www.heywhale.com/home')
    # open('https://www.bilibili.com/')

    def BiliBili(self):  # B站上线经验
        self.page.get("https://www.bilibili.com/")
        time.sleep(1.5)

    def CSDN(self):  # 这个CSDN充数的
        self.page.get("https://www.csdn.net/")
        time.sleep(1.5)

    def Quit(self):
        self.page.quit()
