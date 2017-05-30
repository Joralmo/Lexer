import re
tokens = [
    (r'[$][^\d]([A-Za-z])*([0-9])*',"VARIABLE"),
	(r'Sr.escriba','FUNCION'),
	(r'Sr.igual', 'ASIGNACION'),
	(r'Sr.esigual', 'COMPARACION'),
	(r'Sr.suma', 'SUMA'),
	(r'Sr.resta', 'RESTA'),
	(r'Sr.para', 'CICLO'),
	(r'Sr.mientras', 'CICLO'),
	(r'Sr.si', 'CONDICION'),
	(r'Sr.no', 'CONDICION'),
	(r'Sr.multiplica', 'MULTIPLICACION'),
	(r'Sr.divide', 'DIVICION'),
	(r'<=', 'DELIMITADOR'),
	(r'=>', 'DELIMITADOR'),
	(r'\(', 'PARENTESIS'),
	(r'\)', 'PARENTESIS'),
	(r'\d{1,}', 'ENTERO'),
	(r'(\")(.*)(\")', 'CADENA'),
	(r'[ \n\t]+', None),
]
string = open('prueba.sr').read()
def validate(caracteres):
	pos = 0
	#caracteres=re.sub("\s*","",caracteres)
	while pos < len(caracteres):
		m = None
		for token in tokens:
			token, tipo = token
			r =re.compile(token)
			m = r.match(caracteres, pos)
			if m:
				text = m.group(0)
				if tipo!=None:
					print(str(text)+" >> "+str(tipo))
				break
		if m:
			pos =  m.end(0)
		else:
			print("Caracter ilegal", caracteres[pos])
			pos = pos + 1
validate(string)