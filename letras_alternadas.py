# UFCG - Programação 1
# Yalle Carvalho
# Letras alternadas

# Entrada
palavra = input()
letras = '' 

# Calculo da impressão de letras
for i in range(0, len(palavra), 2):
    letras += palavra[i]
print(letras)
