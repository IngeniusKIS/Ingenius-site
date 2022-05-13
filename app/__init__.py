from flask import *
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bs = Bootstrap(app)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.debug = True

from app import routes