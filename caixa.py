n = int(input())
num_dados = 0

for i in range(n):
    dados = input()
    d = dados.split()
    num_dados += 1
    if int(d[0]) < 0:
        print('dado inconsistente. peso negativo.')
    elif int(d[1]) < 0:
        print('dado inconsistente. combustível negativo.')
    elif int(d[2]) < 0:
        print('dado inconsistente. altitude negativa.')
    else:
        print('{} dados válidos.'.format(num_dados))
