from flask import Flask
from flask import render_template
from flask import request
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def mainf():
	textres = ""
	baseres = ""
	errorde = False
	erroren = False
	if request.method == "POST":
		texte = request.form["texte"]
		basee = request.form["basee"]
		# print(f"{texte}\n{basee}")
		if request.form["action"] == "en":
			try:
				baseres = base64.b64encode(bytearray(texte, "ascii")).decode("ascii")
				textres = texte
			except:
				erroren = True
		elif request.form["action"] == "de":
			try:
				textres = base64.b64decode(bytearray(basee, "ascii")).decode("ascii")
				baseres = basee
			except:
				errorde = True
		elif request.form["action"] == "cl":
			textres = ""
			baseres = ""
	return render_template("index.html", textres = textres, baseres = baseres, errorde=errorde, erroren=erroren)


app.run(host="0.0.0.0", port=8080)