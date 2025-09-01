#!/usr/bin/env python3
import argparse
import random

art = """\033[94m
██████╗  ██████╗  ██████╗ ██████╗ ███████╗███╗   ██╗
██╔══██╗██╔═══██╗██╔════╝██╔════╝ ██╔════╝████╗  ██║
██║  ██║██║   ██║██║     ██║  ███╗█████╗  ██╔██╗ ██║
██║  ██║██║   ██║██║     ██║   ██║██╔══╝  ██║╚██╗██║
██████╔╝╚██████╔╝╚██████╗╚██████╔╝███████╗██║ ╚████║
╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝
\033[0m """
print(art)

def generate_cpf(state_option, mask=True):
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

    cpf_base = [int(d) for d in prefix] + [random.randint(0, 9) for _ in range(7)]

    def calculate_digit(digits, weights):
        total = sum(d * w for d, w in zip(digits, weights))
        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder

    first_digit = calculate_digit(cpf_base, range(10, 1, -1))
    cpf_base.append(first_digit)
    second_digit = calculate_digit(cpf_base, range(11, 1, -1))
    cpf_base.append(second_digit)

    if mask:
        return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf_base)
    else:
        return ''.join(map(str, cpf_base))

def generate_cnpj(mask=True):
    base = [random.randint(0, 9) for _ in range(8)] + [0, 0, 0, 1]

    def calculate_digit(digits, weights):
        total = sum(d * w for d, w in zip(digits, weights))
        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder

    first_weights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    second_weights = [6] + first_weights

    first_digit = calculate_digit(base, first_weights)
    second_digit = calculate_digit(base + [first_digit], second_weights)

    cnpj = base + [first_digit, second_digit]

    if mask:
        return "%s%s.%s%s%s.%s%s%s/%s%s%s%s-%s%s" % tuple(cnpj)
    else:
        return ''.join(map(str, cnpj))

def generate_renavam(mask=True):
    renavam = [random.randint(0, 9) for _ in range(10)]

    weights = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    total = sum(d * w for d, w in zip(renavam, weights))
    remainder = total % 11
    dv = 0 if remainder == 0 or remainder == 1 else 11 - remainder

    renavam.append(dv)

    if mask:
        return "%s%s%s.%s%s%s.%s%s%s-%s" % tuple(renavam)
    else:
        return ''.join(map(str, renavam))

def main():
    parser = argparse.ArgumentParser(description="Gerador de documentos aleatórios.")
    parser.add_argument("-d", "--documento", type=str, required=True,
                        choices=["cpf", "cnpj", "renavam"],
                        help="Tipo de documento a ser gerado: 'cpf', 'cnpj' ou 'renavam'.")
    parser.add_argument("-q", "--quantidade", type=int, default=1,
                        help="Quantidade de documentos a serem gerados.")
    parser.add_argument("-e", "--estado", type=str,
                        choices=["SP", "BA", "PR", "Mistos"],
                        help="Estado para geração de CPF (opcional, apenas para 'cpf').")
    parser.add_argument("-m", "--mascara", action="store_true",
                        help="Adiciona máscara ao documento gerado.")
    parser.add_argument("-o", "--output", type=str,
                        help="Nome do arquivo de saída para salvar os documentos.")

    args = parser.parse_args()

    if args.documento == "cpf" and not args.estado:
        args.estado = "Mistos"

    documentos = []

    if args.documento == "cpf":
        documentos = [generate_cpf(args.estado, mask=args.mascara) for _ in range(args.quantidade)]
    elif args.documento == "cnpj":
        documentos = [generate_cnpj(mask=args.mascara) for _ in range(args.quantidade)]
    elif args.documento == "renavam":
        documentos = [generate_renavam(mask=args.mascara) for _ in range(args.quantidade)]

    if args.output:
        with open(args.output, "w") as file:
            for doc in documentos:
                file.write(doc + "\n")
        print(f"{len(documentos)} documentos gerados e salvos em '{args.output}'.")
    else:
        print("Documentos gerados:")
        for doc in documentos:
            print(doc)

if __name__ == "__main__":
    main()
