# UFCG - P1 - 2019.2
# Yalle Carvalho - 119210523
# CNPJ

cnpj = input()

v1 = float(cnpj[0])
v2 = float(cnpj[1])
v3 = float(cnpj[3])
v4 = float(cnpj[4])
v5 = float(cnpj[5])
v6 = float(cnpj[7])
v7 = float(cnpj[8])
v8 = float(cnpj[9])

v9 = '0001'
v10 = float(v9[0])
v11 = float(v9[1])
v12 = float(v9[2])
v14 = float(v9[3])

dv = int(v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8  + v10 + v11 + v12 + v14)

print('{0}/{1}-{2:02}'.format(cnpj, v9, dv))
