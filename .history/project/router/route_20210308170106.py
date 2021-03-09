from project import app
from project.controllers.aplicationController import appController
@app.route('/')
def add():
    return appController.index()