# UFCG - Programação 1
# Yalle Carvalho
# Encontra elemento

# função para encontrar
def meu_in(sequencia, num):
    for e in sequencia:
        if e == num:
            return True
    
    return False

num = input()
sequencia = input().split()

if meu_in(sequencia, num):
    print('sim')
else:
    print('não')
