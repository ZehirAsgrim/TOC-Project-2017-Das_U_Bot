import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '488537287:AAHUaeLpt6fu3JGXcE1QzRvIRpjj85abBYM'
WEBHOOK_URL = 'https://706a245a.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'homeport',
        'temp',
        'info',
        'convoy',
        'cargo',
        'otaku',
        'victory',
        'destroyer',
        'underwater',
        'sunk',
        'kameraden',
        'greet',
        'banana',
        'aircraft',
        'allbanana',
        'outofdiesel',
        'outofo2',
        'lorient'
        ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'homeport',
            'dest': 'convoy',
            'conditions': 'is_going_to_convoy'
        },
        {
            'trigger': 'advance',
            'source': 'homeport',
            'dest': 'cargo',
            'conditions': 'is_going_to_cargo'
        },
        {
            'trigger': 'advance',
            'source': 'homeport',
            'dest': 'temp',
            'conditions': 'is_going_to_temp'
        },
        {
            'trigger': 'advance',
            'source': 'homeport',
            'dest': 'info',
            'conditions': 'is_going_to_info'
        },
        {
            'trigger': 'go_back',
            'source': 'temp',
            'dest': 'homeport'
        },
        {
            'trigger': 'go_back',
            'source': 'info',
            'dest': 'homeport'
        },
        {
            'trigger': 'advance',
            'source': 'homeport',
            'dest': 'otaku',
            'conditions': 'is_going_to_otaku'
        },
        {
            'trigger': 'go_back',
            'source': 'otaku',
            'dest': 'homeport'
        },
        {
            'trigger': 'advance',
            'source': 'convoy',
            'dest': 'victory',
            'conditions': 'is_going_to_victory'
        },
        {
            'trigger': 'advance',
            'source': 'convoy',
            'dest': 'destroyer',
            'conditions': 'is_going_to_destroyer'
        },
        {
            'trigger': 'advance',
            'source': 'destroyer',
            'dest': 'underwater',
            'conditions': 'is_going_to_underwater'
        },
        {
            'trigger': 'advance',
            'source': 'destroyer',
            'dest': 'kameraden',
            'conditions': 'is_going_to_kameraden'
        },
        {
            'trigger': 'advance',
            'source': 'kameraden',
            'dest': 'greet',
            'conditions': 'is_going_to_greet'
        },
        {
            'trigger': 'go_back',
            'source': 'greet',
            'dest': 'kameraden'
        },
        {
            'trigger': 'advance',
            'source': [
                'underwater',
                'aircraft'
            ],
            'dest': 'sunk',
            'conditions': 'is_going_to_sunk'
        },
        {
            'trigger': 'advance',
            'source': [
                'victory',
                'underwater'
            ],
            'dest': 'outofo2',
            'conditions': 'is_going_to_outofo2'
        },
        {
            'trigger': 'go_back',
            'source': 'sunk',
            'dest': 'homeport'
        },
        {
            'trigger': 'advance',
            'source': [
                'outofo2',
                'aircraft'
            ],
            'dest': 'kameraden',
            'conditions': 'is_going_to_kameraden'
        },
        {
            'trigger': 'advance',
            'source': 'kameraden',
            'dest': 'outofdiesel',
            'conditions': 'is_going_to_outofdiesel'
        },
        {
            'trigger': 'advance',
            'source': 'cargo',
            'dest': 'banana',
            'conditions': 'is_going_to_banana'
        },
        {
            'trigger': 'advance',
            'source': 'banana',
            'dest': 'allbanana',
            'conditions': 'is_going_to_allbanana'
        },
        {
            'trigger': 'advance',
            'source': 'allbanana',
            'dest': 'aircraft',
            'conditions': 'is_going_to_aircraft'
        },
        {
            'trigger': 'advance',
            'source': 'outofdiesel',
            'dest': 'lorient',
            'conditions': 'is_going_to_lorient'
        },
        {
            'trigger': 'go_back',
            'source': 'lorient',
            'dest': 'homeport'
        }
    ],
    initial='homeport',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
