SALDO_CLIENTE = 500.00
print(f"SALDO ATUAL = R${SALDO_CLIENTE:.2f}")
cheque = input("Informe o valor do cheque: ")

int_cheque = 0
valor_valido = None

try:
    int_cheque = float(cheque)
    valor_valido = True
except:
    valor_valido = None
if valor_valido is True:
    novo_saldo = SALDO_CLIENTE + int_cheque
    print(f"Seu saldo após a entrada do cheque é de R${novo_saldo:.2f}")
else:
    print("Cheque inválido!")