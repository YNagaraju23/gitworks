from flask import Flask, app, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("name.html")
@app.route("/success")
def success():
    return "Login page is successfully loaded"
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST" and request.form["username"]=="admin":
        return redirect(url_for('home'))
if __name__ == "__main__":
    app.run(debug=True)