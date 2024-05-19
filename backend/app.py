from flask import Flask, request, render_template, url_for,session, abort, redirect
import bot 
import env
import pymongo

app = Flask(__name__)
app.secret_key = env.SECRET_KEY

client = pymongo.MongoClient(env.mongo_api)
db = client['studysquad']

users = db['users']


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html', error="")

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    return abort(401)

@app.route('/room',)
def room():
    if 'username' in session:
        return render_template('room.html')
    return abort(401)

@app.route('/file')
def file():
    if 'username' in session:
        return render_template('fileReader.html')
    return abort(401)

@app.route('/video')
def video():
    if 'username' in session:
        return render_template('video.html')
    return abort(401)

@app.route('/ytnotes')
def ytnotes():
    if 'username' in session:
        return render_template('ytnotes.html',data="")
    return abort(401)

@app.route('/valid', methods=['POST'])
def valid():
    email=request.form['email']
    password=request.form['password']
    user = users.find_one({'email':email,'password':password})
    if user is None:
        return render_template('login.html',error="Invalid Credentials")
    session['username'] = email
    return redirect(url_for('dashboard'))

@app.route('/generate' , methods=['POST'])
def gen():
    video_id = request.form['link']
    response = bot.get_notes(env.gemini_api,video_id)
    print(response)
    return render_template('ytnotes.html',data=response)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)