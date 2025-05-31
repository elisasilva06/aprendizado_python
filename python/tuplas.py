# cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
# while True:
#     num = int(input('digite um numero entre 0 e 20: '))
#     if 0 <= num <= 20:
#         break
#     print('tente novamente. ', end='')
# print(f'voce digitou o numero {cont[num]}')    



# times = ("Palmeiras", "Flamengo", "Cruzeiro", "Red Bull Bragantino", "Fluminense", "Ceará", "Bahia", "Corinthians", "Mirassol", "Atlético-MG", "Botafogo", "Grêmio", "São Paulo", "Internacional", "Santos", "Fortaleza", "Sport", "Vitória", "Juventude", "Vasco")
# print("-="*10)
# for cont in times:
#     print(cont)
# print("-="*10)    
# print(f"a)Os 5 primeiros times : {times[0:5]}")
# print("-="*10)
# print(f"b)Os últimos 4 colocados: {times[-4:]}")
# print("-="*10)
# print(f"c)times em ordem alfabetica: {sorted(times)}")
# print("-="*10)
# print(f'd)Em que posiçao esta o flamengo: {times.index("Flamengo")}')




# from random import randint
# numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
# print(f'Eu sorteei os valores: ', end='')
# for n in numeros:
#     print(f'{n} ',end='')
# print(f'\nO maior valor sorteado foi {max(numeros)}') 
# print(f'O menor valor sorteado foi {min(numeros)}')   


# lista = []
# for n in range (0,4):
#     num = int(input("digite um numero: "))
#     lista.append(num)
# print(f'a) quantas vezes o valor 9 apareceu: {lista.count(9)}')
# if 3 in lista:
#     print(f'b)em que posicao foi digitado o valor 3: {lista.index(3)}')
# else:
#     print("b) o valor 3 nao foi digitado")
# print('c)os valores pares digitados foram: ', end=' ')
# for num in lista:
#     if num % 2 == 0:
#         print(num, end=' ')
