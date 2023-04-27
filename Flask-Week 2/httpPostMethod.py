from flask import *
app = Flask(__name__)

@app.route('/')
def lg():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['pas']
    if username == "Hari Prabu" and password == '12345':
        return 'Welcome '+username+'!!!'

if __name__ == '__main__':
    app.run(debug=True)