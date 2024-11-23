from boosting import *
import httpx, random, time, datetime, json, os, hashlib
from keyauth import api
if os.name == 'nt':
    import ctypes
import hashlib
import sys
import os

# Clear the console screen
os.system('cls' if os.name == 'nt' else 'clear')

    
config = json.load(open("config.json", encoding="utf-8"))



def getinviteCode(invite_input):
    if "discord.gg" not in invite_input:
        return invite_input
    if "discord.gg" in invite_input:
        invite = invite_input.split("discord.gg/")[1]
        return invite
    if "https://discord.gg" in invite_input:
        invite = invite_input.split("https://discord.gg/")[1]
        return invite
    if "invite" in invite_input:
        invite = invite_input.split("/invite/")[1]
        return invite

def menu():
    print(Style.BRIGHT + Fore.RED + r'''
 
 __    __  ______  __     __  ______         _______   ______   ______   ______  ________ ______  
/  \  /  |/      \/  |   /  |/      \       /       \ /      \ /      \ /      \/        /      \ 
$$  \ $$ /$$$$$$  $$ |   $$ /$$$$$$  |      $$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$  $$$$$$$$/$$$$$$  |
$$$  \$$ $$ |  $$ $$ |   $$ $$ |__$$ |      $$ |__$$ $$ |  $$ $$ |  $$ $$ \__$$/   $$ | $$ \__$$/ 
$$$$  $$ $$ |  $$ $$  \ /$$/$$    $$ |      $$    $$<$$ |  $$ $$ |  $$ $$      \   $$ | $$      \ 
$$ $$ $$ $$ |  $$ |$$  /$$/ $$$$$$$$ |      $$$$$$$  $$ |  $$ $$ |  $$ |$$$$$$  |  $$ |  $$$$$$  |
$$ |$$$$ $$ \__$$ | $$ $$/  $$ |  $$ |      $$ |__$$ $$ \__$$ $$ \__$$ /  \__$$ |  $$ | /  \__$$ |
$$ | $$$ $$    $$/   $$$/   $$ |  $$ |      $$    $$/$$    $$/$$    $$/$$    $$/   $$ | $$    $$/ 
$$/   $$/ $$$$$$/     $/    $$/   $$/       $$$$$$$/  $$$$$$/  $$$$$$/  $$$$$$/    $$/   $$$$$$/  
                                                                            


''' + Fore.RESET)
    print(Style.BRIGHT + Fore.GREEN + f"                                                {Fore.UNDERLINE}NOVA X Boost Tool" + Fore.RESET)
    print(Style.BRIGHT + Fore.WHITE + """
                                    [ 01 ] Boost, [ 02 ] Stock, [ 03 ] Exit  
    """ + Fore.RESET)
    

    choice = input(f"\n{Style.BRIGHT}{Fore.WHITE}Option {Fore.ARROW} " + Fore.RESET)
    if choice == "1":
        invite = getinviteCode(input(f"{Style.BRIGHT + Fore.RED}Invite Link/Code {Fore.WHITE}(Example: discord.gg/): {Fore.RESET}"))
        amount = input(f"{Style.BRIGHT + Fore.RED}Amount: {Fore.RESET}")
        while amount.isdigit() != True:
            print(Fore.BLUE + "Amount cannot be 0." + Fore.RESET)
            amount = input(f"{Style.BRIGHT + Fore.RED}Boosts: {Fore.RESET}")
        months = input(f"{Style.BRIGHT + Fore.RED}Months: {Fore.RESET}")
        while amount.isdigit() != True:
            print(Fore.BLUE + "Months cannot be a string." + Fore.RESET)
            months = input(f"{Style.BRIGHT + Fore.RED}Months: {Fore.RESET}")
        start = time.time()
        boosted = thread_boost(invite, int(amount), int(months), config['nickname'], config["bio"])
        end = time.time()
        print()
        sprint(f"Boosted https://discord.gg/{invite} {variables.boosts_done} times in {round(end - start, 2)} seconds.", True)
        print()
        input(Style.BRIGHT + Fore.WHITE + "Press enter to return to menu" + Fore.RESET)
        os.system('')
        menu()
        
    if choice == "2":
        print(f'{Style.BRIGHT + Fore.BLUE}1 Month Nitro Tokens {Fore.WHITE} > {len(open("input/1m_tokens.txt", "r").readlines())}{Fore.RESET}')
        print(f'{Style.BRIGHT + Fore.BLUE}1 Month Boosts {Fore.WHITE} > {len(open("input/1m_tokens.txt", "r").readlines())*2}{Fore.RESET}')
        print()
        print(f'{Style.BRIGHT + Fore.BLUE}3 Month Nitro Tokens {Fore.WHITE} > {len(open("input/3m_tokens.txt", "r").readlines())}{Fore.RESET}')
        print(f'{Style.BRIGHT + Fore.BLUE}3 Month Boosts {Fore.WHITE} > {len(open("input/3m_tokens.txt", "r").readlines())*2}{Fore.RESET}')
        print()
        input(Style.BRIGHT + Fore.WHITE+ "Press enter to return to menu" + Fore.RESET)
        os.system('')
        menu()
        
    if choice == "3":
        quit()
        
if __name__ == "__main__":
    os.system('')
    menu()

