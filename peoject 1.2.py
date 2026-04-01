import winsound
from datetime import date

hoje = date.today()

sexo_masculino = "masculino", "m", "macho", "homem", "homi", "man"

sexo_feminino = "feminino", "f", "fêmea", "mulher", "muie", "muié", "girl"
print("-" * 80)

nomes = []
cidades = []
anos_nas = []
meses_nas = []
dias_nas = []


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

    mes_nas = int(input("Digite o seu mês de nascimento").strip())

    dia_nas = int(input("Digite o dia de nascimento").strip())

    idade = hoje.year - ano_nas - ((hoje.month, hoje.day) < (mes_nas, dia_nas))

    if idade < 18:
        print("Infelizmente, esse site é +18.")
        print("(ACESSO NEGADO)")
    nomes.append(nome)
    cidades.append(cidade)
    anos_nas.append(ano_nas)
    meses_nas.append(mes_nas)
    dias_nas.append(dia_nas)



    if sexo_base in sexo_masculino:
        tratamento = "senhor"
    else:
        tratamento = "senhora"

    print("Perfeito, o seu cadastro foi finalizado com sucesso, {} {}.".format(tratamento, nome))
print()
print("-" * 30)

resposta = input("Deseja ver o conteúdo dos cadastros? ").strip().lower()

if resposta in ["sim", "s", "positivo", "pode ser"]:
    print("Nomes:{}".format(nomes))
    print()
    print("Cidades:{}".format(cidades))
    print()
    print("Certo, conversa encerrada")

else:
    (print("Certo, conversa encerrada"))
print()
print("-" * 30)
winsound.PlaySound("mp3xx1.wav", winsound.SND_FILENAME)
winsound.PlaySound("mp3xx1.wav", winsound.SND_FILENAME)