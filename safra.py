# UFCG - P1 - 2019.2
# Yalle Carvalho - 119210523
# Divisão Safra

soja = int(input())
clientes_atacado = int(input())
clientes_varejo = int(input())

soja_atacado = int(soja / clientes_atacado)
soja_varejo = (soja - (soja_atacado * clientes_atacado)) / clientes_varejo

print("Clientes no atacado = {}kg cada.".format(soja_atacado))
print("Clientes no varejo = {:.2f}kg cada.".format(soja_varejo))
