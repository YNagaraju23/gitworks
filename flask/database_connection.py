from flask import Flask,render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime
import os
app = Flask(__name__)
print(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
try:
    os.makedirs(app.instance_path)
except OSError:
    print("ERROR")
if __name__=="__main__":
    app.run(debug=True)