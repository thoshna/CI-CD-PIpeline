# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    return f"Hello, {name}! Your email is {email}."

if __name__ == '__main__':
    app.run(debug=True)
