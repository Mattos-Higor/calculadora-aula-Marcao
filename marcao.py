print("CALCULADORA")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação:")
print("1 - Soma")
print("2 - Subtração")  # <-- Reativada!
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite a opção: ")

if opcao == "1":
    resultado = num1 + num2
    print("Resultado:", resultado)

elif opcao == "2":  # <-- Reativada!
    resultado = num1 - num2
    print("Resultado:", resultado)

elif opcao == "3":
    resultado = num1 * num2
    print("Multiplicação resultou em:", resultado)
    
elif opcao == "4":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Não é possível dividir por zero")
elif opcao == "5":  # <-- Nova lógica adicionada!
    resultado = num1 ** num2
    print("O resultado da potenciação é:", resultado)

else:
    print("Opção inválida")