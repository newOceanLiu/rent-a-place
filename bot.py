from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def chat():
    return "Hello human! \n"

if __name__ == "__main__":
    app.run()
