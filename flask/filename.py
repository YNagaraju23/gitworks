from flask import Flask, render_template
app=Flask(__name__)
@app.route('/user/<username>')
def show_user(username):
    return f'hello {username}'
@app.route('/')
def hello():
    return "hello world"
@app.route("/index")
def index():
    return "this is an index page"

if __name__=="__main__":
    app.run(debug=True)