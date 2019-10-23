# UFCG - Programação 1
# Yalle Carvalho
# Converte matrícula

matricula = input()
nova = ''
contem_nove = False

for i in range(len(matricula)-7):
    nova += '1'
    nova += matricula[1] 
    nova += matricula[2]
    nova += matricula[3] 
    nova += matricula[4]
    nova += '0'
    nova += matricula[5]
    nova += matricula[6]
    nova += matricula[7]

    if nova > matricula:
        contem_nove = True

print(nova)

