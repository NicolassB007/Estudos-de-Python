import os
student_information = {}
while True:
    student_name = input("Informe o nome do aluno: ").capitalize()
    age_student = input("Informe a idade do aluno: ")


    student_name_valid = None

    if (student_name.isalpha()):
        student_name_valid = True
    
    if student_name_valid is None:
        os.system("cls")
        print("O nome do aluno informado é inválido!")
        print("Verifique o nome e informe novamente por gentileza")
        continue

    while True:
        age_student_valid = None
        age_int_student = 0

        try:
            age_int_student = int(age_student)
            if age_int_student >= 0:
                age_int_student = int(age_student)
                age_student_valid = True
                break
        except ValueError:
            age_student_valid = None

    if "nome" not in student_information:
        student_information["nome"] = [student_name]
    else:
        student_information["nome"].append(student_name)

    if "idade" not in student_information:
        student_information["idade"] = [age_int_student]
    else:
        student_information["idade"].append(age_int_student)

    esc = input("Você quer informar mais algum nome? (s/n): ").lower()
    esc_valid = None

    if (esc.startswith("s")):
        os.system("cls")
        continue
    else:
        break

print("ALUNOS: ")

for name, age in student_information.items():
    print(name, age)
