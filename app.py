from flask import Flask, request, jsonify
from truecallerpy import search_phonenumber
import os


def get_truecaller_info(phone_number):
    api_key = os.environ.get('TRUECALLER_API_KEY')
    country_code = "IN"
    data = search_phonenumber(phone_number, country_code, api_key)
    
    return data


app = Flask(__name__)



@app.route('/api/process/', methods=['GET'])
def process():
    phone_number = request.args.get('phonenumber')
    

    if phone_number:
        result = get_truecaller_info(phone_number)
        return jsonify(result)
    else:
        return jsonify({'error': 'Invalid phone number'}), 400
    
@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"
if __name__ == '__main__':
    app.run()
