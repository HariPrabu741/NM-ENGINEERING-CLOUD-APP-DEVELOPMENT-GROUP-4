from flask import *
app = Flask(__name__)
@app.route('/')
def lg():
    return render_template('login.html')
@app.route('/login',methods=['GET'])
def login():
    un = request.args.get('un')
    ps = request.args.get('pas')

    if un == 'Hari' and ps == '123':
        return 'Hello '+un+'!!!!'
if __name__ == '__main__':
    app.run(debug=True)