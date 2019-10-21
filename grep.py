# UFCG - Programação 1
# Yalle Carvalho
# Grep

palavra = input()
num_frases = int(input())

pertencente = False

for i in range(num_frases):
    frases = input()
    palavras = frases.split()

    if not pertencente and palavras[i] == palavra:
        pertencente = True
        print(frases)
