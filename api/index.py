from flask import Flask, request, jsonify,render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

while True:
    app.run()