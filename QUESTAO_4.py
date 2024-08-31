def verd(A, B, C):
    return (A != B) and not C

def false(A, B, C):
    return not ((A != B) and not C)

# lembrar que C eh false
condicoes = [(True, True, False), (True, False, False), (False, True, False), (False, False, False)]

for A, B, C in condicoes:
    print(f"|{A:^5}| {B:^5}| {C:^5} = {verd(A, B, C):^5} | { false(A, B, C):^5}|")