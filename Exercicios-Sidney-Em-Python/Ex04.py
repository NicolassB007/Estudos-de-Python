SALDO_CLIENTE = 500.00
print(f"SALDO ATUAL = R${SALDO_CLIENTE:.2f}")
cheque = input("Informe o valor do cheque: ")

int_cheque = float(cheque)

novo_saldo = SALDO_CLIENTE + int_cheque
print(f"Seu saldo após a entrada do cheque é de R${novo_saldo:.2f}")