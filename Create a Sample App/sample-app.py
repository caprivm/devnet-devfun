from flask import Flask, render_template
from flask import request

sample = Flask(__name__)

@sample.route("/")
def main():
    # return "You are calling me from " + request.remote_addr
    return render_template("index.html")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)