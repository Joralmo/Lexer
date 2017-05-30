import lexer



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

lexer.validate(a)