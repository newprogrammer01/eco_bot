from flask import Flask, request, jsonify
import os
import telegram


app = Flask(__name__)
TOKEN=os.environ.get('TOKEN')
bot=telegram.Bot(token='6047203124:AAEHAsliWgI329nLtH5vv8ymWKHmRQ-6V8s')

@app.route('/')
def home():
    html = '''
    <h1> This is a home page </h1>
    <p> This is a paragraph </p>
    '''
    return html


@app.route('/api', methods=['POST'])
def api():

    data = request.get_json(force=True)
    output = {'message': 'Hello World'}
    return output



if __name__ == '__main__':
    app.run(debug=True)