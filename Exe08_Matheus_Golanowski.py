#Defina uma variável chamada total como 0 (Zero).
#Peça ao usuário para inserir cinco números e, após cada entrada, pergunte se ele deseja que esse número seja incluído (S ou s, N ou n).
#Se ele desejar, adicione o número ao total. Se ele não quiser incluí-lo, não o adicione ao total. Depois de inserir todos os cinco números, exiba o total.
print("Matheus Golanowski")
total = 0
for i in range(5):
    numero = int(input("Insira 5 numeros: "))
    incluido = input("Voçê deseja que esse numero seja incluido? S/s ou N/n")
    if incluido.lower() == "s":
        total += numero
        print("O total de numeros incluidos é de", total)
        