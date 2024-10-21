#Próximos elementos das sequências

def completar_sequencias():
    sequencia_a = [1, 3, 5, 7]
    sequencia_a.append(sequencia_a[-1] + 2)

    sequencia_b = [2, 4, 8, 16, 32, 64]
    sequencia_b.append(sequencia_b[-1] * 2)

    sequencia_c = [0, 1, 4, 9, 16, 25, 36]
    sequencia_c.append((len(sequencia_c))**2)

    sequencia_d = [4, 16, 36, 64]
    sequencia_d.append((len(sequencia_d) * 2)**2)

    sequencia_e = [1, 1, 2, 3, 5, 8]
    sequencia_e.append(sequencia_e[-1] + sequencia_e[-2])

    sequencia_f = [2, 10, 12, 16, 17, 18, 19]
    sequencia_f.append(sequencia_f[-1] + 1)

    print("Sequência a:", sequencia_a)
    print("Sequência b:", sequencia_b)
    print("Sequência c:", sequencia_c)
    print("Sequência d:", sequencia_d)
    print("Sequência e:", sequencia_e)
    print("Sequência f:", sequencia_f)

completar_sequencias()
