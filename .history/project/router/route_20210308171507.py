from project import app
from project.controllers.aplicationController import appController

@app.route('/')
@app.route('/home')
def index():
    return appController.index()