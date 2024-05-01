from flask import Flask, send_from_directory
from flask_cors import CORS

from csTime.wscore_drissionpage.py_script.Daily import Daily
from csTime.wscore_drissionpage.py_script.ShengTen import ShengTen
from csTime.wscore_drissionpage.py_script.JueJin import JueJin

app = Flask(__name__)
CORS(app)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.root_path,
                               'static/favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/ShengTen')
def run_ShengTen():
    try:
        # 在视图函数内部创建 ShengTen 实例
        ShengTen_instance = ShengTen()
        # ShengTen_instance.read_credentials()
        ShengTen_instance.LogIn()
        ShengTen_instance.SignIn()
        ShengTen_instance.Quit()
        return '昇腾签到成功'
    except Exception as e:
        return f'昇腾签到任务执行失败：{e},\n请手动签到'


@app.route('/JueJin')
def run_JueJin():
    try:
        # 在视图函数内部创建 JueJin 实例
        JueJin_instance = JueJin()
        JueJin_instance.SignIn()
        JueJin_instance.LotteryDraw()
        return '掘金签到成功'
    except Exception as e:
        return f'掘金签到任务执行失败：{e},\n请手动签到'
    finally:
        JueJin_instance = JueJin()
        JueJin_instance.Quit()


@app.route('/Daily')
def run_Daily():
    try:
        Daily_instance = Daily()
        Daily_instance.HeyWhale()
        Daily_instance.BiliBili()
        Daily_instance.CSDN()
        return '日常上线成功'
    except Exception as e:
        return f'掘金签到任务执行失败：{e},\n请手动签到'
    finally:
        Daily_instance = Daily()
        Daily_instance.Quit()


if __name__ == '__main__':
    app.run(host='192.168.1.101', debug=True, port=8033)
    # http://192.168.1.101:8033/ShengTen
    while True:
        pass
