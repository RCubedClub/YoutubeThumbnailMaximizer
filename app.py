from flask import Flask
from flask import render_template
from flask import request

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

@app.route('/showLink', methods=['POST'])
def showLink():
	vidID=request.form.get('vidID')

	return render_template('showLink.html', )

if __name__=="__main__":
	app.run()


