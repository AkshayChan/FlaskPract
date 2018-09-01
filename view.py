from flask import Flask, jsonify, request, render_template
app = Flask(__name__)
import os

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'


@app.route('/', methods=['GET'])
def main():
    user = {'username' : 'Akshay', 'name' : 'Cha'}
    return render_template('index.html', title="title", user=user)

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')
    
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')
    
@app.route('/cleaner', methods=['GET'])
def cleaner():
    return render_template('cleaner.html')
    
if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run(host = host, port = port)