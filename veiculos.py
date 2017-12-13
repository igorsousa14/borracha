from math import *
from string import *
import sys
from datetime import datetime
class Vei:

    today = datetime.now()
    day = today.day
    month = today.month
    year = today.year

    marca = 0
    modelo = 0
    ano = 0
    valor = 0
    codigo = 0

    lveiculos = []
    lmarca = []
    lmodelo =[]
    lano = []
    lvalor = []
    lcodigo = []


    while True:
            
            print('Menu\n')
            print('Escolha uma Opção: ')
            print('1 - Consultar Veiculos')
            print('2 - Adicionar Veiculos')
            print('3 - Alugar/reservar veiculos')
            print('4 - Devolver/liberar veiculos')
            print('5 - Excluir veiculos')
            print('6 - Avançar data atual')
            print('7 - Sair')

            print('Data atual:%d/'%(day),'%d/'%(month),'%d'%(year))
            print('Quantidade de veiculos: xx ')
            print('Quantidade de veiculos alugados: xx ')
            print('Quanditade de atrasos: xx\n')

            op = int(input('Escolha Uma Opção: '))

            if op == 1:

               for item in lmarca:
                   print(item)
               for item in lmodelo:
                   print(item)
               for item in lano:
                   print(item)
               for item in lvalor:
                   print(item)
               for item in lcodigo:
                   print(item)


            if op == 2:
                
                
                print('Digite a marca: ')
                marca = input()
                lmarca.append(marca)
            
                print('Digite o modelo ')
                modelo = input()
                lmodelo.append(modelo)

                print('Digite o ano: ')
                ano = int(input())
                lano.append(ano)

                print('Digite o valor: ')
                valor = int(input())
                lvalor.append(valor)

                print('Codigo Criado')
                lcodigo.append(codigo + 1)

                print('Carro cadastrado\n')
                pass

          
            if op == 5:
                print('Digite o veiculo a ser excluido: ')
            if op == 6:
                
                day = today.day +1
                
            if op == 7:
                
                
                sys.exit(0)


                pass
    
    

    

            
        
        
            
        

    
            

            
               
   
    
            

    

    
        
        
            
    
