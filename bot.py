from flask import Flask,request
import json
import requests

app = Flask(__name__)

VALIDATION_TOKEN = 'aijiajia'
PAT = 'EAAYW62J5ODcBADa6pvBqHgoZBoW4bTw8ltDjK3ZAmUAWQ7JKsfZCc11YGoSS1lYhf5wBOZBtJc9ykpdZAv4VJm9Yi2Ss2cm9QCd8w5gRSSqUoCfPYZAjvz0sFKCrPusb4PsUMAJObAn97NNG3q3L3LltfsRo9McBInOfjfHQerqQZDZD'

@app.route("/bot", methods=['GET'])
def handle_verification():
    print 'handling verification'
    if request.args.get('hub.mode') == 'subscribe' \
        and request.args.get('hub.verify_token') == VALIDATION_TOKEN:
        print 'verification passes'
        return request.args.get('hub.challenge')
    print 'verification failed'
    return 'Error, wrong verfication token'

@app.route("/bot", methods=['POST'])
def handle_messages():
    print "handling messages"
    payload = request.get_data()
    print payload
    for sender, message in parse_request(payload):
        print "incoming from %s: %s" % (sender, message)
        send_message(PAT, sender, message)
    return "OK"

def parse_request(payload):
    print "parsing request"
    data = json.loads(payload)
    messaging_events = data["entry"][0]["messaging"]
    for event in messaging_events:
        if "message" in event and "text" in event["message"]:
            yield event["sender"]["id"], event["message"]["text"].encode('unicode_escape')
        # else:
        #     yield event["sender"]["id"], "I can't echo this"

def send_message(token, recipient, text):
  """Send the message text to recipient with id recipient.
  """
  r = requests.post("https://graph.facebook.com/v2.6/me/messages",
    params={"access_token": token},
    data=json.dumps({
      "recipient": {"id": recipient},
      "message": {"text": text.decode('unicode_escape')}
    }),
    headers={'Content-type': 'application/json'})
  if r.status_code != requests.codes.ok:
    print r.text



if __name__ == "__main__":
    app.run()
