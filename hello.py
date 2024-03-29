from flask import Flask, url_for, request, render_template
import os
app = Flask(__name__)

#Name not necessary
@app.route('/hello/<name>')
@app.route('/hello')
def hello(name=None):
    return render_template('hello.html', name_temp=name)
    
@app.route('/login_user', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
         return "User %s logged in" % request.form['username']
    return render_template('login.html')
    
if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run(host = host, port = port)