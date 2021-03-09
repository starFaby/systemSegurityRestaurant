from flask import render_template
class AplicationController():
    def __init__(self):
        pass

    def index(self):
        return render_template('index.html')

appController = AplicationController()