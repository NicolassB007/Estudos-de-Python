# Operadores lógicos
# and (e) or (ou) not (nao)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso a expressão inteira 
# serao avaliadas naquele valor
# São considerados falsy (que vc já viu) 
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Digite a senha: ")

senha_permitida = '123456'
if (entrada == 'E' and senha_digitada == senha_permitida):
    print("Entrar")
else: 
    print("Sair")

# Avaliação de curto circuito
print(True and False and True)