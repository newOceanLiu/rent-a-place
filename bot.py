from flask import Flask
from flask import request

app = Flask(__name__)

VALIDATION_TOKEN = 'aijiajia'

@app.route("/bot", methods=['GET','POST'])
def chat():
    if request.method == 'GET' and request.args.get('verify_token'):
        return request.args.get('challenge')
    else:
        return "Hello human! \n"
        
if __name__ == "__main__":
    app.run()
