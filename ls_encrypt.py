import os
from cryptography.fernet import Fernet

def imprime_logo():
    logo = open("logo.txt")
    print()
    print(logo.read())
    print()

#Imprime o logo do Lock Snake
imprime_logo()

# Imprime informações sobre o desenvolvedor
print("Desenvolvedor: Henrique Sebastião.")
print("https://github.com/henriquesebastiao")
print()

operacao = 0

while operacao == 0 or operacao != 1 or operacao != 2:
    print("O que você deseja fazer hoje?")
    print("1 - Criptografar arquivos")
    print("2 - Descriptografar arquivos")
    print()

    operacao = int(input("lock@snake:~$ "))
    
    if operacao == 0 or operacao != 1 or operacao != 2:
        print()
        print("Essa opção não existe :|")
        print("Por favor, tente novamente!")
    else:
        continue

if operacao == 1:
    print("Então quer dizer que você quer tornar alguns arquivos inacessíveis...")
    print("Para isso preciso que me informe algumas informações.")
    
    # -> CONTINUAR AQUI!
    
    # Pede ao usuário o caminho diretório em que estão os arquivos a serem criptografados
    diretorio_criptografar = input("lock@snake:~$ ")

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