#----------------------------------#
from time import sleep as slp
from subprocess import run
import json
import os
import requests
#----------------------------------#
def banner():
    data = """
    \033[35m ▒█████   █    ██ ▄▄▄█████▓▓█████  ██▀███       
    \033[35m▒██▒  ██▒ ██  ▓██▒▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒     
    \033[35m▒██░  ██▒▓██  ▒██░▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒     
    \033[35m▒██   ██░▓▓█  ░██░░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄       
    \033[35m░ ████▓▒░▒▒█████▓   ▒██▒ ░ ░▒████▒░██▓ ▒██▒         \033[1;37m|     \033[1;35mLink: \033[1;4;34mgithub.com/gokuzinn/OuterHeaven\033[0m
    \033[35m░ ▒░▒░▒░ ░▒▓▒ ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░         \033[1;37m|     \033[1;35mAuthor \033[1;34mRetr0\033[0m
    \033[35m  ░ ▒ ▒░ ░░▒░ ░ ░     ░     ░ ░  ░  ░▒ ░ ▒░         \033[1;37m|     \033[1;35mDescription: \033[1;34mUse com sabedoria...\033[0m
    \033[35m░ ░ ░ ▒   ░░░ ░ ░   ░         ░     ░░   ░          \033[1;37m|     \033[1;35mProject: \033[1;34mOuterHeaven\033[0m
    \033[35m    ░ ░     ░                 ░  ░   ░              \033[1;37m|     \033[1;35mScripter: \033[1;34mDreexShiryu1\033[0m
                                                    
    \033[35m ██░ ██ ▓█████ ▄▄▄    ██▒   █▓▓█████  ███▄    █ 
    \033[35m▓██░ ██▒▓█   ▀▒████▄ ▓██░   █▒▓█   ▀  ██ ▀█   █ 
    \033[35m▒██▀▀██░▒███  ▒██  ▀█▄▓██  █▒░▒███   ▓██  ▀█ ██▒
    \033[35m░▓█ ░██ ▒▓█  ▄░██▄▄▄▄██▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒
    \033[35m░▓█▒░██▓░▒████▒▓█   ▓██▒▒▀█░  ░▒████▒▒██░   ▓██░
    \033[35m ▒ ░░▒░▒░░ ▒░ ░▒▒   ▓▒█░░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒ 
    \033[35m ▒ ░▒░ ░ ░ ░  ░ ▒   ▒▒ ░░ ░░   ░ ░  ░░ ░░   ░ ▒░
    \033[35m ░  ░░ ░   ░    ░   ▒     ░░     ░      ░   ░ ░ 
    \033[35m ░  ░  ░   ░  ░     ░  ░   ░     ░  ░         ░ 
                              ░
    """
    return print(data)

def list_help():
    data = """
    \033[35mTerminal Commands           Description\033[0m
    \033[1;37m==================          =============\033[0m

    help                        Aparece os comandos da terminal
    ip                          Aparece seu IP interno e externo
    search                      Faz pesquisa dos módulos e scripts
    use                         Usa o módulo
    set                         Seleciona uma opção
    """
    return print(data)

#----------------------------------#
print("\033[1;34mProcess loading...\033[0m")
slp(3)
run("clear",shell=True)
banner()
dir = os.path.dirname(os.path.abspath(__file__))
close = False
while not close:
    cmd = input("\033[4;35m\x6f\x68\x31\033[0m > ")
    if cmd == "help":
        print("="*40,"\n\033[1;34m[-]\033[0m\texec : %s\n"%(cmd))
        slp(1)
        list_help()
    elif cmd == "exit":
        close = True
        print("="*40,"\n\033[1;34m[-]\033[0m\texec : %s\n"%(cmd))
        slp(1)
    elif cmd == "banner":
        slp(1)
        banner()
    else:
        print("="*40,"\n\033[1;34m[-]\033[0m\texec : %s\n"%(cmd))
        slp(1)
        run(cmd,shell=True)
#----------------------------------#
