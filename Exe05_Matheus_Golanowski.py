#Peça ao usuário para inserir um número que deseja a tabuada e, em seguida, exibir a tabuada para esse número.
print("Matheus Golanowski")
numero = int(input("Digite um numero que deseja fazer a tabuada: "))
print("Tabuada do numero", numero)
for i in range(11):
    print("{} x {} = {}".format(numero,i,numero * i))
    