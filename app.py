from flask import Flask, jsonify

# 初始化 Flask 应用
app = Flask(__name__)

# 定义路由：访问根路径（/）时执行的函数
@app.route('/')
def hello_world():
    return "Hello, Flask! 这是我的第一个服务端程序"

# 定义带参数的路由：例如访问 /user/张三，会返回对应内容
@app.route('/user/<name>')
def get_user(name):
    return f"你好，{name}！"

# 定义一个返回 JSON 数据的接口（实际开发中常用）
@app.route('/api/data')
def get_data():
    data = {
        "name": "Flask 教程",
        "version": "1.0",
        "features": ["简单", "轻量", "灵活"]
    }
    # jsonify 会自动把字典转为 JSON 格式，并设置正确的响应头
    return jsonify(data)

# 启动服务（只有在直接运行该文件时才执行）
if __name__ == '__main__':
    # debug=True 表示开启调试模式（代码修改后自动重启），host='0.0.0.0' 允许外部访问
    app.run(debug=True, host='0.0.0.0', port=5000)
