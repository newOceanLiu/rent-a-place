from flask import Flask
from flask import request

app = Flask(__name__)

VALIDATION_TOKEN = 'aijiajia'

@app.route("/bot", methods=['GET','POST'])
def chat():
    is_verification, verification_response = handle_verification()
    if is_verification:
        return verification_response
    else:
        return "Hello human! \n"

def handle_verification():
    if request.method == 'GET' \
        and request.args.get('hub.mode') == 'subscribe' \
        and request.args.get('hub.verify_token') == VALIDATION_TOKEN:
        return True, request.args.get('hub.challenge')
    return False, None
if __name__ == "__main__":
    app.run()
