from statistics import quantiles
import colorama
import time
from colorama import Fore
colorama.init()

RED = Fore.RED
BLUE = Fore.BLUE
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
RESET = Fore.RESET

def display_banner():
    banner_text= '''
 _    _            _      _______          _  
| |  | |          | |    |__   __|        | | 
| |__| | __ _  ___| | __    | | ___   ___ | | 
|  __  |/ _` |/ __| |/ /    | |/ _ \ / _ \| | 
| |  | | (_| | (__|   <     | | (_) | (_) | | 
|_|  |_|\__,_|\___|_|\_\    |_|\___/ \___/|_| 

Hack Tool 
Coded by Adam
-First Project-
                                             
    '''
    print(f"{CYAN}{banner_text}{RESET}")

display_banner()

time.sleep(1)
print(Fore.RED+'\nDO AT YOUR OWN RISK!')
time.sleep(1)

# option
print(Fore.RED+'\nFacebook [1]\nInstagram [2]\nYoutube [3]')
time.sleep(1)
hack = input('\n\nWhich one you want to hack?: ')

if str(1) in hack:
    
    username=input('\nTarget username: ')
    
    print(Fore.YELLOW+'\n\nPlease wait')
    time.sleep(3)
    print(f'Collecting data from {username}')
    time.sleep(2)
    print('Searching account...')
    time.sleep(7)
    print(Fore.GREEN+'Account was found!')
    time.sleep(3)
    print('Waiting for attacking')
    time.sleep(5)
    print('Attack is starting... \n\n\n')
    time.sleep(5)


    a = Fore.GREEN+f"Collecting data from {username}"
    
    for i in range(0,101):
        print(a+"  "+"- "+str(i)+"%")
        
        time.sleep(0.1)
    b = f"Attacking {username}'s IP Adress"
    c = "Cracking password..."
    for i in range(101):
        print(b+"  "+"- "+str(i)+"%")
        print(c+"  "+"- "+str(i)+"%")
        time.sleep(0.1)
    
        if i ==100:
            
            print(Fore.RED+f"\n{username}'s Password has been cracked!")
            time.sleep(3)
            print(f"Open this link in Chrome to get his pass: https://bit.ly/the-power-of-link")
            time.sleep(8)
            quit= input('Press q and enter to quit: ')
            if 'q' in quit:
                quit()

elif str(2) in hack:

    
    username=input('\nTarget username: ')
    
    print(Fore.YELLOW+'\n\nPlease wait')
    time.sleep(3)
    print(f'Collecting data from {username}')
    time.sleep(2)
    print('Searching account...')
    time.sleep(7)
    print(Fore.GREEN+'Account was found!')
    time.sleep(3)
    print('Waiting for attacking')
    time.sleep(5)
    print('Attack is starting... \n\n\n')
    time.sleep(5)


    a = Fore.GREEN+f"Collecting data from {username}"
    
    for i in range(0,101):
        print(a+"  "+"- "+str(i)+"%")
        
        time.sleep(0.1)
    b = f"Attacking {username}'s IP Adress"
    c = "Cracking password..."
    for i in range(101):
        print(b+"  "+"- "+str(i)+"%")
        print(c+"  "+"- "+str(i)+"%")
        time.sleep(0.1)
    
        if i ==100:
            
            print(Fore.RED+f"\n{username}'s Password has been cracked!")
            time.sleep(3)
            print(f"Open this link in Chrome to get his pass: https://bit.ly/the-power-of-link")
            time.sleep(8)
            quit= input('Press q and enter to quit: ')
            if 'q' in quit:
                quit()

elif str(3) in hack:

    
    username=input('\nTarget username: ')
    
    print(Fore.YELLOW+'\n\nPlease wait')
    time.sleep(3)
    print(f'Collecting data from {username}')
    time.sleep(2)
    print('Searching account...')
    time.sleep(7)
    print(Fore.GREEN+'Account was found!')
    time.sleep(3)
    print('Waiting for attacking')
    time.sleep(5)
    print('Attack is starting... \n\n\n')
    time.sleep(5)


    a = Fore.GREEN+f"Collecting data from {username}"
    
    for i in range(0,101):
        print(a+"  "+"- "+str(i)+"%")
        
        time.sleep(0.1)
    b = f"Attacking {username}'s IP Adress"
    c = "Cracking password..."
    for i in range(101):
        print(b+"  "+"- "+str(i)+"%")
        print(c+"  "+"- "+str(i)+"%")
        time.sleep(0.1)
    
        if i ==100:
            
            print(Fore.RED+f"\n{username}'s Password has been cracked!")
            time.sleep(3)
            print(f"Open this link in Chrome to get his pass: https://bit.ly/the-power-of-link")
            time.sleep(8)
            quit= input('Press q and enter to quit: ')
            if 'q' in quit:
                quit()


else:
    quit()