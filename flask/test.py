<<<<<<< HEAD
import flask
app = flask.Flask(__name__)
@app.route("/")
def hello():
    return "Hello, World!"
if __name__ == "__main__":
=======
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        return f"Hello {name}, POST request received"
    return render_template('name.html')

if __name__ == '__main__':
>>>>>>> 96bab3c6334f4daa21158864506ea63d294fcd03
    app.run(debug=True)
