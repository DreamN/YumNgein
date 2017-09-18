from flask import Flask, request
import requests
import json
import traceback
from fnRoute import regFunc
from settings import verify_token, token

app = Flask(__name__)


@app.route('/webhook', methods=['GET'])# initial verification
def initVerif():
    if request.args.get('hub.verify_token') == verify_token:
      return request.args.get('hub.challenge')
    return "Wrong Verify Token"


@app.route('/webhook', methods=['POST'])
def webhook():
    text = request.form['text']
    sender = "sd7hkj"
    return regFunc.serve(text, sender)
    # try:
    #     data = json.loads(request.data)
    #     text = data['entry'][0]['messaging'][0]['message']['text'].lower() # Incoming Message Text
    #     sender = data['entry'][0]['messaging'][0]['sender']['id'] # Sender ID
    #
    #     print("Incoming Message: {}".format(text))
    #     text_send = "Hello"
    #     payload = {'recipient': {'id': sender}, 'message': {'text': text_send}}
    #     r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
    # except Exception as e:
    #     print(traceback.format_exc()) # something went wrong
    # return "Foo!"#Not Really Necessary


@app.route('/')
def home():
    return "<h1>I'm 'Yum Ngein'</h1>"

if __name__ == '__main__':
  app.run(debug=True, port=8080)
