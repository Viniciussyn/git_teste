print("Digite tres valores: ")

contador = 0

for i in range (0 , 3):

    print("Digite um valor: ")
    numero = int(input())

    if numero > contador:

        contador = numero

print("O maior número digita é: " , contador)

