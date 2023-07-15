from flask import Flask, request, jsonify
from get import get_truecaller_info

app = Flask(__name__)



@app.route('/api/process/', methods=['GET'])
def process():
    phone_number = request.args.get('phonenumber')
    

    if phone_number:
        result = get_truecaller_info(phone_number)
        return jsonify(result)
    else:
        return jsonify({'error': 'Invalid phone number'}), 400

if __name__ == '__main__':
    app.run()
