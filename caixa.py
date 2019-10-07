n = int(input())
num_dados = 0

a = False

for i in range(n):
    dados = input()
    d = dados.split()
    num_dados += 1
    if not a and int(d[0]) < 0:
        a = True
        print('dado inconsistente. peso negativo.')
    elif not a and int(d[1]) < 0:
        a = True
        print('dado inconsistente. combustível negativo.')
    elif not a and int(d[2]) < 0:
        a = True
        print('dado inconsistente. altitude negativa.')

print('{} dados válidos.'.format(num_dados))

