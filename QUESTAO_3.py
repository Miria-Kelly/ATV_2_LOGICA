def conjuncao(x, c):
    return x and c

def disjuncao(x, c):
    return x or c

def condicional(x, c):
    return not x or c

def bicondicional(x, c):
    return x == c

def ou_exclusivo(x, c):
    return x != c

tabela_base= [(True, True), (True, False), (False, True), (False, False)]

#titulos
print("A".center(11), "B".center(10), "A ^ B".center(10), "A v B".center(10),
      "A -> B".center(10),"A <-> B".center(10), "A XOR B".center(10))

#andar pela tabela base e mostrar as operaçoes logicas
for x, c in tabela_base:
    print(f"|{x:^10}|{c:^10}|{conjuncao(x, c):^10}"
          f"|{disjuncao(x, c):^10}|{condicional(x, c):^10}"
          f"|{bicondicional(x, c):^10}|{ou_exclusivo(x, c):^10}|")
