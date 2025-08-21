numeros_str = input("Digite os números separados por espaço: ")

# Converte a lista de strings para lista de inteiros
numeros = list(map(int, numeros_str.split()))

# Contadores para positivos, negativos e zeros
positivos = 0
negativos = 0
zeros = 0

# Análise de cada número
for num in numeros:
    if num > 0:
        print(f"{num} é positivo.")
        positivos += 1
    elif num < 0:
        print(f"{num} é negativo.")
        negativos += 1
    else:
        print(f"{num} é zero.")
        zeros += 1

# Relatório final
print("Relatório:")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Zeros: {zeros}")