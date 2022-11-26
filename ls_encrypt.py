# Importando dependências
import os
from cryptography.fernet import Fernet

# Definindo funções
def imprime_logo():
    logo = open("logo.txt")
    print()
    print(logo.read())
    logo.close()
    print()
# Esta funcao não só pode parecer estúpida, como é. Mas é apenas para deixar claro onde haverá uma quebra de linha
def quebraLinha():
    print()
# Função para entradas do usuário
def terminal():
    input("lock@snake:~$ ")

#Imprime o logo do Lock Snake
imprime_logo()

# Imprime informações sobre o desenvolvedor
print("Desenvolvedor: Henrique Sebastião.")
print("https://github.com/henriquesebastiao")
quebraLinha()

operacao = 0
operacoes_possiveis = [1, 2]

while operacao not in operacoes_possiveis:
    print("O que você deseja fazer hoje?")
    print("1 - Criptografar arquivos")
    print("2 - Descriptografar arquivos")
    quebraLinha()

    operacao = int(terminal())
    
    if operacao not in operacoes_possiveis:
        quebraLinha()
        print("Essa opção não existe :|")
        print("Por favor, tente novamente!")
        quebraLinha()
    else:
        quebraLinha()
        continue

if operacao == 1:
    print("Então quer dizer que você quer tornar alguns arquivos inacessíveis...")
    print("Para isso preciso que me informe algumas informações.")
    quebraLinha()
    
    # -> CONTINUAR AQUI!
    
    # Pede ao usuário o caminho diretório em que estão os arquivos a serem criptografados
    diretorio_criptografar = terminal()

    # Pede para o usuário o caminho do diretório no qual deseja salvar a chave para descriptografia dos arquivos
    # Muda para o diretório em que ficará a chave
    os.chdir(input("Informe o diretório no qual deseja salvar a chave para descriptografia -> "))
    files = []

    # Gera e salva a chave de descriptografia
    key = fernet.generate_key()
    with open("chave.key", "wb") as chave:
        chave.write(key)

    # Muda para o diretório dos arquivos que seram criptografados
    os.chdir(diretorio_criptografar)

    for file in os.listdir():
        if file == "ls.py" or file == "chave.key":
            continue
        if os.path.isfile(file):
            files.append(file)

    # Começa a criptografar os arquivos
    for file in files:
        with open(file, "rb") as arquivo:
            conteudo = arquivo.read()
        conteudo_encrypted = Fernet(key).encrypt(conteudo)
        with open(file, 'wb') as arquivo:
            arquivo.write(conteudo_encrypted)