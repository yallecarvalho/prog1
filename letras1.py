# UFCG - Programação 1
# Yalle Carvalho
# Letras dobradas

num = int(input())
sem, com = [], []

for i in range(num):
    palavra = input()
    dob = 0
    for j in range(1, len(palavra)):
        if palavra[j-1] == palavra[j]:
            dob += 1
    if dob >= 1:
        com.append(palavra)
    if dob == 0:
        sem.append(palavra)

print('{} palavra(s) com letras dobradas:'.format(len(com)))
for p in com:
    print(p)
print('---')
print('{} palavra(s) sem letras dobradas:'.format(len(sem)))
for p in sem:
    print(p)
