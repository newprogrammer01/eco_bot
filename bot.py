from flask import Flask, request
import requests
import os 
app=Flask(__name__)
TOKEN=os.environ['TOKEN']
@app.route('webhook', methods=['POST'])
def webhook():
    data=request.get_json(force=True)
    print(data)
    return 'ok'
    
