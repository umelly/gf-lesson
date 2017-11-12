# -*- coding: utf-8 -*-

from flask import Flask, request, url_for, redirect, \
    render_template, Response

# flask应用对象
app = Flask(__name__)

# app.config.from_envvar 从环境变量里面获取配置文件的路径
# app.config.from_object 以对象来配置app
# app.config.from_pyfile 以py文件来配置app
# 从类对象来配置app
class Config(object):
    DEBUG = True
app.config.from_object(Config)

# HTTP错误捕获处理
# 比如设置自定义的404,500错误页面
@app.errorhandler(404)
def page_not_found(error):
    return "page_not_found"

# 每个HTTP请求开始之前可以额外做的事情
@app.before_request
def before_request_():
    pass

# 每个HTTP请求之后的响应response对象做额外处理
@app.after_request
def after_request_(response):
    return response

@app.route("/")
def index():
    """
    返回内容
    > 不管返回什么内容,最后都会变成flask.wrapper.Response对象

    1. render_template(HTML_PATH), 
       render_template默认会读取项目下的templates目录下的文件
    2. 字符串
    3. flask Response对象
    """
    # return "hello,world"
    # return Response("hello,world")
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
