#Faça um programa que solicite ao usuário para digitar o seu nome e um número qualquer, em seguida, exiba seu nome de várias vezes de acordo com o número que ele digitou!
print("Matheus Golanowski")
nome = input("Qual seu nome: ")
numero = int(input("Digite um numero"))
for i in range(numero):
    print(nome)