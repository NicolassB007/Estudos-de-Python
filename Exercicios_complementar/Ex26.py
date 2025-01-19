import random
# Em andamento

while True: 
    numbers_cpf_list = []
    def create_cpf():
        for counter in range(0, 9):
            numbers = random.randint(0, 9)
            numbers_cpf_list.append(numbers)
        return numbers_cpf_list
    
    def first_number(cpf):

        def multiplication_numbers_in_cpf():
            list_numbers_multiplied = []
            index = 0
            for number in range(10, 1, -1):
                multiplied_result = numbers_cpf_list[index] * number
                list_numbers_multiplied.append(multiplied_result)
                index += 1
            return list_numbers_multiplied

        def calculate(): # Somando e divindo para ter o primeiro numero

            multiplied_numbers = multiplication_numbers_in_cpf()
            addition = 0

            for number in multiplied_numbers:
                addition += number
            
            addition_ten_times = addition * 10
            module_result_addition = addition_ten_times % 11

            result_first_number = module_result_addition if module_result_addition <= 9 else 0

            numbers_cpf_list.append(result_first_number)

            return result_first_number

        return calculate

    def second_number(cpf):
        def multiplying_numbers():
            list_numbers_multiplied = []
            index = 0
            for number in range(11, 1, -1):
                multiplied_result = numbers_cpf_list[index] * number
                list_numbers_multiplied.append(multiplied_result)
                index += 1

            return list_numbers_multiplied
        
        def second_calculate():
            multiplied_numbers = multiplying_numbers()
            addition = 0

            for number in multiplied_numbers:
                addition += number
            
            addition_ten_times = addition * 10
            module_result_addition = addition_ten_times % 11

            result_second_number = module_result_addition if module_result_addition <= 9 else 0

            numbers_cpf_list.append(second_number)

            return result_second_number
            
        return second_calculate



    cpf_created = create_cpf
    first_number_in_cpf = first_number(cpf_created)
    second_number_in_cpf = second_number(cpf_created)

    print(cpf_created())
    print(first_number_in_cpf())
    print(second_number_in_cpf())

    break