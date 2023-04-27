# Step-1
from flask import Flask
# Step-2
app = Flask(__name__)
# Step-3
def demo():
    return 'This is an alternate method for routing.'
def demo1():
    return 'Welcome all!!!'

app.add_url_rule('/demo',"demo",demo)

app.add_url_rule('/','demo1',demo1)

# Step-4
if __name__ == '__main__':
    app.run(debug=True)