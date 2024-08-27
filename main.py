from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from wtforms import Form, BooleanField, StringField, validators
from flask_wtf import FlaskForm
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
