# Step-1
from flask import Flask
# Step-2
app=Flask(__name__)
# Step-3
@app.route('/wiki')
def demo():
    return 'Hello!!! Welcome to routing concept.'
@app.route('/hari')
def demo1():
    return 'Hello Hari!'
@app.route('/home/<name>')
def demo2(name):
    return 'Hello '+name
# Step-4
if __name__ == '__main__':
    app.run(debug=True)