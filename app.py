from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from url_processor import processURL
from url_processor import prepareURLfromVidID

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def main():
	return render_template('index.html')

@app.route('/submitLink', methods=['POST'])
def submitLink():
	vidURL = request.form.get('vidURL')
	videoID = processURL(vidURL);
	return redirect(url_for('showLink', vidID=videoID))

@app.route('/showLink', methods=['GET'])
def showLink():
	vidID=request.args.get('vidID')
	shareableLink = prepareURLfromVidID(vidID);
	return render_template('showLink.html', shareableURL = shareableLink)

if __name__=="__main__":
	app.run()


