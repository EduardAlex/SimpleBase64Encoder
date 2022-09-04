from flask import Flask
from flask import render_template
from flask import request
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def mainf():
	textres = ""
	baseres = ""
	if request.method == "POST":
		texte = request.form["texte"]
		basee = request.form["basee"]
		# print(f"{texte}\n{basee}")
		if request.form["action"] == "en":
			baseres = base64.b64encode(bytearray(texte, "ascii")).decode("ascii")
			textres = texte
		elif request.form["action"] == "de":
			textres = base64.b64decode(bytearray(basee, "ascii")).decode("ascii")
			baseres = basee
		elif request.form["action"] == "cl":
			textres = ""
			baseres = ""
	return render_template("index.html", textres = textres, baseres = baseres)


app.run(host="0.0.0.0", port=80, debug=True)