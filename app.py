from flask import Flask, request
from fnRoute import regFunc
from settings import verify_token
from utils import sendMessage
import traceback
import json

app = Flask(__name__)


@app.route('/webhook', methods=['GET'])# initial verification
def initVerif():
    if request.args.get('hub.verify_token') == verify_token:
      return request.args.get('hub.challenge')
    return "Wrong Verify Token"


@app.route('/webhook', methods=['POST'])
def webhook():
    text = request.form['text']
    sender = "me"
    return regFunc.serve(text, sender)
    # try:
    #     data = json.loads(request.data)
    #     text = data['entry'][0]['messaging'][0]['message']['text'].lower()  # Incoming Message Text
    #     sender = data['entry'][0]['messaging'][0]['sender']['id']  # Sender ID
    #     reply_msg = regFunc.serve(text, sender)
    #     sendMessage(sender, reply_msg)
    # except Exception as e:
    #     print(traceback.format_exc()) # something went wrong


@app.route('/')
def home():
    return "<h1>I'm 'Yum Ngein'</h1>"

if __name__ == '__main__':
  app.run(debug=True, port=8080)
