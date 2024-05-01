from DrissionPage import ChromiumPage, ChromiumOptions
from csTime.wscore_drissionpage.py_script.__init__ import read_chrome_options, read_credentials
import time as time


class ShengTen:
    def __init__(self):
        read_chrome_options(self)
        self.co = ChromiumOptions().set_paths(browser_path=f"{self.browser_path}",
                                              user_data_path=f"{self.user_data_dir}",
                                              local_port=9999
                                              )
        # self.co.set_argument('--window-size', '20000,10000')
        self.page = ChromiumPage(self.co)

    def LogIn(self):
        read_credentials(self)
        self.page.get('https://www.hiascend.com/login?validated=true', retry=3, interval=2, timeout=15)  # 跳转到登录页面
        # self.page.set.window.max()
        time.sleep(1.0)
        ClickID = self.page.ele('.:userAccount')
        ClickID.input(f"{self.id}")
        ClickPW = self.page.ele(
            'x://*[@id="hiascend"]/div/div[2]/div/div/div[1]/div/div/div/div[1]/form/div[3]/div[1]/input')
        ClickPW.input(f"{self.password}")
        self.page.ele('.:hwid-btn-primary').click()
        # self.page.cookies(as_dict=True)
        time.sleep(2)

    # open('https://www.hiascend.com/login?validated=true')

    def SignIn(self):
        self.page.get("https://www.hiascend.com/profile-signin")
        time.sleep(1)
        self.page.ele('x://*[@id="hiascend"]/div/main/div/div/div[2]/div/div/div[1]/div[2]/div[2]/button').click()
        time.sleep(2.5)

    def Quit(self):
        self.page.quit()


if __name__ == '__main__':
    shengten_instance = ShengTen()
    shengten_instance.LogIn()
    shengten_instance.SignIn()
    shengten_instance.Quit()
