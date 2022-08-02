from imghdr import what
from time import sleep

def cabeçalho(txt = ""):
    """Função para otimizar cabeçalho"""
    print(txt.upper().center(22)) 
    print('_' * 22)

def moeda(num=0):
    """Função para transformar os dados monetários no formato correto"""
    return(f'R${num:.2f}'.replace('.',','))

def controle(num = 0):
    """Função facilitadora para próximas funções"""
    print(f'Você tem {moeda(num)} na conta.')

def ideal(num = 0, nam = 'Indefinido'):
    """Função que vai realizar as operações de soma e procentagem sob o salário informado"""
    while True:
        try:
            sal = float(input(f'{nam}, Qual é o seu salário mensal (limpo) no momento? -> ').replace(',','.'))
            print(f'\nSomando o seu salário com seu saldo, você terá {moeda(num + sal)} na conta')
            print('\n\033[0;33mO ideal é guardarmos de 30 a 40% do nosso salário para investimento e/ou poupança\033[m')
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número válido.\033[m')
        except(KeyboardInterrupt):
            print('\033[0;31mErro! Usuário não digitou um valor.\033[m')
        else:
            break
        des = 0
    while True:
        try:
            des = float(input('Qual a porcentagem de economia para esse mês? -> ').replace(',','.'))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número válido.\033[m')
        except(KeyboardInterrupt):
            print('\033[0;31mErro! Usuário não digitou um valor.\033[m')
        else:
            break
    if des < 30:
        print('\033[0;31mATENÇÃO!\033[m Sua porcentagem de economia está menor do que o recomendado')
    elif des > 40:
        print(' \033[0;36mSua economia será acima da média!\033[m')
    porc = des / 100
    result = sal * porc
    tot1 = result + num
    sleep(1)
    print(f'\nVocê precisa sobrar ao menos {moeda(result)} do seu salário esse mês para atingir a meta')
    print(f'Somando a sua economia desejada com o seu saldo total no momento, você ficaria com um montante de \033[0;36m{moeda(tot1)}\033[m')
    sleep(1)
    print('\nConsiderando os dados informados, podemos fazer uma projeção de saldo para os próximos anos...')
    an = ''
    an = str(input('Você deseja saber a projeção em meses[M] ou em anos[A]? -> ').upper().strip() [0])
    if an == 'A':       
        while True:
            try:
                anos = int(input('Você quer saber a projeção para quantos anos? -> '))
                yeartot = anos * 12
                money = yeartot * result
                print(f'\nGuardando {moeda(result)} durante {anos} anos, você conseguirá guardar {moeda(money)}')
                tot = num + money
                sleep(1)
                print(f'\nSomando ao seu atual saldo total, você terá \033[0;36m{moeda(tot)}\033[m de saldo.')
            except (ValueError, TypeError):
                print('\033[0;31mErro! Digite um número válido.\033[m')
            except(KeyboardInterrupt):
                print('\033[0;31mErro! Usuário não digitou um valor.\033[m')
            else:
                break
    elif an == 'M':
        while True:
            try:
                meses = int(input('Você quer saber a projeção para quantos meses? -> '))
                money = meses * result
                print(f'\nGuardando {moeda(result)} durante {meses} meses, você conseguirá guardar {moeda(money)}')
                tot = num + money
                sleep(1)
                print(f'\nSomando ao seu atual saldo total, você terá \033[0;36m{moeda(tot)}\033[m de saldo.')      
            except (ValueError, TypeError):
                print('\033[0;31mErro! Digite um número válido.\033[m')
            except(KeyboardInterrupt):
                print('\033[0;31mErro! Usuário não digitou um valor.\033[m')
            else:
                break               
    while an not in 'AaMm':
        print('\033[0;31mErro! Digite uma opção válida.\033[m')
        an = str(input('Você deseja saber a projeção em meses[M] ou em anos[A]? -> ').upper().strip() [0])





    

    
