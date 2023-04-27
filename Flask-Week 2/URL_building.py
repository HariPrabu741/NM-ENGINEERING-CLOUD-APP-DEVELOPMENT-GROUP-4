# Step-1
from flask import *
# Step-2
app = Flask(__name__)
# Step-3
@app.route('/login')
def login():
    return 'Login'
@app.route('/signup')
def signup():
    return 'Signup'
@app.route('/newsfeed')
def newsfeed():
    return 'NewsFeed'
@app.route('/user/<name>')
def user(name):
    if name=='Hari':
        return redirect(url_for('login'))
    if name=='signup':
        return redirect(url_for('signup'))
    if name=='newsfeed':
        return redirect(url_for('newsfeed'))
# Step-4
if __name__ == '__main__':
    app.run(debug=True)