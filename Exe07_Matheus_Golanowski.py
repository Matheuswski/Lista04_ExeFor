#Peça ao usuário para inserir seu nome e um número. Se o número for menor que 10, exiba o nome dele esse número de vezes; caso contrário, exiba a mensagem “Numero muito alto" três vezes.
print("Matheus Golanowski")
nome = input("Insira seu nome: ")
numero = int(input("Insira um numero: "))
if numero <10:
    for i in range(numero):
        print(nome)
else:
    for i in range(3):
     print("Numero muito alto")