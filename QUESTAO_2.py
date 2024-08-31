def menor_num(valor1, valor2):
    global menor
    menor = valor1
    if valor2 < menor:
        menor = valor2
    return menor
def mdc(valor1, valor2):
    menor = menor_num(valor1,valor2)
    mdc = 1
    for c in range(1, menor + 1):
        if valor1 % c == 0 and valor2 % c == 0:
            mdc = c
    return mdc

def mmc(valor1, valor2):
    mmc = 1
    c = 2
    while valor1 > 1 or valor2 > 1:
        if valor1 % c == 0 or valor2 % c == 0:
            if valor1 % c == 0:
                valor1 = valor1 // c
            if valor2 % c == 0:
                valor2 = valor2 // c
            mmc *= c
        else:
            c += 1
    return mmc


valor1  = int(input("digite 1 valor: "))
valor2 = int(input("digite o 2 valor: "))
print(f"MDC: {mdc(valor1, valor2)}")
print(f"MMC: {mmc(valor1, valor2)}")