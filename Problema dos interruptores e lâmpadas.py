#Problema dos interruptores e lâmpadas

def descobrir_interruptores():
    lampadas = {"lampada_1": "fria e apagada", "lampada_2": "fria e apagada", "lampada_3": "fria e apagada"}
    lampadas["lampada_1"] = "quente e apagada"
    lampadas["lampada_2"] = "acesa e quente"
    lampadas["lampada_3"] = "fria e apagada"

    for lampada, estado in lampadas.items():
        print(f"{lampada} está {estado}.")

    print("\nConclusão:")
    print("Interruptor 1 controla a lampada_1 (quente e apagada).")
    print("Interruptor 2 controla a lampada_2 (acesa e quente).")
    print("Interruptor 3 controla a lampada_3 (fria e apagada).")

descobrir_interruptores()

