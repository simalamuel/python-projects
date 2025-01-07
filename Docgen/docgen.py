import random

art = """\033[94m
██████╗  ██████╗  ██████╗ ██████╗ ███████╗███╗   ██╗
██╔══██╗██╔═══██╗██╔════╝██╔════╝ ██╔════╝████╗  ██║
██║  ██║██║   ██║██║     ██║  ███╗█████╗  ██╔██╗ ██║
██║  ██║██║   ██║██║     ██║   ██║██╔══╝  ██║╚██╗██║
██████╔╝╚██████╔╝╚██████╗╚██████╔╝███████╗██║ ╚████║
╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
\033[0m """
print(art)

def generate_cpf(state_option):
    state_prefixes = {
        "SP": ["11", "12", "13", "14", "15", "16", "17", "18", "19"],
        "BA": ["71", "73", "74", "75", "77", "78"],
        "PR": ["41", "42", "43", "44", "45", "46", "47"],
    }

    if state_option in state_prefixes:
        prefix = random.choice(state_prefixes[state_option])
    elif state_option == "Mistos":
        prefix = random.choice(state_prefixes["SP"] + state_prefixes["BA"] + state_prefixes["PR"])
    else:
        return 0

    cpf = [random.randint(0, 9) for _ in range(9)]

    cpf = [int(digit) for digit in prefix] + cpf[2:]

    def calculate_digit(cpf):
        weight = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        total = sum(cpf[i] * weight[i] for i in range(9))
        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder

    first_digit = calculate_digit(cpf)
    cpf.append(first_digit)
    second_digit = calculate_digit(cpf)
    cpf.append(second_digit)

    if len(cpf) == 11:
        return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)
    else:
        return 0

def generate_cpf_sem_mascara(state_option):
    state_prefixes = {
        "SP": ["11", "12", "13", "14", "15", "16", "17", "18", "19"],
        "BA": ["71", "73", "74", "75", "77", "78"],
        "PR": ["41", "42", "43", "44", "45", "46", "47"],
    }
    if state_option in state_prefixes:
        prefix = random.choice(state_prefixes[state_option])
    elif state_option == "Mistos":
        prefix = random.choice(state_prefixes["SP"] + state_prefixes["BA"] + state_prefixes["PR"])
    else:
        return 0
    
    cpf = [random.randint(0, 9) for _ in range(9)]

    cpf = [int(digit) for digit in prefix] + cpf[2:]

    def calculate_digit(cpf):
        weight = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        total = sum(cpf[i] * weight[i] for i in range(9))
        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder

    first_digit = calculate_digit(cpf)
    cpf.append(first_digit)
    second_digit = calculate_digit(cpf)
    cpf.append(second_digit)

    if len(cpf) == 11:
        return ''.join(map(str, cpf))
    else:
        return 0

def generate_cnpj():
    def calculate_special_digit(l):
        digit = 0
        for i, v in enumerate(l):
            digit += v * (i % 8 + 2)
        digit = 11 - digit % 11
        return digit if digit < 10 else 0

    cnpj = [1, 0, 0, 0] + [random.randint(0, 9) for x in range(8)]

    for _ in range(2):
        cnpj = [calculate_special_digit(cnpj)] + cnpj

    return '%s%s.%s%s%s.%s%s%s/%s%s%s%s-%s%s' % tuple(cnpj[::-1])

def generate_cnpj_numeros():
    def calculate_special_digit(l):
        digit = 0
        for i, v in enumerate(l):
            digit += v * (i % 8 + 2)
        digit = 11 - digit % 11
        return digit if digit < 10 else 0

    cnpj_numeros = [1, 0, 0, 0] + [random.randint(0, 9) for x in range(8)]

    for _ in range(2):
        cnpj_numeros = [calculate_special_digit(cnpj_numeros)] + cnpj_numeros

    return '%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % tuple(cnpj_numeros[::-1])

def generate_renavam():
    renavam = [random.randint(0, 9) for _ in range(10)]
    weights = [2, 3, 4, 5, 6, 7, 8, 9]
    total = sum(renavam[i] * weights[i % len(weights)] for i in range(8))
    remainder = total % 11
    check_digit = 11 - remainder if remainder >= 2 else 0
    renavam.append(check_digit)
    return ''.join(map(str, renavam))

def main():
    print("Escolha o tipo de documento para gerar:")
    print("1 - CPF")
    print("2 - CPF (sem máscara)")
    print("3 - CNPJ")
    print("4 - CNPJ (sem máscara)")
    print("5 - RENAVAM")

    escolha = input("Digite o número correspondente à sua escolha: ")

    quantidade = int(input("Quantos documentos você deseja gerar? "))

    if escolha == "1" or escolha == "2":
        print("Escolha o estado ou opção 'Mistos' para gerar CPFs:")
        print("1 - Paraná (PR)")
        print("2 - Bahia (BA)")
        print("3 - São Paulo (SP)")
        print("4 - Mistos (Aleatório entre SP, BA e PR)")

        estado = input("Digite o número correspondente à sua escolha: ")

        if estado == "1":
            state_option = "PR"
        elif estado == "2":
            state_option = "BA"
        elif estado == "3":
            state_option = "SP"
        elif estado == "4":
            state_option = "Mistos"
        else:
            print("Opção inválida. Tente novamente.")
            return

        if escolha == "1":
            documentos = [generate_cpf(state_option) for _ in range(quantidade)]
        elif escolha == "2":
            documentos = [generate_cpf_sem_mascara(state_option) for _ in range(quantidade)]

    elif escolha == "3":
        documentos = [generate_cnpj() for _ in range(quantidade)]
    elif escolha == "4":
        documentos = [generate_cnpj_numeros() for _ in range(quantidade)]
    elif escolha == "5":
        documentos = [generate_renavam() for _ in range(quantidade)]
    else:
        print("Opção inválida. Tente novamente.")
        return

    print("1 - Sim")
    print("2 - Não")
    salvar_arquivo = input("Deseja salvar os documentos em um arquivo: ").strip()

    arquivo = input("Qual o nome do arquivo: ")

    if salvar_arquivo == "1":
        filename = f"{arquivo}.txt"
        with open(filename, "w") as file:
            for doc in documentos:
                file.write(doc + "\n")
        print(f"{quantidade} documentos gerados e salvos em {filename}")
    elif salvar_arquivo == "2":
        for doc in documentos:
            print(doc)
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
