from flask import Flask, request
from application import main

app = Flask(__name__)

@app.route('/', methods=['GET'])
def call():
    return main(request)
