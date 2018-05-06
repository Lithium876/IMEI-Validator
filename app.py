from flask import Flask, request, render_template
from IMEI import *

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
	return render_template("index.html")

@app.route("/",methods=['POST'])
def res():
    number=request.form['number']
    position=request.form['position']
    if len(position) == 0:
    	res = ValidateIMEI(number)
    else:
    	res = ValidateIMEI(number, int(position))
    
    return render_template('index.html', result=res)

if __name__ == "__main__":
    app.run(port=8081, debug=True)