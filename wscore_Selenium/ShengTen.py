from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time as time


class ShengTen:
    def __init__(self):
        option = EdgeOptions()
        option.use_chromium = True
        option.add_argument(r"user-data-dir=C:\Users\ASUS\AppData\Local\Google\Chrome\User Data")
        self.driver = Edge(options=option)

    def LogIn(self):
        self.driver.maximize_window()
        self.driver.get("https://www.hiascend.com/login?validated=true")
        self.driver.implicitly_wait(1)  # 等待页面加载完全
        time.sleep(0.1)
        ClickPW = self.driver.find_element(By.CLASS_NAME, 'hwid-input-root')
        ClickPW.click()
        QR = self.driver.find_element(By.CLASS_NAME, 'qrcode-img-block')
        QR.click()
        Sign_in = self.driver.find_element(By.CLASS_NAME, 'hwid-btn')
        time.sleep(0.5)
        Sign_in.click()
        # time.sleep(2.5)

        self.driver.implicitly_wait(10)  # 等待页面加载完全
        time.sleep(1.5)
        u_name = self.driver.find_element(By.CLASS_NAME, 'user-name')
        u_name.click()
        sign_in = self.driver.find_element(By.CLASS_NAME, 'o-btn')
        time.sleep(2.5)
        sign_in.click()
        time.sleep(2.5)


    def SignIn(self):
        self.driver.get("https://www.hiascend.com/profile-signin")
        self.driver.implicitly_wait(1)  # 等待页面加载完全
        time.sleep(0.5)
        sign_in = self.driver.find_element(By.CLASS_NAME, 'o-btn')
        sign_in.click()
        time.sleep(2.5)

if __name__ == '__main__':
    ShengTen = ShengTen()
    try:
        ShengTen.LogIn()
    except Exception as e:
        ShengTen.SignIn()
        print("发生异常:", e)
    else:
        ShengTen.SignIn()
    finally:
        print("《《《《 脚本运行结束 《《《《")
