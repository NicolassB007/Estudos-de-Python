import math
def number_root(number):
    def calculation_root():
        return math.sqrt(number)
    return calculation_root

final_result = number_root(11)
print(f"{final_result():.2f}")