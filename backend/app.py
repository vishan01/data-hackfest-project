from flask import Flask, request, render_template, url_for
import bot 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/room')
def room():
    return render_template('room.html')

@app.route('/file')
def file():
    return render_template('fileReader.html')



if __name__ == '__main__':
    app.run(debug=True)