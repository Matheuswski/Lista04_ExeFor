#Peça um número abaixo de 50 e, em seguida, faça uma contagem regressiva de 50 até esse número, certificando-se de mostrar o número que eles inseriram na saída.
print("Matheus Golanowski")
numero = int(input("Digite um numero menor que 50: "))
for i in range(50, numero -1, -1):
    print(i)