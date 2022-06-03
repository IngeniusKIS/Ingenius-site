from flask import *
from app import app 

@app.route('/')
def home():
	return render_template('home.html')


@app.route('/register/')
def register():
	return render_template('register.html')


@app.route('/about/')
def about():
	return redirect('https://fast-falls-22011.herokuapp.com/#about')

@app.route('/events/')
def events():
	return render_template('events.html')