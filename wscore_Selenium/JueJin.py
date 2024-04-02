from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time as time


# 该脚本：掘金平台一次性完成“签到+抽奖+沾喜气”,最好一天只运行一次
# 必须有谷歌浏览器，并且谷歌内核不低于75版本
# 必须安装webdriver驱动，并且登陆好账号
# 注意：下方有一处涉及到需手动修改的内容，请阅读注释


class JueJin:
    def __init__(self):
        option_save = EdgeOptions()
        option_save.use_chromium = True
        # 将cookie保存起来，下方的C：......中涉及到的文件，需要根据本人的User Data文件夹路径来修改
        option_save.add_argument(r"user-data-dir=C:\Users\ASUS\AppData\Local\Google\Chrome\User Data")
        self.driver = Edge(options=option_save)

    def SignIn(self):
        self.driver.maximize_window()
        self.driver.get('https://juejin.cn/user/center/signin')  # 签到页面
        time.sleep(0.1)
        search = self.driver.find_element(By.XPATH, "//button[@class='signin btn']")
        search.click()
        time.sleep(2)

    def LotteryDraw(self):
        self.driver.get('https://juejin.cn/user/center/lottery')  # 抽奖
        time.sleep(1.5)
        search1 = self.driver.find_element(By.XPATH, "//div[@class='text text-free']")
        search1.click()
        time.sleep(3)

    def Thumb_up(self):
        self.driver.get('https://juejin.cn/user/center/lottery')  # 点一下“沾”
        time.sleep(1.5)
        search2 = self.driver.find_element(By.CLASS_NAME, 'stick-btn')
        search2.click()
        time.sleep(3)


if __name__ == '__main__':
    jue = JueJin()
    try:
        jue.SignIn()
    except Exception as e:
        # jue.Thumb_up()
        jue.LotteryDraw()
        print("发生异常:", e)

    else:
        jue.LotteryDraw()
        # jue.Thumb_up()
    finally:
        print("《《《《 脚本运行结束 《《《《")
