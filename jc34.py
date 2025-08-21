idade = int(input("Digite sua idade: "))
estudante = input("É estudante? (s/n): ").strip().lower()

# Verifica o preço do ingresso baseado nas regras
if idade <= 12:
    preco = 8.00
elif estudante == 's':
    preco = 12.00
elif idade >= 65:
    preco = 10.00
else:
    preco = 20.00
    
    # Exibe o preço formatado
print(f"Preço do ingresso: R$ {preco:.2f}")