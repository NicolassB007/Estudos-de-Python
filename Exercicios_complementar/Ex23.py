def exponent_of_power(exponent_number):
    def number_power(base_number):
        return base_number ** exponent_number
    return number_power

square_result = exponent_of_power(2)
cubic_result = exponent_of_power(3)

print(f"RESULTADO DO NÚMERO AO QUADRADO -> {square_result(4)}")
print(f"RESULTADO DO NÚMERO AO CUBO -> {cubic_result(4)}")