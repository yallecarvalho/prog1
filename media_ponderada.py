# UFCG - P1 - 2019.2
# Yalle Carvalho - 119210523
# Média

nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
peso1 = float(input())
peso2 = float(input())
peso3 = 100 - (peso1 + peso2)

m1 = nota1 * (peso1 / 100)
m2 = nota2 * (peso2 / 100)
m3 = nota3 * (peso3 / 100)


print('Média Final: {:.1f}'.format(m1 + m2 + m3))
