from flask import *
from app import app 

@app.route('/')
def home():
	return render_template('home.html')


@app.route('/register/')
def register():
	return render_template('register.html')