primeiro_valor = input("Primeiro valor: ")
segundo_valor = input("Segundo valor: ")

int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)

if int_primeiro_valor > int_segundo_valor:
    print(f"{primeiro_valor=} é maior que o {segundo_valor=}")
else:
    print(f"{segundo_valor=} é maior que o {primeiro_valor=}")