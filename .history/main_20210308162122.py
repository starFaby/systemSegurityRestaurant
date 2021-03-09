


@app.route('/')
def index():
    return 'faby star'

from project import demo
print(demo.add())
if __name__ == '__main__':
    app.run(debug=True)