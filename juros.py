emprestimo = float(input("insira o emprestimo: "))
juros = float(input("insira o juros: "))
tempo = float(input("insira quantas vezes o juros foi aplicado: "))

valor = emprestimo + ((juros*emprestimo)*tempo)

print(valor)