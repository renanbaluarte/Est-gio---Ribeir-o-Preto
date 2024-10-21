# Verificar a existência da letra 'a'

def contar_a(string):
    count = string.lower().count('a')
    return count

string = input("Informe uma string: ")
ocorrencias = contar_a(string)

if ocorrencias > 0:
    print(f"A letra 'a' aparece {ocorrencias} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")
