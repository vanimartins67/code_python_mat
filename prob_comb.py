def fat(pos):
    resultado = 1 
    for n in range(1, pos + 1):
        resultado = resultado * n
    return resultado
def comb(n,p):
    return fat(n) / (fat(p) * fat(n - p))
print(comb(6, 4))

def prob(n, p):
    return n / p
# Passo 1: Total de comitês possíveis (sem restrição)
total = comb(5, 2) * comb(6, 2) * comb(3, 2)

# Passo 2: Comitês que incluem João e Maria
joao_e_maria = comb(5, 2) * comb(3, 2)

# Passo 3: Comitês válidos
validos = total - joao_e_maria

# Passo 4: Probabilidade
probabilidade = validos / total

print(f"Total de comitês possíveis: {total}")
print(f"Comitês com João e Maria: {joao_e_maria}")
print(f"Comitês válidos: {validos}")
print(f"Probabilidade: {probabilidade:.4f} ou {probabilidade*100:.2f}%")
