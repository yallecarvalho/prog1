# UFCG - Programação 1
# Yalle Carvalho
# Imprime Ranking (Cumulativo)

num = int(input())
times = []
pontuacao = []


for i in range(num):
    times.append(input())
    pontuacao.append(input())

for i in range(num):
    if i == 0:
        print("{}. {} ({})".format(i+1, times[0], pontuacao[0]))
    elif pontuacao[i] == pontuacao[i-1]:
        print("{}. {} ({})".format(i, times[i], pontuacao[i]))
    else: 
        print('{}. {} ({})'.format(i+1, times[i], pontuacao[i]))
