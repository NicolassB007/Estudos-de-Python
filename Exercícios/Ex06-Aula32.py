hora = input("Informe a hora: ")
hora_float = float(hora)

if (hora_float >= 0) and (hora_float <= 11):
    print("Bom dia!")
elif (hora_float >= 12) and (hora_float <= 17):
    print("Boa tarde!")
elif (hora_float >= 18) and (hora_float <= 23):
    print("Boa noite!")
else:
    print("Hora inválida")