from flask import Flask
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/alexa')


@ask.intent('LightOnIntent')
def light_on():
    return statement("Light it up")


if __name__ == '__main__':
    app.run()
