''' Crie uma calculadora que faça as 4 operações 
básicas da matemática, e ao final, pergunte ao usuário 
se deseja fazer outro cálculo ou se deseja encerrar o programa. 
Ao terminar, envio o arquivo .py.'''

while True:
    print(f'{'_'*20} calculadora python {'_*20'}\n')
    print('1 - Soma. ')
    print('2 - subtração. ')
    print('3 - Multiplicação. ')
    print('4 - Divisão. ')
    print('5 - Sair do programa. ')

    # Operação escolhida
    operação = input('Operação desejada: ')

    # Verificar se o usuario vai fazer a operação ou vai sair
    if operação != '5':
    #informar os valores
        x = str(input('Informe o numero 1º número: ')).replace(',', '.')
        y = str(input('Informe o número 2º número: ')).replace(',', '.')

        #Converter para float
        x = float(x)
        y = float(y)

        #Verificar a operação desejada
        match operação:
            case '1':
                print(f'{x} + {y} = {x + y}')
            case '2':
                print(f'{x} - {y} = {x - y}')
            case '3':
                print(f'{x} x {y} = {x * y}')
            case '4':
                print(f'{x} : {y} = {x / y}')
            case _:
                print('Operação invalida!')
    
        #Reiniciar loop
        continue
    else:
        print('programa encerrado!')
        break
  
            

