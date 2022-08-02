from interface import *
from cadastro import *

#Leitor de arquivo com dados do cadastro
arq = 'Dadosmoney.txt'
if arquivoexiste(arq):
    print('\nArquivo encontrado com sucesso!\n')
else:
    print('\nArquivo não encontrado.\n')
    criararquivo(arq)
#Leitor de arquivo com dados do cadastro

#Programa principal
while True:
    cabeçalho('controle de saldo')
    name = str(input('\nQual o seu nome? -> '))
    print(f'Seja bem vindo \033[0;33m{name}!\033[m')
    while True:
        try:
            idade = int(input('\nQuantos anos você tem? -> '))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número válido.\033[m')
        except(KeyboardInterrupt):
            print('\033[0;31mErro! Usuário não digitou um valor.\033[m')
        else:
            break
    while True:
        try:
            qnt = float(input('Qual seu saldo total no momento? -> ').replace(',', '.').strip())
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número válido.\033[m')
        except(KeyboardInterrupt):
            print('\033[0;31mErro! Usuário não digitou um valor.\033[m')
        else:
            break

    controle(qnt)
    ideal(qnt, name)
    cadastrar(arq, name, qnt)
    continuar = str(input('Você deseja realizar outra analise financeira?[S/N] -> ')).strip() .upper()
    while continuar not in 'SN':
        print('Desculpe, não entendi...\n')
        continuar = str(input('Você deseja continuar?[S/N] -> ')).strip() .upper()
    print('\n')
    if continuar in 'nN':
        break
#Programa principal

#Leitor de arquivo
why = str(input('Você deseja conferir os dados cadastrados em nosso sistema?[S/N] -> ')).strip() .upper()
while why not in 'SN':
    print('Desculpe, não entendi...\n')
    why = str(input('Você deseja continuar?[S/N] -> ')).strip() .upper()
print('\n')
if why == 'S':
    lerarquivo('Dadosmoney.txt')
#Leitor de arquivo

    
print('\n')
cabeçalho('fim do programa')

