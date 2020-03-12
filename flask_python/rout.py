from flask import Flask
app = Flask(__name__) # khai báo 1 thể hiện class flask và được sử dụng xuyên suốt chương trình

@app.route('/') # dùng để chỉ định hàm phía dưới nó, ở đây home() sẽ được thực thi khi truy cập vào root url of website

def home():
    return 'home page'

@app.route('/user')
def user():
    return 'user page'

@app.route('/about')
def about():
    return 'about page'

if __name__ == '__main__':
    app.run()
