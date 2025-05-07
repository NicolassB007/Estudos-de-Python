# Try, except, else e finally

try:
    print("ABRIR ARQUIVO")
    # 8/0
except ZeroDivisionError:
    print("DIVIDIU POR 0")
else:
    print("Não teve erro")
finally:
    print("FECHAR ARQUIVO")
    