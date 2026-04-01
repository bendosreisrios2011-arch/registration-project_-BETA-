#PROJETO 1.0


import winsound
nomes_femininos = [
   "ana","maria","julia","juliana","mariana","beatriz","bia","carla","carolina",
   "camila","gabriela","luana","larissa","leticia","renata","raquel","patricia",
   "paula","fernanda","flavia","daniela","aline","alice","amanda","bruna",
   "bianca","barbara","cintia","clara","cristina","debora","denise","elaine",
   "elisa","emanuelle","ester","fabiana","fatima","giovana","helena","isabela",
   "isadora","joana","karina","laura","luciana","marcela","michelle","natalia",
   "nicole","olivia","priscila","rafaela","regina","sabrina","samara","silvia",
   "simone","sonia","tatiana","tania","vanessa","veronica","vitoria","yasmin",
   "yara","adriana","alexandra","andrea","angelica","antonia","celia","dalila",
   "edna","irene","joelma","karen","leila","maisa","noemi","rosana","suely",
   "tereza","valeria","sara","antonieta","mirela","emilia","luísa","luisa",


    # EUA / internacionais
    "emma","ava","sophia","isabella","mia","amelia","harper","evelyn","abigail",
    "emily","ella","elizabeth","luna","sofia","avery","scarlett","grace","chloe",
    "victoria","riley","aria","lily","aubrey","zoey","penelope","layla","nora",
    "hazel","madison","savannah","brooklyn","bella","claire","skylar","lucy",
    "paisley","everly","anna","caroline","nova","genesis","emilia","kennedy",
    "helga","nadine","selene","ingrid","freya","astrid"


    # Cantoras internacionais
    "madonna","beyonce","rihanna","adele","taylor","selena","ariana","katy",
    "lady","billie","dua","shakira","celine","whitney","mariah","britney",
    "pink","sia","lorde","alicia","janet","cher","lana","kylie","demi",
    "halsey","ellie","fiona","norah","amy","nina","jessie","toni","ciara",
    "meghan","sza","doja","cardi","nicki","melanie","grimes","bjork","aurora","miley",
    "pink","lady","kesha","madison","miley",

    # Cantoras brasileiras
    "madonna", "beyonce", "rihanna", "adele", "taylor", "selena", "ariana", "katy",
    "billie", "dua", "shakira", "celine", "whitney", "mariah", "britney", "sia",
    "alicia", "janet", "cher", "lana", "kylie", "demi", "halsey", "fiona", "norah",
    "amy", "nina", "jessie", "toni", "ciara", "meghan", "sza", "doja", "cardi", "nicki",
    "melanie", "grimes", "bjork",
    "ivete", "claudia", "elba", "gal", "rita", "marisa", "sandy", "wanessa", "ludmilla",
    "anitta","clarice","odete","ofelia","matilde",
    "margarida","eunice"
 
    # Nomes adicionados por você
    "flor","charlene","zuleide","leda","luan"]

print("-" * 80)

nomes = []
cidades = []

for i in range(3):
    nome = input("Nome? ").strip()
    print()
    cidade = input("Cidade? ").strip()
    print()
    nomes.append(nome)
    cidades.append(cidade)
    if nome.split()[0].lower() in nomes_femininos:
        tratamento = "senhora"
    else:
        tratamento = "senhor"

    print("Perfeito, o seu cadastro foi finalizado com sucesso, {} {}.".format(tratamento, nome))
print()
print("-" * 60)

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
