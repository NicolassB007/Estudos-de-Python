# Exercício - Sistema de perguntas e respostas
# Feito com auxilio do professor do curso online UDEMY

perguntas = [
    {
        "Pergunta": "Quanto é 2 + 2?",
        "Opções": ['1', '2', '3', '4'],
        "Resposta": '4'
    },
    {
        "Pergunta": "Quanto é 5 * 5",
        "Opções": ["25", "12", "22", "24"],
        "Resposta": "25", 
    },
    {
        "Pergunta": "Quanto é 10 / 2",
        "Opções": ["6", "3.5", "2", "5"],
        "Resposta": '5',  
    }
]

qtd_acertos = 0
for pergunta in perguntas:
    print("Pergunta: ", pergunta["Pergunta"])

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f"{i}) {opcao}")

    esc_user = input("Informe uma opção: ")

    qtd_options = len(opcoes)
    acerto = False
    esc_user_int = 0
    esc_user_valid = None

    if esc_user.isdigit():
        esc_user_int = int(esc_user)
        esc_user_valid = True

    if esc_user_valid is True:
        if esc_user_int >= 0 and esc_user_int < qtd_options:
            if opcoes[esc_user_int] == pergunta["Resposta"]:
                acerto = True
                qtd_acertos += 1
        
    if acerto:
        print("Parabéns, você acertou!")
    else:
        print("Que pena, você errou!")

    print('\n')
        
print(f"Você teve {qtd_acertos} acertos!")
print(f"ACERTOS {qtd_acertos} de {len(perguntas)}")