# UFCG - P1 - 2019.2
# Yalle Carvalho - 119210523
# Tweets por Página

qtt = int(input())
pg = qtt // 400

tp = qtt % 400
r = tp * 100 / qtt

print('Serão necessárias {} página(s) para visualizar os tweets.'.format(pg))
print('{:.1f}% dos tweets serão perdidos.'.format(r))
