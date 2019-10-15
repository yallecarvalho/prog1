# UFCG - Programação 1
# Yalle Carvalho
# Imprime Ranking (Cumulativo)

num = int(input())
times = []
pontuacao = []


for i in range(num):
    times.append(input())
    pontuacao.append(input())

ranking = 1
for i in range(num):
    if i == 0:
        print("{}. {} ({})".format(ranking, times[0], pontuacao[0]))
    elif pontuacao[i] == pontuacao[i-1]:
        print("{}. {} ({})".format(ranking, times[i], pontuacao[i]))
    else: 
        ranking = i + 1
        print("{}. {} ({})".format(ranking, times[i], pontuacao[i]))
