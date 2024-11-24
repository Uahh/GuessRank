
from flask import Flask, request, redirect, url_for, render_template, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Guess Rank Flask App!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass

@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('home')))
    resp.set_cookie('username', '', expires=0)
    return resp

if __name__ == '__main__':
    app.run(debug=True)