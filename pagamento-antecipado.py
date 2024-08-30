value = float(input("Digite o valor do produto: "))
descount = int(input("Digite o valor do desconto do produto: "))
descount = descount / 100

final_value = value * descount
print(final_value)