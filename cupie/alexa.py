from flask import Flask
from flask_ask import Ask, statement

from cupie import light


app = Flask(__name__)
ask = Ask(app, '/')


@ask.intent('LightOnIntent')
def light_on():
    light.on()
    return statement("Light it up")

@ask.intent('LightOffIntent')
def light_off():
    light.off()
    return statement("Goodnight sweet prince")

if __name__ == '__main__':
    app.run()
