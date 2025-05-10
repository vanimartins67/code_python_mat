# resultado = 1
# for n in range(1, 11):
#     print(n)
#     resultado =  resultado * n
# print("Fatorial de 10", resultado)


def fat(pos):
    resultado = 1 
    for n in range(1, pos + 1):
        # print(n)
        resultado = resultado * n
# print("Fatorial de", pos, resultado)
    return resultado
print(fat(5))


def comb(n,p):
    return fat(n) / (fat(p) * fat(n - p))
print(comb(6, 4))

def prob(n, p):
    return n / p

caso1 = comb(6, 4) * (4 * prob(3, 6)) * (2 * prob(3, 6))
print(caso1)

caso2 = comb(6, 6) * (5 * prob(3, 6)) * (1 * prob(3, 6))
print(caso2)   

caso3 = comb(6, 6) * (6 * prob(3, 6))
print(caso3)

print("Resultado: ", (caso1 + caso2 + caso3))








