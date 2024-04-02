import random
import time
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
ua = UserAgent()


class WR:
    def __init__(self):
        options = EdgeOptions()
        options.use_chromium = True
        # 设置 Headless 模式
        # options.add_argument('--headless')
        # 读取本地浏览器cookie缓存，避免登录页面出现
        options.add_argument("user-data-dir=C:\\Users\\ASUS\\AppData\\Local\\Google\\Chrome\\User Data")
        driver = Edge(options=options)

        # 设置自定义请求头和网络模拟参数
        custom_headers = {
            "User-Agent": ua.random,
            'Accept-Language': 'en-US,en;q=0.9',
            # 在这里添加其他自定义请求头
        }
        network_conditions = {
            'offline': False,
            'latency': 5,  # 模拟网络延迟（毫秒）
            'download_throughput': 1024 * 1024,  # 下载速率（bytes/s）
            'upload_throughput': 1024 * 1024,  # 上传速率（bytes/s）
        }
        driver.set_network_conditions(
            offline=network_conditions['offline'],
            latency=network_conditions['latency'],
            download_throughput=network_conditions['download_throughput'],
            upload_throughput=network_conditions['upload_throughput'],
            connection_type='cellular2g',
            headers=custom_headers
        )

        driver.get("https://rewards.bing.com/redeem/pointsbreakdown")
        driver.implicitly_wait(1)  # 等待页面加载完全

        # 在当前浏览器实例中新建标签页
        driver.execute_script("window.open('about:blank', 'tab2');")
        # 切换到新建的标签页
        driver.switch_to.window("tab2")
        driver.get("https://cn.bing.com/")
        time.sleep(0.5)
        # driver.minimize_window()
        num01 = driver.find_element(By.ID, "id_rc")
        num00 = num01.text
        print(f"首次积分为 {num00}")
        print("-------------------------")
        for i in range(50):
            search_word = generate_random_phrase()
            time.sleep(0.9)
            driver.refresh()
            print(f"第{i + 1}次")
            input_box = driver.find_element(By.ID, "sb_form_q")
            input_box.clear()
            input_box.send_keys(search_word)
            input_box.send_keys(Keys.ENTER)
            time.sleep(0.8)
        num02 = driver.find_element(By.ID, "id_rc")
        print(num02.text)
        print("总分为 %s，本次获取 %s分,共成功 %s次" % (num02.text,
                                           int(num02.text) - int(num00),
                                           int((int(num02.text) - int(num00)) / 3)))
        driver.quit()


def generate_random_chinese(length):
    # 生成随机汉字
    random_chinese = ''.join([chr(random.randint(0x4e00, 0x9fff)) for _ in range(length)])
    return random_chinese


def generate_random_phrase(num_words=5):
    # 生成随机组合的词
    random_words = [generate_random_chinese(random.randint(1, 3)) for _ in range(num_words)]
    # 将词连接成短语并返回
    return ''.join(random_words)


if __name__ == '__main__':
    wr = WR()
    print("结束任务")
