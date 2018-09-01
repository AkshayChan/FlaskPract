from flask import Flask, url_for, request
import os
app = Flask(__name__)

#1
@app.route('/')
def index():
    return url_for('show_user', username = 'Akshay') #reference the function not URL
 
#2 - GET Contains username in the url, can't do    
@app.route('/lgin', methods=['GET'])
def login():
    if request.values:
        return "Username is " + request.values["username"]
    else:
        return '<form method="get" action="/login"><input text="type" name="username"><p><button type="submit">Submit</button></form>'

#3 - POST - need GET too as first time we hit url - GET
@app.route('/lgin', methods=['GET', 'POST'])
def lgin():
    if request.method == 'POST':
        return "Username is " + request.values["username"]
    else:
        return '<form method="post" action="/lgin"><input text="type" name="username"><p><button type="submit">Submit</button></form>'

#4 - variable
@app.route ('/user/<username>')
def show_user(username):
    return "Hello" + " " + str(username) #or return "Hello %s" $ username
    
#5 - int variable
@app.route('/user/<int:post>')
def show_post(post):
    return "This is post" + " " + str(post) #or return "Hello %d" $ post

#6 - debugger
@app.route('/hello')
def hello_world():
    #important for debugging
    #import pdb; pdb.set_trace()
    return "Hello World"
    
if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run(host = host, port = port)