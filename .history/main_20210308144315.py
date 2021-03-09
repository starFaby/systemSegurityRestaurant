from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'faby star'

print(__name__)