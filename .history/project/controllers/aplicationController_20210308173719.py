from flask import render_template
class AplicationController():
    def __init__(self):
        pass

    def index(self):
        return render_template('frontend/pages/home/home.html')
    
    def about(self):
        return render_template('frontend/pages/about/about.html')

appController = AplicationController()