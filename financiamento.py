valor = float(input("insira o valor: "))
qparcelas = float(input("insira quantas parcelas: "))
juros = float(input("insira o juros: "))

parcela = (valor/qparcelas) + ((valor/qparcelas)*(juros))

print(f"cada parcela sera de {parcela}")
