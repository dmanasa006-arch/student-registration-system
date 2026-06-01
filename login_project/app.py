from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Predefined credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "12345"

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return redirect(url_for('home'))
    else:
        return render_template(
            'login.html',
            error="Invalid User ID or Password"
        )

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)