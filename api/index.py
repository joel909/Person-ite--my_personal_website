from flask import Flask, request, jsonify,render_template,url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')
@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='favicon.ico')
@app.route('/404', methods=['GET'])
def not_found():
    return render_template('404.html')

@app.route('/journey', methods=['GET'])
def journey():
    return render_template('journey.html')

@app.route('/insta', methods=['GET'])
def insta():
    return render_template('insta.html')

while True:
    app.run(debug=True,host="0.0.0.0",port=5000)

##feature 1 - all pages footer
##feature 2 - link to my github page and other pages 
##feture 3 - custom font from google fonts

##feature 4 - 404 not found page
## hackatime image which shows live time from hackatime 
## differt color and differnt fonts size and color 

##html button to redirect to my instagram page
## special support for differnt screen sizes
##hovering buttons on home page