# UFCG - Programação 1
# Yalle Carvalho
# Letras dobradas

num = int(input())
sem, com = [], []

for i in range(num):
    palavra = input()
    duplicou = False
    for j in range(len(palavra)-1):
        if palavra[j] == palavra[j-1]:
            duplicou = True
            com.append(palavra)
    if duplicou == False:
        sem.append(palavra)

print('{} palavra(s) com letras dobradas:'.format(len(com)))
for p in com:
    print(p)
print('---')
print('{} palavra(s) sem letras dobradas:'.format(len(sem)))
for p in sem:
    print(p)
