import  re
tokens=[
    ("^Sr.escriba(\().*(\))$","FUNCION"),
    ("^\s*Sr.mas\s*$","SUMA"),
    ("^\s*Sr.menos\s*$","RESTA"),
    ("^\s*Sr.por\s*$","MULTIPICACION"),
    ("^\s*Sr.entre\s*$","DIVISION"),
    ("^[A-z]+[0-9 A-z]*$","VARIABLE"),
    ("^Sr.si$","CONDICION"),
    ("^Sr.sino$","CONDICION"),
    ("^=>$","DELIMITADOR"),
    ("^<=$","DELIMITADOR"),
    ("^\($","PARENTESIS"),
    ("^\)$","PARENTESIS"),
    ("^[0-9]+x[A-z 0-9]*$","INVALIDO")
]
f=open("a.txt","r")
data=f.read()
exp=""
"""def lexer(x):
    sw=0
    for token in tokens:
        if re.match(token[0],x):
            print(x+" -> "+token[1])
            sw=1
    if sw==0:
        print(x+" ->  INVALIDO ")
palabras=data.split()
for palabra in palabras:
    lexer(palabra)"""
def lexer(x):
    for token in tokens:
        if re.match(token[0],x):
            print(x+" -> "+token[1])
for linea in data:
    if not linea == " ":
        exp += linea
        lexer(exp)
    else:
        print(exp)
        exp=""