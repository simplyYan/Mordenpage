from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/readfile', methods=['POST'])
def read_file():
    data = request.json
    file_path = data.get('file_path')

    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        return jsonify({"content": content}), 200
    else:
        return jsonify({"error": "File not found"}), 404

@app.route('/writefile', methods=['POST'])
def write_file():
    data = request.json
    file_path = data.get('file_path')
    content = data.get('content')

    with open(file_path, 'w') as f:
        f.write(content)

    return jsonify({"message": "File written successfully"}), 200

@app.route('/submitform', methods=['POST'])
def submit_form():
    form_data = request.form
    return jsonify({"message": "Form submitted", "data": form_data}), 200

@app.route('/startsession', methods=['POST'])
def start_session():
    session['active'] = True
    return jsonify({"message": "Session started"}), 200

@app.route('/setsession', methods=['POST'])
def set_session():
    data = request.json
    key = data.get('key')
    value = data.get('value')
    session[key] = value
    return jsonify({"message": f"Session key {key} set"}), 200

@app.route('/getsession', methods=['POST'])
def get_session():
    data = request.json
    key = data.get('key')
    value = session.get(key, None)
    if value:
        return jsonify({"value": value}), 200
    else:
        return jsonify({"error": "Session key not found"}), 404

@app.route('/endsession', methods=['POST'])
def end_session():
    session.clear()
    return jsonify({"message": "Session ended"}), 200

@app.route('/httprequest', methods=['POST'])
def http_request():
    data = request.json
    url = data.get('url')

    try:
        response = requests.get(url)
        return jsonify({"response": response.text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)