from flask import Flask
from flask import session
app = Flask(__name__)
app.secret_key = "recipes_evan"

DATABASE = "recipes"