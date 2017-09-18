from flask import Flask, request
from fnRoute import regFunc
from settings import verify_token
from settings import token
import traceback
import requests
import json
import sys

app = Flask(__name__)


@app.route('/webhookx', methods=['GET'])  # initial verification
def initVerif():
    if request.args.get('hub.verify_token') == verify_token:
        return request.args.get('hub.challenge')
    return "Wrong Verify Token"


@app.route('/webhookx', methods=['POST'])
def webhook():
    data = json.loads(request.data)
    print(data)
    text = data['entry'][0]['messaging'][0]['message']['text'].lower()  # Incoming Message Text
    sender = data['entry'][0]['messaging'][0]['sender']['id']  # Sender ID
    print("RECIEVE: {} FROM {}".format(text, sender))
    sys.stdout.flush()
    reply_msg = regFunc.serve(text, sender)
    try:
        payload = {'recipient': {'id': sender}, 'message': {'text': reply_msg}}
        r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
    except Exception as e:
        print(traceback.format_exc())  # something went wrong
    return "Foo!"  # Not Really Necessary


@app.route('/')
def home():
    return "<h1>I'm 'Yum Ngein'</h1>"

if __name__ == '__main__':
    app.run(debug=False, port=8080)
