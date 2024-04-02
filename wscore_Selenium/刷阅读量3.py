import requests
from fake_useragent import UserAgent
ua = UserAgent()


def load_page(url):
    headers = {
        "User-Agent": ua.random
    }
    # proxy_list = [
    #     {'http': 'http://175.178.223.138:8088'}
    # ]
    proxy_list = [
        {'http': 'http://222.74.73.202:42055'},
        {'http': 'http://61.216.156.222:60808'},
        {'http': 'http://27.42.168.46:55481'},
        {'http': 'http://61.164.39.68:53281'}
    ]
    # 使用代理服务器发送GET请求，接收服务器返回的响应
    # response = requests.get(url, headers=headers)
    # return response.text
    for per_ip in proxy_list.copy():
        try:
            response = requests.get(url, headers=headers, proxies=per_ip, timeout=5)
        except:
            print(f"IP地址：{per_ip['http']}无效")
            proxy_list.remove(per_ip)
        else:
            print(f"IP地址：{per_ip['http']}有效")  # 若IP有效则返回状态码
            print("状态码为：" + str(response.status_code))


if __name__ == "__main__":
    for j in range(9999999):
        for i in range(10):
            print(f"第{j+1}次")
            if i == 1:
                base_url = 'https://blog.csdn.net/tanz10086/article/details/128835171'
                print("记录一个CentOS 6版本中，yum install 命令无法实现的问题 # 谭子")
            elif i == 2:
                base_url = 'https://blog.csdn.net/tanz10086/article/details/127524278'
                print('腾讯云服务器/Windows Server 2012 R2 上搭载web服务 动态图图解（http协议）# 谭子')
            elif i == 3:
                base_url = 'https://blog.csdn.net/weixin_63519461/article/details/128316021'
                print("MyBatis 万字长文：从入门到动态SQL超详细")
            elif i == 4:
                base_url = 'https://blog.csdn.net/weixin_63519461/article/details/127937850'
                print("红黑树的插入与验证——附图详解")
            elif i == 5:
                base_url = 'https://blog.csdn.net/weixin_63519461/article/details/127795857'
                print("垃圾回收机制——GC详讲")
            elif i == 6:
                base_url = 'https://blog.csdn.net/tanz10086/article/details/124446995'
                print("我自己动手写一个网页收藏站，你说行不行？【html+css+js】#谭子")
            elif i == 7:
                base_url = 'https://blog.csdn.net/tanz10086/article/details/127495140'
                print("Python学生信息管理系统（增删查改、模糊查找、txt文件输出）# 谭子")
            elif i == 8:
                base_url = 'https://blog.csdn.net/weixin_63519461/article/details/126320794'
                print("锁策略 和 CAS 和 synchronized 的自适应过程 学习总结")
            elif i == 9:
                base_url = 'https://blog.csdn.net/tanz10086/article/details/127616888'
                print("Python模拟银行管理系统（面向对象）# 谭子")
        # elif i == 10:
        #     print('结束')
        #     break
            else:
                base_url = 'https://blog.csdn.net/weixin_63519461/article/details/126349406'
                print("HashMap, Hashtable, ConcurrentHashMap 之间的区别")
            load_page(base_url)

