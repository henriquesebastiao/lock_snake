#!/bin/sh

if test -f .ascii; then
    cat .ascii
fi

VERMELHO='\033[0;31m'
AZUL='\033[0;34m'
VERDE='\033[0;32m'
BRANCO='\033[0m'

checkroot(){
    SAVE_LD_PRELOAD="$LD_PRELOAD"
    unset LD_PRELOAD
    if [ "$(id -u)" -ne 0 ]; then
        echo -e "${VERMELHO}You must be root user to run this script!\n${BRANCO}"
        exit 1
    fi
    LD_PRELOAD="$SAVE_LD_PRELOAD"
}

apt_based(){
    apt-get update
    apt-get install -y python3 python3-pip
    pip install -r requirements.txt
    if [ "$?" -ne 0 ]; then
        echo -e "${VERMELHO}An error occurred! It looks like apt-get doesn't work.\n${BRANCO}"
        exit 1
    fi
}

pacman_based(){
    pacman -Sy
    pacman -S python python-pip
    pip install -r requirements.txt
    if [ "$?" -ne 0 ]; then
        echo -e "${VERMELHO}An error occurred! It looks like pacman doesn't work.\n${BRANCO}"
        exit 1
    fi
}

# CONTINUAR AQUI ->

yum_based(){
    yum update -y
    yum install -y python3 python3-pip
    pip install -r requirements.txt
    if [ "$?" -ne 0 ]; then
        echo -e "${VERMELHO}Um erro ocorreu! Parece que o yum não funciona.\n${BRANCO}"
        exit 1
    fi
}

checkroot

KERNEL="$(uname -s | tr '[:upper:]' '[:lower:]')"
if [ "$KERNEL" = "linux" ]; then
    DISTRO="$(grep ^ID= /etc/os-release | cut -d= -f2 | tr '[:upper:]' '[:lower:]' | sed 's/\"//g')"

    case "$DISTRO" in

        "gentoo")
            emerge --sync
            emerge -av dev-lang/php dev-python/pip
            if [ "$?" -ne 0 ]; then
                printf "${VERMELHO}Um erro ocorreu! parece que o portage não funciona.\n${BRANCO}"
                exit 1
            fi
        ;;

        "debian" | "kali" | "ubuntu" | "linuxmint")
            apt_based
        ;;

        "arch" | "manjaro" | "arcolinux" | "garuda" | "artix")
            pacman_based
        ;;

        "fedora" | "centos")
            yum_based
        ;;

        *)
            printf "${VERMELHO}Não consegui detectar sua distribuição linux!\n${BRANCO}"
            printf "${AZUL}Esta ferramenta precisa do ${VERDE}python3${AZUL} e do ${VERDE}php${AZUL}."
            printf " instale você mesmo esses pacotes em seu sistema operacional.\n${BRANCO}"
            printf "${AZUL}Instale também as bibliotecas python necessárias via ${BRANCO}'${VERDE}pip install -r requirements.txt${BRANCO}'\n"
            exit 1
    esac

elif [ "$KERNEL" = "darwin" ]; then
    printf "${VERMELHO}Não é possível instalar no macOS!\n${BRANCO}"
    exit 1

else
    printf "${VERMELHO}Não é possível instalar no Windows!\n${BRANCO}"
    exit 1
fi

printf "${VERDE}Dependências instaladas com sucesso!\n${BRANCO}"
exit 0