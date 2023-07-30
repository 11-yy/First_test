

"""Flask 将表单数据提交到模板"""

from flask import Flask, render_template, request
from werkzeug.wrappers.response import ResponseStream

app = Flask(__name__)

@app.route('/')
def student():
    return render_template('index5.html')
#个人理解：rendertamplate就是链接flask到html的函数

@app.route('/result',methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        rst = request.form
        return render_template("result5.html", result=rst)


if __name__ == "__main__":
    app.run(debug=True, threaded = True)
