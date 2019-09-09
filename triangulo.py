# UFCG - P1 - 2019.2
# Yalle Carvalho - 119210523
# Perímetro de Triângulo

import math

xa = int(input())
ya = int(input())
xb = int(input())
yb = int(input())
xc = int(input())
yc = int(input())

dab = math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)
dac = math.sqrt((xa - xc) ** 2 + (ya - yc) ** 2)
dbc = math.sqrt((xb - xc) ** 2 + (yb - yc) ** 2)

p = dab + dac + dbc

print('O perímetro é de {:.2f}'.format(p))
