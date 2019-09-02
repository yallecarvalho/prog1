# UFCG - P1 - 2019.2
# Yalle Carvalho - 119210523
# Calcula ingressos do cinema

adultos = int(input())
criancas = int(input())
ingresso = float(input())

valor_total = (adultos * ingresso) + criancas * (ingresso/2)

print("Total: R$ {:.2f}".format(valor_total))
