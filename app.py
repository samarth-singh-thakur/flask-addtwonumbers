from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    try:
        data = request.get_json()
        if 'value1' in data and 'value2' in data:
            value1 = data['value1']
            value2 = data['value2']
            result = value1 + value2
            return jsonify({'result': result})
        else:
            return jsonify({'error': 'Please provide both value1 and value2 in the request.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
