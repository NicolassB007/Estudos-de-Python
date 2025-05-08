# raise - lançando exceções (erros)

# print(123)
# raise ValueError("Deu erro")
# print(123)

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError("Você está tentando dividir por 0")
    return True

def deve_ser_int_or_float(n):
    tipo_de_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f"{n} deve ser int ou float"
            f"{tipo_de_n} enviado"
        )


def divide(n, d):
    deve_ser_int_or_float(n)
    deve_ser_int_or_float(d)
    nao_aceito_zero(d)
    return n / d

print(divide(8, '0'))