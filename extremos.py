# UFCG - P1 - 2019.2
# Yalle Carvalho - 119210523
# Média dos Extremos

n = int(input())
lista = []
maior = 0
menor = 0

for i in range(n):
    a = int(input())
    lista.append(a)
    if i == 0:
        maior = a
        menor = a
    else:
        if a > maior:
            maior = a
        elif a < menor:
            menor = a
    
m_extremos = (maior + menor) / 2
acima_m = 0
abaixo_m = 0

for i in range(len(lista)):
    if lista[i] > m_extremos:
        acima_m += 1
    elif lista[i] < m_extremos:
        abaixo_m += 1

print('Menor número: {}'.format(menor))
print('Maior número: {}'.format(maior))
print('Média dos extremos: {:.2f}'.format(m_extremos))
print('{} número(s) abaixo da média'.format(abaixo_m))
print('{} número(s) acima da média'.format(acima_m))
