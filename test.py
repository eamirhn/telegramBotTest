from flask import Response
from flask import request
from flask import Flask
import json
import requests
import os
url = "https://api.telegram.org/bot5164303840:AAFinWpqK_Nk3_6ZJscImsaL31zoCE0dsyo/"

app = Flask(__name__)


def get_all_updates():
    response = requests.get(url+'getUpdates')
    return response.json()


def get_last_update(allUpdates):
    return allUpdates['result'][-1]


def get_chat_id(update):
    return update['message']['chat']['id']


def sendmessage(chat_id, text):
    sendData = {'chat_id': chat_id, 'text': text}
    response = requests.post(url + 'sendMessage', sendData)
    return response


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':

        # get last interact
        msg = request.get_json()

        # get chat id of last interact
        chat_id = get_chat_id(msg)

        # get user's input
        text = msg['message'].get('text', '')

        if text == '/start':
            sendmessage(chat_id, 'Name Film Ra Vared Konid')
        return Response('ok', status=200)
    else:
        return '<h1>Film Bot</h1>'


app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
