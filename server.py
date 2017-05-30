import lexer

from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask import request
from flask import json

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/", methods=['POST'])
def hello():

	a = """
		$a2 Sr.igual 3
		$b2 Sr.igual 4
		Sr.si ($b2 Sr.esigual $a2) => m
		    Sr.escriba("El mayor es" Sr.suma $b2)
		Sr.no =>
		        Sr.escriba("El mayor es" Sr.suma $a2)
		    <=
		<=
		"""
	invalidos = []
	
	string = request.form.get('string')

	json = lexer.validate(string)
	return jsonify(json)

if __name__ == "__main__":
    app.run(host="0.0.0.0")