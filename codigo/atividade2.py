# Exercicio 1

# for n in range(1, 11):
#     print(n)

# Exercicio 2

# for n in range(5):
#     print("Estudando Python!")

# Exercicio 4

# for n in range(3):
#     nome = input("Informe o nome: ")
#     print(f'O nome é {nome}')

# Exercicio 5

soma = 0

for n in range(5):
    number = float(input("informe um número: "))
    print(f'O número é: {number}')
    soma += number
    media = soma / 5

print(f'A soma é: {soma:.2f}')
print(f'O media é: {media:.2f}')
