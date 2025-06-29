from flask import Flask, request, jsonify,render_template,url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')
@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='favicon.ico')

while True:
    app.run(debug=True,host="0.0.0.0",port=5000)