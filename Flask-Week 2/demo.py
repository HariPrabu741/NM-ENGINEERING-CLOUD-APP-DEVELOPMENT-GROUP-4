from flask import *
app = Flask(__name__)
'''@app.route('/')
def dem():
    return "<html><body><h2>Hii, I'm Hari Prabu. Welcome to Flask app.</h2></body></html>"
'''
@app.route('/')
def dem():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    un = request.form['un']
    ps = request.form['pas']
    return render_template('output.html',name=un)
if __name__=='__main__':
    app.run(debug=True)