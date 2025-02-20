#Escreva um programa para pedir um número e em seguida o nome. Exiba o nome (uma letra de cada vez em cada linha) e repita isso para o número de vezes que ele digitou.
print("Matheus Golanowski")
numero = int(input("Digite um numero: "))
nome = input("Qual seu nome: ")
for i in range(numero):
    for letras in nome:
        print(letras)
