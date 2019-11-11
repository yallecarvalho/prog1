# UFCG - Programação 1
# Yalle Carvalho
# Embarque organizado

par = 0
passageiros = input().split()
resultado = ''

for i in range(len(passageiros)):
    if int(passageiros[i]) % 2 == 0:
        par += 1
    if int(passageiros[i]) % 2 != 0 and par >= 1:
        resultado = 'erro'

if resultado != 'erro':
    resultado = 'ok'

print(resultado)
