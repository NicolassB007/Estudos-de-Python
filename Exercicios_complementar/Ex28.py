import os
student_information = {}
while True:
    student_name = input("Informe o nome do aluno: ").capitalize()
    age_student = input("Informe a idade do aluno: ")
    note_student = input("Informe a nota do aluno: ")


    student_name_valid = None

    if (student_name.isalpha()):
        student_name_valid = True
    
    if student_name_valid is None:
        os.system("cls")
        print("O nome do aluno informado é inválido!")
        print("Verifique o nome e informe novamente por gentileza")
        continue

    while True:
        note_student_valid = None
        note_student_double = 0

        try:
            note_student_double = float(note_student)
            note_student_valid = True
            break
        except ValueError:
            age_student_valid = None

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

    if "nota" not in student_information:
        student_information["nota"] = [note_student_double]
    else:
        student_information["nota"].append(note_student_double)

    esc = input("Você quer informar mais algum nome? (s/n): ").lower()
    esc_valid = None

    if (esc.startswith("s")):
        os.system("cls")
        continue
    else:
        break

print("ALUNOS: ")

for name in student_information["nome"]:
    print(f"Nome: {name} -- ", end=' ')

print("\n")

for age in student_information["idade"]:
    print(f"Idade: {age} --", end=' ')

print("\n")

for note in student_information["nota"]:
    print(f"Nota: {note} -- ", end=' ')
