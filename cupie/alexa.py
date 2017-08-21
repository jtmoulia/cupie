import random

from flask import Flask
from flask_ask import Ask, statement

from cupie import light


app = Flask(__name__)
ask = Ask(app, '/')


@ask.intent('LightOnIntent')
def light_on():
    light.on()
    return statement(random.choice([
        "Light it up",
        "Here comes the sun",
        "Don't let moths in",
        "O right in the camera",
    ]))

@ask.intent('LightOffIntent')
def light_off():
    light.off()
    return statement(random.choice([
        "Goodnight sweet prince",
        "Lights out",
        "Sunset",
        "I'll see you in your dreams, bitch",
    ]))

if __name__ == '__main__':
    app.run()
