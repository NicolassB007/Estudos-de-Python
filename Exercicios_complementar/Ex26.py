import random

numbers_cpf_list = []

multiplication_result = []

while True:
    def create_cpf():
        for numeros in range(0, 9):
            numbers = random.randint(0, 9)
            numbers_cpf_list.append(numbers)
        return numbers_cpf_list
    
    def first_number(cpf):
        multiplication = 1
        index = 0
        for numeros in range(10, 1, -1):
            multiplication = cpf[index] * numeros
            multiplication_result.append(multiplication)
            index += 1
        return multiplication_result
    
    break