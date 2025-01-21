# Em andamento, quase finalizado
import os
while True:
    cpf_user_converted = []
    print("O CPF deve conter apenas 11 dígitos numéricos.")
    user_name = input("Informe seu nome, por gentileza: ").capitalize().strip()
    cpf_informed = input("Informe o cpf: ").replace('.', '').replace('-', '')

    if user_name.isalpha():
        pass
    else:
        print("Insira um nome válido, por gentileza.")
        continue

    if cpf_informed.isdigit() and len(cpf_informed) == 11:
        for number in cpf_informed:
            cpf_user_converted.append(int(number))

 
        def first_number_calculation(cpf_user_converted):
            # Multiplicando os 9 primeiros números do cpf começando por 10 até 2
            # Após a multiplicação é feito a soma de todos eles
            multiplied_digit = [number * cpf_user_converted[index] for index, number in enumerate(range(10, 1, -1))]

            total_added = 0
            for number in multiplied_digit:
                total_added += number

            # Multiplicando o resultado por 10 e depois pegando o resto da divisão
            # por 11

            multiplying_by_ten = total_added * 10
            module = multiplying_by_ten % 11

            first_number = 0 if module > 9 else module

            return first_number
            
        def second_number_calculation(cpf_user_converted):
            # Multiplicando os 9 primeiros números do cpf começando por 11 até 2
            # Após a multiplicação é feito a soma de todos eles
            multiplied_digit = [number * cpf_user_converted[index] for index, number in enumerate(range(11, 1, -1))]

            total_added = 0
            for number in multiplied_digit:
                total_added += number

            # Multiplicando o resultado por 10 e depois pegando o resto da divisão
            # por 11

            multiplying_by_ten = total_added * 10
            module = multiplying_by_ten % 11

            second_number = 0 if module > 9 else module

            return second_number
        
        def validating_cpf(cpf_user_converted):
            first_cpf_number = first_number_calculation(cpf_user_converted)
            second_cpf_number = second_number_calculation(cpf_user_converted)

            if first_cpf_number == cpf_user_converted[-2] and second_cpf_number == cpf_user_converted[-1]:
                return True
            else:
                return False

        if validating_cpf(cpf_user_converted) == True:
            os.system("cls")
            print("O CPF informado é válido!")
            final_cpf = ''
            counter = 1
            for number in cpf_informed:
                final_cpf += number
                if counter == 9:
                    final_cpf += '-'
                    counter = 1
                    continue
                if counter % 3 == 0:
                    final_cpf += '.'
                counter += 1
            os.system("cls")
            print(f"Nome do portador: {user_name}")
            print(f"CPF: {final_cpf}")
        else:
            print("CPF é inválido. Verifique os números digitados para ver se não houve algum digito inserido errado.")

    else:
        print("O CPF deve conter apenas 11 dígitos numéricos.")