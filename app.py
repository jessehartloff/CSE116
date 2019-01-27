from flask import Flask

app = Flask(__name__)


@app.route('/cse116')
def cse116():
    return 'Hello CSE116!'


@app.route('/cse442')
def cse442():
    return 'Hello CSE442!'


if __name__ == '__main__':
    app.run()
