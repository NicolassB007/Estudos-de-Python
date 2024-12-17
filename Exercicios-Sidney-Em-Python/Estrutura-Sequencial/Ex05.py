saldo_cliente = input("Qual o seu saldo bancário: ")
parcelas = input("Quantas parcelas são: ")
valor_parcelas = input("Qual o valor de cada parcela: ")
parcelas_pagas = input("Quantas parcelas foram pagas: ")

float_saldo_cliente = float(saldo_cliente)
int_parcelas = int(parcelas)
int_parcelas_pagas = int(parcelas_pagas)
float_valor_parcelas = float(valor_parcelas)

parcelas_restantes = int_parcelas - int_parcelas_pagas

if (parcelas_restantes <= 0):
    print("Todas as parcelas foram pagas")
elif (int_parcelas_pagas == 0):
    total_pagar = int_parcelas * float_valor_parcelas
    saldo_final = float_saldo_cliente - total_pagar
    print(f"PARCELAS A PAGAR = {int_parcelas}")
    print(f"TOTAL A PAGAR = {total_pagar:.2f}")
    if (float_saldo_cliente < total_pagar):
        print("SALDO BANCÁRIO INSUFICIENTE")
        saldo_necessario = total_pagar - float_saldo_cliente
        print(f"SALDO NECESSÁRIO PARA PAGAR TODAS AS PARCELAS RESTANTES  = R${saldo_necessario:.2f}")
    else:
        print(f"SALDO FINAL = {saldo_final:.2f}")
else:
    total_pagar = parcelas_restantes * float_valor_parcelas
    saldo_final = float_saldo_cliente - total_pagar
    print(f"PARCELAS A PAGAR = {parcelas_restantes}")
    print(f"TOTAL A PAGAR = {total_pagar:.2f}")
    if (float_saldo_cliente < total_pagar):
        print("SALDO BANCÁRIO INSUFICIENTE")
        saldo_necessario = total_pagar - float_saldo_cliente
        print(f"SALDO NECESSÁRIO PARA PAGAR TODAS AS PARCELAS RESTANTES = R${saldo_necessario:.2f}")
    else:
        print(f"SALDO FINAL = {saldo_final:.2f}")