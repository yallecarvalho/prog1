# UFCG - Programação 1
# Yalle Carvalho
# Mais velhos primeiro

def idosos_inicio(fila):
    j = 0
    for i in range(len(fila)):
        if int(fila[i]) >= 60:
          mais_velho = fila[i]  
          fila[j], fila[i] = fila[i], fila[j]
          j += 1
