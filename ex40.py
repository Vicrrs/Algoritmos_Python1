from random import choice
a1 = input("Digite o nome do primeiro aluno: ")
a2 = input("Digite o nome do segundo aluno: ")
a3 = input("Digite o nome do terceiro aluno: ")
a4 = input("Digite o nome do quarto aluno: ")
a5 = input("Digite o nome do quinto aluno: ")
a6 = input("Digite o nome do sexto aluno: ")
a7 = input("Digite o nome do sétimo aluno: ")
a8 = input("Digite o nome do oitavo aluno: ")

lista = [a1, a2, a3, a4, a5, a6, a7, a8]
escolhido = choice(lista)

print("O aluno sorteado foi {}" .format(escolhido))