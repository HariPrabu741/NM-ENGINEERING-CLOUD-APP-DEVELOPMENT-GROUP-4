# Step-1: Import the required lib (Flask,...)
# Step-2: Initialize the flask
# Step-3: Write script to route and to do some actions
# Step-4: Run the app

# Step-1
from flask import Flask
# Step-2
app = Flask(__name__)
# Step-3
@app.route('/')
def demo():
    return "Welcome Hari!!! This is my 1st app with flask framework."
# Step-4
if __name__ == '__main__':
    app.run(debug=True)
