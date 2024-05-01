from DrissionPage import ChromiumPage, ChromiumOptions
from csTime.wscore_drissionpage.py_script.__init__ import read_chrome_options
import time as time


class JueJin:
    def __init__(self):
        read_chrome_options(self)
        self.co = ChromiumOptions().set_paths(browser_path=f"{self.browser_path}",
                                              user_data_path=f"{self.user_data_dir}",
                                              local_port=9999
                                              )
        # self.co.set_argument('--window-size', '20000,10000')
        self.page = ChromiumPage(self.co)

    def SignIn(self):  # 签到页面
        self.page.get('https://juejin.cn/user/center/signin', retry=3, interval=2, timeout=15)
        time.sleep(1.0)
        # self.page.ele("x://button[@class='signin btn']").click()
        self.page.ele('x// *[ @ id = "juejin"] / div[1] / main / div[2] / div / div[1] / div[2] / div[2] / div[2] / '
                      'div[1] / button')
        time.sleep(2)

    # open('https://juejin.cn/user/center/signin')

    def LotteryDraw(self):  # 抽奖
        self.page.get("https://juejin.cn/user/center/lottery")
        time.sleep(1.0)
        self.page.ele("x://div[@class='text text-free']").click()
        time.sleep(5)

    def Thumb_up(self):  # 点一下“沾”
        self.page.get('https://juejin.cn/user/center/lottery')
        time.sleep(1.0)
        self.page.ele(".:stick-btn").click()
        time.sleep(2)

    def Quit(self):
        self.page.quit()


if __name__ == '__main__':
    juejin_instance = JueJin()
    juejin_instance.SignIn()
    juejin_instance.LotteryDraw()
    juejin_instance.Quit()
