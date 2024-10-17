import random

# Função que gera a introdução da frase
def gerar_introducao():
    introducoes = ["Eu sou Vitor,", "Eu sou Emilly,", "Eu sou Leandro," ,"Eu sou Alice,"]
    return random.choice(introducoes)

# Função que gera o desnvolvimentos da frase
def gerar_desenvolvimento():
    desenvolvimentos = ["tenho 20 anos", "tenho 18 anos", "tenho 28 anos", "tenho 22 anos"]
    return random.choice(desenvolvimentos)

# Função que gera o final da frase
def gerar_final():
    finais = ["e gosto de animais.", "e gosto de carros.", "e gosto de motos.", "e gosto de viajar."]
    return random.choice(finais)

# Função principal que gera a frase completa
def gerar_frase():
    introducao = gerar_introducao()
    desenvolvimento = gerar_desenvolvimento()
    final = gerar_final()

    frase = f"{introducao} {desenvolvimento} {final}"
    return frase

# Exibe a frase gerada
if __name__ == "__main__":
    print(gerar_frase())

