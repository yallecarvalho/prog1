# UFCG - P1 - 2019.2
# Yalle Carvalho - 119210523
# Graus Decimais

graus = int(input())
minutos = int(input())
segundos = int(input())

graus_decimais = graus + ((minutos / 60) + (segundos / 3600))

print("graus = {:.4f}".format(graus_decimais))
