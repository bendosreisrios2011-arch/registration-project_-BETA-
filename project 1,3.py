#PROJETO 1.3

import winsound
from datetime import date

meses = {
    # PT
    "janeiro": 1, "fevereiro": 2, "março": 3, "marco": 3, "abril": 4, "maio": 5,
    "junho": 6, "julho": 7, "agosto": 8, "setembro": 9, "outubro": 10,
    "novembro": 11, "dezembro": 12,

    # EN
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11,
    "december": 12
}

hoje = date.today()

sexo_masculino = "masculino", "m", "macho", "homem", "homi", "man"

sexo_feminino = "feminino", "f", "fêmea", "mulher", "muie", "muié", "girl"
print("-" * 80)

cadastros = []

for i in range(3):

    nome = input("Nome completo?").title().split()[0]

    while True:
        sexo = input("Sexo? ").strip().lower()

        if sexo == "":
            print("Sexo inválido. Digite novamente.")
            continue
        sexo_base = sexo.split()[0]

        if sexo_base in sexo_masculino or sexo_base in sexo_feminino:
           break
        else:
            print("Sexo invalido. Digite novamente.")

    cidade = input("Cidade de residência?").strip()

    ano_nas = int(input("Digite o seu ano de nascimento").strip())
    while True:
        mes_txt = input("Digite o seu mês de nascimento").strip().lower()

        if mes_txt.isdigit():
            mes_nas = int(mes_txt)
            if 1 <= mes_nas <= 12:
             break
            print("Mês inválido. Digite um mês real.")
            continue
