import re
tokens = [
    (r'suma', 'SUMA'),
    (r'resta', 'RESTA'),
    (r'multiplica', 'MULTIPLICACION'),
    (r'divide', 'DIVISION'),
    (r'<=', 'DELIMITADOR'),
    (r'=>', 'DELIMITADOR'),
    (r'\(', 'PARENTESIS'),
    (r'\)', 'PARENTESIS'),
    (r'[ \n\t]+', None),
]
string = open('l.sr').read()

def validate(caracteres):
    pos = 0
    while pos < len(caracteres):
        m = None
        for token in tokens:
            token, tipo = token
            r = re.compile(token)
            m = r.match(caracteres, pos)
            if m:
                text = m.group(0)
                print(text)
                break
        if m:
            pos = m.end(0)
        else:
            print("Ilegal caracter", caracteres[pos])
        break
validate(string)