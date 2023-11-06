# Exercício Python 28 : Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
anoatual = int(input("Digite o ano atual: "))
maiorid = []
menorid = []
anonasc = []
for i in range(1,8):
    anonas = int(input("Digite um ano de nascimento: "))
    anonasc.append(anonas)
    if anoatual - anonas >= 18:
        maiorid.append(anonas)
    else:
        menorid.append(anonas)
print("As pessoas que nasceram em ", maiorid, "já são maiores de idade!")
print("As pessoas que nasceram em ", menorid, "ainda não atingiram a maioridade!")