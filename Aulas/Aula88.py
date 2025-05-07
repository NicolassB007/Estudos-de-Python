# Try, except, else e finally
# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    print("Linha 1"[1000])
    c = a / b
    print("Linha 2")
except ZeroDivisionError:
    print("Dividiu por 0")
except NameError:
    print("Nome b não está definido")
except (TypeError, IndexError) as error:
    print("TypeError + IndexError")
    print("MSG: ", error)
    print("NOME: ", error.__class__.__name__)
except Exception: # Exception é maior classe de Erro, não tem NINGUÉM acima dela
    print("Erro desconhecido")

print("CONTINUAR")