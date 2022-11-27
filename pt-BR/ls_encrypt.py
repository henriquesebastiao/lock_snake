# Importando dependências
import os
from cryptography.fernet import Fernet

# Definindo funções
def imprime_logo():
    print()

    print("\033[0;34m     dBP    dBBBBP dBBBP  dBP dBP   \033[m"+"\033[0;33m.dBBBBP   dBBBBb   dBBb     dBP dBP dBBBBBP\033[m")
    print("\033[0;34m    dBp    dB'.BP dBP    dBP.d8P    \033[m"+"\033[0;33mBP       dBP dBP  dBPBB    dBP.d8P dBB\033[m")
    print("\033[0;34m   dBP    dB'.BP dBP    dBBBBP'     \033[m"+"\033[0;33m`BBBBb  dBP dBP  dBP BB   dBBBBP' dBBBBP\033[m")
    print("\033[0;34m  dBP    dB'.BP dBP    dBP BB          \033[m"+"\033[0;33mdBP dBP dBP  dBP  BB  dBP BB  dBP\033[m")
    print("\033[0;34m dBBBBP dBBBBP dBBBBP dBP dB'     \033[m"+"\033[0;33mdBBBBP' dBP dBP  dBBBBBBB dBP dB' dBBBBBP\033[m")

    print()
# Esta funcao não só pode parecer estúpida, como é. Mas é apenas para deixar claro onde haverá uma quebra de linha
def quebraLinha():
    print()

#Imprime o logo do Lock Snake
imprime_logo()

# Imprime informações sobre o desenvolvedor
print("Lock Snake - Versão 0.1")
print("Desenvolvido por: Henrique Sebastião")
print("https://github.com/henriquesebastiao")
quebraLinha()

operacao = 0
operacoes_possiveis = [1, 2]

while operacao not in operacoes_possiveis:
    print("O que você deseja fazer hoje?")
    print("1 - Criptografar arquivos")
    print("2 - Descriptografar arquivos")
    quebraLinha()

    operacao = int(input("lock@snake:~$ "))
    
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
    print("Para isso preciso que me informe algumas informações")
    quebraLinha()
    
    # Solicitando o caminho do arquivo
    print("Primeiro informe o caminho do diretório que contém os arquivos para criptografar")
    print("Exemplo: C:"+"\u005c"+"Users"+"\u005c"+"usuario_nome"+"\u005c"+"Documentos"+"\u005c"+"Arquivos")
    quebraLinha()
    diretorio_criptografar = input("lock@snake:~$ ")
    print()

    # Pede para o usuário o caminho do diretório no qual deseja salvar a chave para descriptografia dos arquivos
    # Muda para o diretório em que ficará a chave
    print("Informe o caminho do diretório no qual deseja salvar a chave para descriptografia dos arquivos: ")
    print("Exemplo: C:"+"\u005c"+"Users"+"\u005c"+"usuario_nome"+"\u005c"+"Documentos"+"\u005c"+"Chaves")
    quebraLinha()
    diretorio_chave = input("lock@snake:~$ ")
    
    # Solicitando ao usuário se ele realmenter quer continuar
    quebraLinha()
    print("\033[0;31mAPÓS CRIPTOGRAFAR OS ARQUIVOS, ELES NÃO PODERÃO SER DESCRIPTOGRAFADOS SEM A CHAVE!\033[m")
    print(f"A chave será salva no diretório {diretorio_chave}")
    quebraLinha()
    CONFIRMACAO = input("Você deseja continuar? [s/n]: ")
    
    if CONFIRMACAO == "s" or CONFIRMACAO == "S":
        os.chdir(diretorio_chave)
        files = []

        # Gera e salva a chave de descriptografia
        key = Fernet.generate_key()
        with open("chave.key", "wb") as chave:
            chave.write(key)

        # Muda para o diretório dos arquivos que seram criptografados
        os.chdir(diretorio_criptografar)

        for file in os.listdir():
            if file == "ls_encrypt.py" or file == "chave.key":
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
        
        quebraLinha()
        print("\033[0;32mArquivos criptografados com sucesso!\033[m")
    else:
        print("\033[0;33mOperação cancelada!0\033[m")