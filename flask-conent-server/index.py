from flask import Flask, request, jsonify,render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

while True:
    app.run(host='0.0.0.0', port=80, debug=True)