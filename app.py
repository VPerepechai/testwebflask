from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Dobryi den Everybody!"


@app.route('/about/')
def about():
    return "Boris Johnson is My Hero!"

if __name__ == "__main__":
    app.run(debug=True)