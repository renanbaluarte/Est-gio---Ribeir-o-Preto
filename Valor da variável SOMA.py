#Valor da variável SOMA

def calcular_soma():
    INDICE = 12
    SOMA = 0
    K = 1
    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K
    return SOMA

soma_final = calcular_soma()
print(f"O valor da variável SOMA ao final do processamento será: {soma_final}")
