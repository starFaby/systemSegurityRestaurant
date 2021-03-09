from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'faby star'

from project import *
print(demo.add())
if __name__ == '__main__':
    app.run()