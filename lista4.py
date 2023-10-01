
import time
sair = 0

while sair == 0:
    time.sleep(0.8)

    print("\n\nExercicios:")
    print("0 - Sair")
    print("1 - Meu Curso é Show 10x")
    print("2 - Ler inteiro, Estou sabendo Programar haha")
    print("3 - Imprimir números na tela até 100")
    print("4 - Imprimir 500,497,494 ... 2 na tela")
    print("5 - De 1000 em 1000")
    print("6 - Ler 10 valores e exibir soma")
    print("7 - Ler 10 valores e exibir média")
    print("8 - Ler 10 valores positivos, ignorando os negativos e exibir média")
    print("9 - Ler 10 valores e exibir o maior e o menor valor recebido")
    print("10 - Ler valor inteiro N")
    print("11 - Exibir soma dos 50 primeiros números pares")
    print("12 - Calcular Fatorial")
    print("13 - Exibir divisores")
    print("14 - Primo ou não")
    print("15 - Ler certa quantidade de números e exibir o maior deles")
    print("16 - ")
    print("17 - ")
    print("18 - ")
    print("19 - ")
    print("20 - ")
    print("21 - ")
    print("22 - ")
    print("23 - ")
    print("24 - ")
    print("25 - ")
    print("26 - ")
    print("27 - ")

    escolha = int(input("Executar: "))

    # =======================================
    # SAIR ==================================
    if escolha == 0:
        print("Programa finalizado.")

        break

    # =======================================
    # QUESTÃO 1 =============================

    if escolha == 1:
        i = 1
        while i <= 10:
            i+=1
            print("Meu curso é Show")
        
        print("")
    
    # =======================================
    # QUESTÃO 2 =============================

    elif escolha == 2:
        i = int(input("Digite o número de vezes: "))
        while i >= 1:
            print("Estou sabendo programar")
            i-=1
        print("")
    
    # =======================================
    # QUESTÃO 3 =============================

    elif escolha == 3:
        i = 1
        while i<=100:
            print(i)
            i+=1
        print("")
    
    # =======================================
    # QUESTÃO 4 =============================

    elif escolha == 4:
        i = 500
        while i>=2:
            print(i)
            i-=3
        print("")
    
    # =======================================
    # QUESTÃO 5 =============================

    elif escolha == 5:
        num = int(input("Digite um número: "))
        i = 0
        while i<=100000:
            print(i+num)
            i+=1000
        print("")
    
    # =======================================
    # QUESTÃO 6 =============================

    elif escolha == 6:
        i = 1
        soma = 0
        while i<=10:
            num = int(input("Digite um número: "))
            soma+=num
            i+=1
        print(f"Soma é: {soma}")

        print("")
    
    # =======================================
    # QUESTÃO 7 =============================

    elif escolha == 7:
        
        i = 1
        soma = 0
        while i<=10:
            num = int(input("Digite um número: "))
            soma+=num
            i+=1
        media = int(soma/10)
        print(f"Média é: {media}")

        print("")
    
    # =======================================
    # QUESTÃO 8 =============================

    elif escolha == 8:

        i = 1
        soma = 0
        negativos = 0
        while i<=10:
            num = int(input("Digite um número: "))
            if num<0:
                negativos+=1
            else:
                soma+=num
            i+=1
        media = int(soma/(10-negativos))
        print(f"Média dos positivos é: {media}")

        print("")
    
    # =======================================
    # QUESTÃO 9 =============================

    elif escolha == 9:

        i = 1
        maior = float('-inf')
        menor = float('inf')
        while i<=10:
            num = int(input(f"Digite o {i}º número: "))
            if num>=maior:
                maior = num
            elif num<=menor:
                menor = num                
            i+=1
        
        print(f"O maior número é {maior} e o menor número é {menor}")

        print("")
    
    # =======================================
    # QUESTÃO 10 ============================

    elif escolha == 10:

        valor = int(input("Digite um número: "))
        i = 1
        while i<=valor:
            print(i)
            i+=2
        print("")
    
    # =======================================
    # QUESTÃO 11 ============================

    elif escolha == 11:
        i = 1
        pares = 2
        soma = 0
        while i<=50:
            soma+=pares
            pares+=2
            i+=1
        print('A soma dos 50 primeros números pares é')
        print(soma)
        print("")
    
    # =======================================
    # QUESTÃO 12 ============================

    elif escolha == 12:
        
        num = int(input("Digite um número: ") )
        fat=1
        i=1
        while i <= num:
            fat = fat * i
            i += 1

        print(f"{num}! é {fat}")

    # =======================================
    # QUESTÃO 13 ============================

    elif escolha == 13:
        num = int(input("Digite um número: ") )
        div = 1
        print(f"Divisores de {num}")
        while div<=num:
            if num%div==0:
                print(div)
            div+=1

        
        print("")
    
    # =======================================
    # QUESTÃO 14 ============================

    elif escolha == 14:
        #14. Faça um programa que receba um valor inteiro n ≥ 0 e imprima se esse número é primo ou não.

        num = int(input("Digite o número: "))
        i = 2
        primo = 0

        while i<num:
            if num%i==0:
                primo+=1
            i+=1
                

        if primo == 0:
            print(f"{num} é um número primo")
        else:
            print(f"{num} NÃO é um número primo")
        

        print("")
    
    # =======================================
    # QUESTÃO 15 ============================

    elif escolha == 15:
        #15. Escreva um programa que leia certa quantidade de números e imprima o maior deles e quantas vezes
        # o maior número foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário.
        loop = 0
        maior = 0
        menor = 0
        resp = 0
        while loop==0:

            print("Digite um número ou 'P' para parar:")
            resp = input(": ")

            if resp=="P" or resp =="p":

                print(f"O maior número é {maior} e o menor número é {menor}")
                loop+=1

            else:
                if int(resp)>maior:
                    maior = int(resp)
                else:
                    menor = int(resp)
        
        print("Finalizado")
                


        

        print("")
    
    # =======================================
    # QUESTÃO 16 ============================

    elif escolha == 16:
#16. O número de Fibonacci Fn para n > 0 é definido da seguinte maneira:
#F1 = 1
#F2 = 1
#Fn = Fn−1 + Fn−2 para n > 2
#Faça um programa que receba um valor inteiro n digitado pelo usuário e calcule e Fn.

        n = int(input("Valor de n"))
        i = 0 
        fn = 0
        f2 = 1
        while i<=n:
            print(fn)
            fn+=f2
            f2+=1
            i+=1

            
        print(f"Número final da sequência {fn}")






        print("")
    
    # =======================================
    # QUESTÃO 17 ============================

    elif escolha == 17:

#         17. Faça um programa que receba dois números. Calcule e mostre:
#  A soma dos números pares desse intervalo de números, incluindo os números dados;
#  A multiplicação dos números ímpares desse intervalo, incluindo os digitados
        num1 = int(input("Digite o primeiro número: ")) # 10
        num2 = int(input("Digite o segundo número: "))# 20
        soma = 0
        mult = 1

        if num1>num2:
            i = num2
            while i<=num1:
                if(i%2 == 0):
                    #par
                    soma+=i
                else:
                    #impar
                    mult*=i
                i+=1
        else:
            i = num1
            while i<=num2:
                if(i%2 == 0):
                    #par
                    soma+=i
                else:
                    #impar
                    mult*=i
                i+=1

        print(f"A soma dos pares no intervalo é {soma}")
        print(f"A soma dos pares no intervalo é {mult}")

        print("")
    
    # =======================================
    # QUESTÃO 18 ============================

    elif escolha == 18:
        print("")
    
    # =======================================
    # QUESTÃO 19 ============================

    elif escolha == 19:
        print("")

    # =======================================
    # QUESTÃO 20 ============================

    elif escolha == 20:
        print("")

    # =======================================
    # QUESTÃO 21 ============================

    elif escolha == 21:
        print("")

    # =======================================
    # QUESTÃO 22 ============================

    elif escolha == 22:
        print("")

    # =======================================
    # QUESTÃO 23 ============================

    elif escolha == 23:
        print("")

    # =======================================
    # QUESTÃO 24 ============================

    elif escolha == 24:
        print("")

    # =======================================
    # QUESTÃO 25 ============================
    elif escolha == 25:
        print("")

    # =======================================
    # QUESTÃO 26 ============================

    elif escolha == 26:
        print("")
    # =======================================
    # QUESTÃO 27 ============================

    elif escolha == 27:
        print("")

    # =======================================

    else:
        print("Deus é bom")
        print("")
