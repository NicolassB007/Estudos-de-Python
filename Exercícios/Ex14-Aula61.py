import os
cpf_convertido_para_int = 0
tamanho_cpf = 0
resultado_soma_vezes_dez = 0 # Esse valor é apenas para definir a variável
primeiro_digito_cpf = 0 # Esse valor não é o final!!
segundo_digito_cpf = 0 # Esse valor não é o final!!
modulo_soma_vezes_dez = 0
cpf_final = ''

cpf_convertido_com_sucesso = None

numeros_do_cpf = []
resultado_multiplicacao = [] # Resultados da multiplicação da lista numeros_do_cpf #                              com numeros de 10 até 2
soma_total_de_todos_os_numeros_multiplicados = []
contador = 1

while True:
    print("Informe seu CPF SEM PONTOS E TRAÇOS")
    print("E informe APENAS OS 8 PRIMEIROS DIGITOS")
    cpf = input("Informe seu CPF: ")

    if len(cpf) > 9:
        os.system("cls")
        print("Você informou mais que 9 digitos do cpf!")
        continue
    elif len(cpf) < 0:
        os.system("cls")
        print("Você informou poucos digitos!")
    elif len(cpf) == 9:
        for numero_cpf in cpf:
            try:
                cpf_convertido_para_int = int(numero_cpf)
                cpf_convertido_com_sucesso = True
            except:
                cpf_convertido_com_sucesso = None

            if cpf_convertido_com_sucesso is True:
                numeros_do_cpf.append(cpf_convertido_para_int)
            else:
                os.system("cls")
                print("Valor do CPF inválido!")
                continue

        indice = 0
        for contagem_regressiva in range(10, 1, -1):
            multiplicacao = numeros_do_cpf[indice] * contagem_regressiva
            resultado_multiplicacao.append(multiplicacao)
            indice += 1
        
        indice = 0
        soma = 0
        for numeros in resultado_multiplicacao:
            soma += numeros

        resultado_soma_vezes_dez = soma * 10   
        modulo_soma_vezes_dez = resultado_soma_vezes_dez % 11

        primeiro_digito_cpf = modulo_soma_vezes_dez if modulo_soma_vezes_dez <= 9 else 0

        numeros_do_cpf.append(primeiro_digito_cpf)
        print(f"PRIMEIRO DIGITO É {primeiro_digito_cpf}")

        # Reutilizando a estrutura anterior para conseguir o segundo digito
        resultado_multiplicacao = [] # Zerando a lista de resultados da #                            multiplicação de todos os números do cpf    

        indice = 0
        for contagem_regressiva in range(11, 1, -1):
            multiplicacao = numeros_do_cpf[indice] * contagem_regressiva
            resultado_multiplicacao.append(multiplicacao)
            indice += 1

        indice = 0
        soma = 0
        for numeros in resultado_multiplicacao:
            soma += numeros

        resultado_soma_vezes_dez = 0 # Zerando o valor da variável
        resultado_soma_vezes_dez = soma * 10

        modulo_soma_vezes_dez = 0 # Zerando o valor da variável
        modulo_soma_vezes_dez = resultado_soma_vezes_dez % 11

        segundo_digito_cpf = modulo_soma_vezes_dez if modulo_soma_vezes_dez <= 9 else 0

        print(f"O SEGUNDO DIGITO DO CPF É {segundo_digito_cpf}")

        numeros_do_cpf.append(segundo_digito_cpf)

        contador = 1
        for numeros in numeros_do_cpf:
            cpf_final += str(numeros)
            if len(cpf_final.replace('.', '')) == 9:
                cpf_final += '-'
                contador = 0
                continue
            if contador == 3:
                cpf_final += '.'
                contador = 0
            contador += 1

        os.system("cls")
        print(f"SEU CPF É {cpf_final}")

        # Zerando as variáveis
        cpf_final = ''
        numeros_do_cpf = []
        resultado_multiplicacao = []
        soma_total_de_todos_os_numeros_multiplicados = []