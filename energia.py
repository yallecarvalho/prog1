# UFCG - P1 - 2019.2
# Yalle Carvalho - 119210523
# Consumo Energia

potencia = int(input())
tempo = int(input()) * 60

consumo = ((potencia * tempo) / 3600000)

print("{:.1f} kWh".format(consumo))
