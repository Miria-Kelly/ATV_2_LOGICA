def logica(expressao):
    expressao = expressao.replace("^","and").replace("v", "or").replace("`", 'not')
    resultado = eval(expressao)
    return resultado

A = True
B = False
C = True

prop1 = "A ^(B v C)" # B ou C = V // V e V = V
prop2 = "(A ^ B) v C" # A e B = F // F ou V = V
prop3 = "`(A ^ B) v C " # nao (A e B) = F / V // V ou V = V
prop4 = "` A v(` B ^ C)" # nao A = F // nao  B = V  // (`B e C) = V//  F  ou  V = V
print(logica(prop1))
print(logica(prop2))
print(logica(prop3))
print(logica(prop4))
