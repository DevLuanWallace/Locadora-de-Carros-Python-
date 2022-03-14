import os
import random

def escolha_categoria(escolha,Compacto,Sedan,SUV,Esportivo,Modificado):
    escolha = escolha.lower()
    if escolha == 'compacto':
        print('')
        print('Da uma olhada na lista de carros dessa categoria:')
        print('')
        for carro in Compacto:
            print('')
            for a,v in carro.items():
                print(a,'-',v)
        '''A funcao pega faz um for e imprime todos os campos da agenda de cada carro que esta na categoria Compacto '''            
        
    elif escolha == 'sedan': 
        print('')
        print('Da uma olhada na lista de carros dessa categoria:')
        print('')
        for carro in Sedan:
            print('')
            for a,v in carro.items():
                print(a,'-',v)        
        '''A funcao pega faz um for e imprime todos os campos da agenda de cada carro que esta na categoria Compacto '''            

    elif escolha == 'suv':
        print('')
        print('Da uma olhada na lista de carros dessa categoria:')
        print('')
        for carro in SUV:
            print('')
            for a,v in carro.items():
                print(a,'-',v)
        '''A funcao pega faz um for e imprime todos os campos da agenda de cada carro que esta na categoria Compacto '''            

    elif escolha == 'esportivo':
        print('')
        print('Da uma olhada na lista de carros dessa categoria:')
        print('')
        for carro in Esportivo:
            print('')
            for a,v in carro.items():
                print(a,'-',v)
        '''A funcao pega faz um for e imprime todos os campos da agenda de cada carro que esta na categoria Compacto '''                    

    elif escolha == 'modificado':
        print('')
        print('Da uma olhada na lista de carros dessa categoria:')
        print('')
        for carro in Modificado:
            print('')
            for a,v in carro.items():
                print(a,'-',v)
        '''A funcao pega faz um for e imprime todos os campos da agenda de cada carro que esta na categoria Compacto ''' 

    else:
        print('Acho que nao entendi a categoria que voce digitou!')
        print('Tente Novamente, caso deseje..')

def desconto_reserva(cupom_desconto,custo):
    if cupom_desconto == '5OFF':
        custo_final = custo*0.95
        return custo_final

    elif cupom_desconto == '7OFF':
        custo_final = custo*0.93
        return custo_final

    elif cupom_desconto == '10OFF':
        custo_final = custo*0.9
        return custo_final

    elif cupom_desconto == '12OFF':
        custo_final = custo*0.88
        return custo_final

    elif cupom_desconto == '15OFF':
        custo_final = custo*0.75
        return custo_final

def menu():
    print(' ')
    print('====================MENU===================')
    print('1......... Ver Carros .....................')
    print('2......... Fazer Reservas .................')
    print('3......... Carregar Reservas do usuario ...')
    print('4......... Sortear Carros Promocionais ....')
    print('5......... Excluir Cadastro ...............')
    print('0......... SAIR ...........................')
    print(' ')

def main():
    '''=== Dicionarios de cada carro ==='''
    '''COMPACTOS'''
    Sandero = {
            'Nome':'Renault Sandero' ,
            'Cambio':'CVT' ,'Potencia':'118cv' ,
            'Torque':'16,3 Kgf.m' ,
            'Oa100':'11s' ,
            'Cor':'Prata' ,
            'Custo':35
            }
    Onix = {
            'Nome':'Chevrolet Onix' ,
            'Cambio':'Manual' ,
            'Potencia':'116cv' ,
            'Torque':'16,8 Kgf.m' ,
            'Oa100':'10,1s' ,
            'Cor':'Preto' ,
            'Custo':38
            }
    Etios = {
            'Nome':'Toyota Etios' ,
            'Cambio':'Automatico' ,
            'Potencia':'98cv' ,
            'Torque':'13,1 Kgf.m' ,
            'Oa100':'11,8s' ,
            'Cor':'Vermelho' ,
            'Custo':32
            }
    A1 = {
            'Nome': 'Audi A1' ,
            'Cambio':'Automatico' ,
            'Potencia':'125cv' ,
            'Torque':'20,4 Kgf.m' ,
            'Oa100':'8,9s' ,
            'Cor':'Branco' ,
            'Custo':50
            }
    '''SEDANS'''
    Civic = {
            'Nome':'Honda Civic' ,
            'Cambio':'CVT' ,
            'Potencia':'155cv' ,
            'Torque':'19,5 Kgf.m' ,
            'Oa100':'9,5s' ,
            'Cor':'Preto' ,
            'Custo':60
            }
    Corolla = {
            'Nome':'Toyota Corolla' ,
            'Cambio':'CVT' ,
            'Potencia':'177cv' ,
            'Torque':'21,4 Kgf.m' ,
            'Oa100':'9,7s' ,
            'Cor':'Vinho' ,
            'Custo':62
            }
    Fusion = {
            'Nome':'Ford Fusion' ,
            'Cambio':'Automatico' ,
            'Potencia':'248cv' ,
            'Torque':'38,0 Kgf.m' ,
            'Oa100':'7,3s' ,
            'Cor':'Branco' ,
            'Custo':70
            }
    Sentra = {
            'Nome':'Nissan Sentra' ,
            'Cambio':'CVT' ,
            'Potencia':'140cv' ,
            'Torque':'20,3 Kgf.m' ,
            'Oa100':'9,5s' ,
            'Cor':'Prata' ,
            'Custo':65
            }
    A3 = {
            'Nome':'Audi A3' ,
            'Cambio':'Automatico' ,
            'Potencia':'220cv' ,
            'Torque':'35,7 Kgf.m' ,
            'Oa100':'6,9s' ,
            'Cor':'Cinza' ,
            'Custo':70
            }
    Fluence = {
            'Nome':'Renault Fluence' ,
            'Cambio':'CVT' ,
            'Potencia':'140cv' ,
            'Torque':'20,3 Kgf.m' ,
            'Oa100':'9,5s' ,
            'Cor':'Ametista' ,
            'Custo':65
            }
    '''SUV'''
    Amarok = {
            'Nome':'VolksWagem Amarok' ,
            'Cambio':'Manual' ,
            'Potencia':'180cv' ,
            'Torque':'40,8 Kgf.m' ,
            'Oa100':'11,1s' ,
            'Cor':'Prata' ,
            'Custo':80
            }
    S10 = {
            'Nome':'Chevrolet S10' ,
            'Cambio':'Manual' ,
            'Potencia':'180cv' ,
            'Torque':'44,87 Kgf.m' ,
            'Oa100':'10,3s' ,
            'Cor':'Branco' ,
            'Custo':82
            }
    Ranger = {
            'Nome':'Ford Ranger' ,
            'Cambio':'Manual' ,
            'Potencia':'160cv' ,
            'Torque':'39,3 Kgf.m' ,
            'Oa100':'10,7s' ,
            'Cor':'Prata' ,
            'Custo':80
            }
    Toro = {
            'Nome':'Fiat Toro' ,
            'Cambio':'Manual' ,
            'Potencia':'139cv' ,
            'Torque':'19,3 Kgf.m' ,
            'Oa100':'12,2s' ,
            'Cor':'Branco' ,
            'Custo':75
            }
    '''ESPORTIVOS'''
    Nissan370z = {
            'Nome':'Nissan 370z' ,
            'Cambio':'Manual' ,
            'Potencia':'328cv' ,
            'Torque':'37,0 Kgf.m' ,
            'Oa100':'5,3s' ,
            'Cor':'Preto' ,
            'Custo':100
            }
    Mustang = {
            'Nome':'Ford Mustang' ,
            'Cambio':'Automatico' ,
            'Potencia':'466cv' ,
            'Torque':'56,7 Kgf.m' ,
            'Oa100':'4,3s' ,
            'Cor':'Azul' ,
            'Custo':120
            }
    Challenger = {
            'Nome':'Dodge Challenger' ,
            'Cambio':'Manual' ,
            'Potencia':'717cv' ,
            'Torque':'89,8 Kgf.m' ,
            'Oa100':'4s' ,
            'Cor':'Verde' ,
            'Custo':130
            }
    RS3 = {
            'Nome':'Audi RS3' ,
            'Cambio':'Automatico' ,
            'Potencia':'400cv' ,
            'Torque':'48,9 Kgf.m' ,
            'Oa100':'4,1s' ,
            'Cor':'Preto' ,
            'Custo':122
            }
    Huracan = {
            'Nome':'Lamborghini Huracan' ,
            'Cambio':'Automatico' ,
            'Potencia':'610cv' ,
            'Torque':'57,1 Kgf.m' ,
            'Oa100':'3,2s' ,
            'Cor':'Laranja' ,
            'Custo':150
            }
    Aventador = {
            'Nome':'Lamborghini Aventador' ,
            'Cambio':'Automatico' ,
            'Potencia':'700cv' ,
            'Torque':'70,4 Kgf.m' ,
            'Oa100':'2,9s' ,
            'Cor':'Marrom' ,
            'Custo':155
            }
    Lancer = {
            'Nome':'Mitsubish Lancer Evo X' ,
            'Cambio':'Automatico' ,
            'Potencia':'295cv' ,
            'Torque':'37,32 Kgf.m' ,
            'Oa100':'6,3s' ,
            'Cor':'Branco' ,
            'Custo':100
            }
    M3 = {
            'Nome':'Bmw M3' ,
            'Cambio':'Automatico' ,
            'Potencia':'431cv' ,
            'Torque':'56,1 Kgf.m' ,
            'Oa100':'4,1s' ,
            'Cor':'Cinza' ,
            'Custo':125
            }
    R35 = {
            'Nome':'Nissan GTR' ,
            'Cambio':'Automatico' ,
            'Potencia':'572cv' ,
            'Torque':'65,0 Kgf.m' ,
            'Oa100':'2,8s' ,
            'Cor':'Branco' ,
            'Custo':135
            }
    '''MODIFICADOS'''
    Gol = {
            'Nome':'VolksWagem Gol Quadrado' ,
            'Cambio':'Manual' ,
            'Potencia':'270cv' ,
            'Torque':'35 Kgf.m' ,
            'Oa100':'6,5s' ,
            'Cor':'Preto' ,
            'Custo':70
            }
    RCZ = {
            'Nome':'Peugeot RCZ' ,
            'Cambio':'Manual' ,
            'Potencia':'250cv' ,
            'Torque':'30,5 Kgf.m' ,
            'Oa100':'7s' ,
            'Cor':'Prata' ,
            'Custo':78
            }
    CivicSI = {
            'Nome':'Honda Civic SI' ,
            'Cambio':'Manual' ,
            'Potencia':'390cv' ,
            'Torque':'42,7 Kgf.m' ,
            'Oa100':'5,3s' ,
            'Cor':'Vermelho' ,
            'Custo':85
            }
    DS3 = {
            'Nome':'Citroen DS3' ,
            'Cambio':'Manual' ,
            'Potencia':'280cv' ,
            'Torque':'32,0 Kgf.m' ,
            'Oa100':'5,7s' ,
            'Cor':'Roxo' ,
            'Custo':80
            }
    '''=== dicionario de carros === '''

    '''CATEGORIAS'''
    Compacto = (Sandero,Onix,Etios,A1)
    Sedan = (Civic,Corolla,Fusion,Sentra,A3,Fluence)
    SUV = (Amarok,S10,Ranger,Toro)
    Esportivo = (Nissan370z,Mustang,Challenger,RS3,Huracan,Aventador,Lancer,M3,R35)
    Modificado = (Gol,RCZ,CivicSI,DS3)
    '''Foi organizado em tuplas (para que nao seja alterado o conteudo) os modelos das categorias de carros '''

    exit = True
    while exit:
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        menu()
        op = input('Escolha a opcao desejada: (0 para SAIR)\n')
        print('')

        if op == '1':
            print('')
            print('Ola, nos temos 5 categorias:')
            print('COMPACTO (hatchs)')
            print('SEDAN (medios/grandes)')
            print('SUV (pick-ups)')
            print('ESPORTIVO (exotic/muscle cars)')
            print('MODIFICADO (antigos/novos)')
            print('')
            escolha = str(input('Em qual voce gostaria de acelerar? \n'))
            escolha = escolha.lower()
            escolha_categoria(escolha,Compacto,Sedan,SUV,Esportivo,Modificado)
            exit = True

        elif op == '2':
            status = False
            Sair = True
            count = 0
            print('- Ola, vi que voce quer fazer uma reserva!')
            nome = str(input('Primeiramente, qual o seu nome?\n'))
            nome = nome.upper()
            nome = nome + '.txt'      
            '''Aqui eu concateno a extensao de arquivo para poder abrir com o nome do usuario'''
            ArqUserA = open(nome,'a') 
            '''Abri com append para poder add conteudo ao arquivo ou cria-lo caso ele nao exista'''
            ArqUserR = open(nome, 'r')
            ArqCarros = open('ListaCarros.txt','r')
            '''Abre a ListaCarros.txt no modo leitura'''
            ArqReservasR = open('Reservas.txt','r')
            ArqReservasA = open('Reservas.txt','a')
            '''Abre Reservas.txt no modo leitura e escrita para conferencia e adicao de mais reservas'''
            ArqCupom = open('CuponsDesconto.txt','r')
            cont = 0
            contador_cupom = 0

            for line in ArqUserR:
                cont+=1
            ''' Aqui eu contei o numero de linhas que tem no arquivo, se for maior q 0, ja tem cadastro. Se for 0 o arquivo eh novo'''

            if cont == 0: 
                print('')
                print('- Pelo que estou vendo aqui voce eh um novo usuario! Vamos iniciar o cadastro')
                NomeCompleto = input('Dessa vez preciso do seu nome completo:\n')
                Idade = int(input('Qual a sua idade? (Desculpa mas preciso saber se voce tem idade para dirigir nossas maquinas)\n'))

                if Idade < 18:
                    print('- Desculpe, mas voce eh muito novinho!! Nao posso continuar seu cadastro!')
                    os.remove(nome)
                    '''Aqui removo o arquivo com o nome do usuario caso ele seja menor de idade'''
                    exit = True

                XPcarro = input('Tem experiencia com carros? (Sim/Nao)\n')
                CPF = input('Qual seu CPF?\n')
                '''Agora iremos preencher o arquivo'''
                ArqUserA.write('Nome: '+NomeCompleto+'\n')
                ArqUserA.write('Idade: '+str(Idade)+'\n')
                ArqUserA.write('Tem Experiencia: '+str(XPcarro)+'\n')
                ArqUserA.write('CPF: '+CPF+'\n')
                ArqUserA.write('Reservas:'+'\n')

            while Sair:
                count = 0
                print('')
                print('- Vamos dar inicio as reservas:')
                resposta = input('Voce deseja rever alguma categoria? (sim/nao)\n')
                resposta = resposta.lower()

                if resposta == 'sim':
                    print('')
                    categoria = input('Qual a categoria desejada? (Compacto/Sedan/SUV/Esportivo/Modificado)\n')
                    categoria = categoria.lower()
                    escolha_categoria(categoria,Compacto,Sedan,SUV,Esportivo,Modificado)
                    '''chamei a funcao que mostra a lista de carros por categoria'''
                    Sair = True

                elif resposta == 'nao':
                    marca_carro = str(input('Tudo bem! Qual marca do carro que voce quer reservar?\n'))
                    modelo_carro = str(input('Qual o modelo do carro que voce quer reservar?\n'))
                    marca_carro = marca_carro.lower()
                    modelo_carro = modelo_carro.lower()
                    carro_escolhido = marca_carro+modelo_carro
                    '''Aqui deixa no modelo para fazer a checagem na lista de carros'''

                    for line in ArqCarros:
                        if carro_escolhido in line:
                            '''Aqui fazemos a checagem do nome do carro na lista de veiculos da locadora'''
                            print('')
                            print('- Maneiro! Parece que este carro que voce escolheu esta na nossa lista de veiculos!')
                            print('- Espera so um pouquinho que vou checar se esta disponivel para reserva!')
                            print('')
                            custo = int(line[-4:-1])
                            ''' AQUI A GENTE PEGA O VALOR DO CARRO E COLOCA EM ALGUMA VARIAVEL TEMPORARIA PARA USAR QUANDO VALIDAR O CUPOM '''
                            status = True
            
                    if status == True:
                        for linha in ArqReservasR:
                            if carro_escolhido in linha:
                                '''Caso ele n esteja na lista de Reservas, podera reservar na lista de reservas e no arquivo do usuario'''
                                count += 1

                        if count == 0:
                            print('- Que bom! O carro esta disponivel para reserva...')
                            Tem_cupom = input('Mas antes... Voce tem algum cupom de desconto? (sim/nao) ')
                            Tem_cupom = Tem_cupom.lower()

                            if Tem_cupom == 'sim':
                                print('')
                                cupom_desconto = input('Legal! Digite o cupom: ')
                                print('- Espera so um minuto que iremos verificar se o cupom eh valido!')
                                print('')
                                for cupom in ArqCupom:
                                    if cupom_desconto in cupom:
                                        print('teste')
                                        contador_cupom += 1

                                if contador_cupom >= 1:
                                    print('- Que otimo! Este cupom eh valido em nossa loja! ')
                                    ArqReservasA.write(carro_escolhido+'\n')
                                    ArqUserA.write(marca_carro.upper()+' ' + modelo_carro.upper()+'\n')
                                    custo = desconto_reserva(cupom_desconto,custo)
                                    ArqUserA.write(str(custo)+'\n')
                                    print('- Pronto! Ja reservamos seu carro com o respectivo desconto e esta disponivel no seu cadastro com a loja!')
                                    ''' AQUI A GENTE ATRIBUI O VALOR DO CUPOM NO VALOR DO VEICULO, CASO O CUPOM ESTEJA DISPONIVEL'''
                                    Sair = False
                                    exit = True

                                elif contador_cupom == 0:
                                    print('- Que mau! Nao achamos este cupom!')
                                    ArqReservasA.write(carro_escolhido+'\n')
                                    ArqUserA.write(marca_carro.upper()+' ' + modelo_carro.upper()+'\n')
                                    ArqUserA.write(str(custo)+'\n')
                                    print('- Mas relaxa! Ja reservamos seu carro e esta disponivel no seu cadastro com a loja!')
                                    ''' AQUI A GENTE CADASTRA O VALOR DO CARRO SEM O DESCONTO PQ NAO ACHAMOS O CUPOM DISPONIVEL NO ARQUIVO '''
                                    Sair = False
                                    exit = True

                            elif Tem_cupom == 'nao':
                                print('')
                                print('- De boa, vamos reservar sem cupom mesmo!')
                                ArqReservasA.write(carro_escolhido+'\n')
                                ArqUserA.write(marca_carro.upper()+' '+ modelo_carro.upper()+'\n')
                                ArqUserA.write(str(custo)+'\n')
                                print('- Ja reservamos seu carro e esta disponivel no seu cadastro com a loja!')
                                ''' CASO A PESSOA NAO QUEIRA ADD ALGUM CUPOM DE DESCONTO '''
                                Sair = False
                                exit = True

                            else:
                                print('Cara...')
                                print('Resposta incorreta! Tente Novamente')
                                Sair = True

                        elif count >= 0:
                            ''' Caso ele esteja na lista de Reservas, nao podera reservar'''
                            print('')
                            print('- Infelizmente este carro ja foi reservado, volte e reserve outro')
                            Sair = True

                    elif status == False:
                        print('- Poxa, infelizmente nao temos este carro! Volte e alugue outro!')
                        Sair = False
                        exit = True
                
            ArqReservasR.close()
            ArqReservasA.close()
            ArqCarros.close()
            ArqUserR.close()
            ArqUserA.close()
            ArqCupom.close()
            exit = True

        elif op == '3':
            try:
                print('')
                user = str(input('Qual o seu nome para que possamos verificar seus dados? '))
                user = user.upper()
                user = user+'.txt'
                ArquivoLerUser = open(user,'r')
                print('== Segue suas informacoes: ==\n')
                for dados in ArquivoLerUser:
                    print(dados)
                print('')
                print('Obrigado!')
                exit = True

            except FileNotFoundError:
                print('Poxa, infelizmente nao achamos seu cadastro conosco!')
                exit = True

        elif op == '4':
            print('Ola, iremos sortear carros com descontos promocionais!')
            print('')
            sorteio_cupom = random.randint(1,5)
            if sorteio_cupom == 1:
                print('Boa!! Voce liberou este codigo de desconto >> 5OFF')
                print('Anote ele para ter descontos em uma reserva!')
                print('E olha, nao esqueca de digitar o codigo corretamente!')
                exit = True

            elif sorteio_cupom == 2:
                print('Boa!! Voce liberou este codigo de desconto >> 7OFF')
                print('Anote ele para ter descontos em uma reserva!')
                print('E olha, nao esqueca de digitar o codigo corretamente!')
                exit = True

            elif sorteio_cupom == 3:
                print('Boa!! Voce liberou este codigo de desconto >> 10OFF')
                print('Anote ele para ter descontos em uma reserva!')
                print('E olha, nao esqueca de digitar o codigo corretamente!')
                exit = True

            elif sorteio_cupom == 4:
                print('Boa!! Voce liberou este codigo de desconto >> 12OFF')
                print('Anote ele para ter descontos em uma reserva!')
                print('E olha, nao esqueca de digitar o codigo corretamente!')
                exit = True

            elif sorteio_cupom == 5:
                print('Boa!! Voce liberou este codigo de desconto >> 15OFF')
                print('Anote ele para ter descontos em uma reserva!')
                print('E olha, nao esqueca de digitar o codigo corretamente!')
                exit = True

        elif op == '5':
            try:
                print('')
                userRemove = str(input('Qual o seu nome para que possamos excluir seu cadastro? '))
                userRemove = userRemove.upper()
                ''' Pega o nome que a pessoa digitou e coloca em maiuscula, padrao como esta o arquivo'''
                userRemove = userRemove+'.txt'
                os.remove(userRemove)
                ''' Aqui removemos o arquivo depois de concatenar o nome do arquivo com .txt'''
                print('')
                print('Uma pena termos perdido voce, espero que um dia possa voltar!')
                exit = True
                
            except FileNotFoundError:
                print('Poxa, infelizmente nao achamos seu cadastro conosco!')
                exit = True
                ''' Cao nao ache o arquivo ele retorna essa mensagem e volta para o menu'''

        elif op == '0':
            print('Muito Obrigado por usar o meu programa!')
            frase = 'Feito por Luan Wallace ^_^)'
            return frase
            '''Return ja finaliza o programa '''

        else:
            print('Opcao invalida!')
            print('')
            exit = True

print(main())
