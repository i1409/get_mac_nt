#!/usr/bin/env python3
from argparse import ArgumentParser
import sys
from pexpect import pxssh
from datetime import datetime
import random

banner_list = ["""
    .------..------..------..------..------..------..------.
    |I.--. ||H.--. ||Y.--. ||P.--. ||E.--. ||R.--. ||X.--. |
    | (\/) || :/\: || (\/) || :/\: || (\/) || :(): || :/\: |
    | :\/: || (__) || :\/: || (__) || :\/: || ()() || (__) |
    | '--'I|| '--'H|| '--'Y|| '--'P|| '--'E|| '--'R|| '--'X|
    `------'`------'`------'`------'`------'`------'`------'
""",
"""
    /$$ /$$                                                        
    |__/| $$                                                        
    /$$| $$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$
    | $$| $$__  $$| $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$|  $$ /$$/
    | $$| $$  \ $$| $$  | $$| $$  \ $$| $$$$$$$$| $$  \__/ \  $$$$/ 
    | $$| $$  | $$| $$  | $$| $$  | $$| $$_____/| $$        >$$  $$ 
    | $$| $$  | $$|  $$$$$$$| $$$$$$$/|  $$$$$$$| $$       /$$/\  $$
    |__/|__/  |__/ \____  $$| $$____/  \_______/|__/      |__/  \__/
                /$$  | $$| $$                                    
                |  $$$$$$/| $$                                    
                \______/ |__/                                    
""",
"""  _ _                                
    (_) |                               
    _| |__  _   _ _ __   ___ _ ____  __
    | | '_ \| | | | '_ \ / _ \ '__\ \/ /
    | | | | | |_| | |_) |  __/ |   >  < 
    |_|_| |_|\__, | .__/ \___|_|  /_/\_\
              __/ | |                   
             |___/|_|                   
""",
"""
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     _____    | || |  ____  ____  | || |  ____  ____  | || |   ______     | || |  _________   | || |  _______     | || |  ____  ____  | |
| |    |_   _|   | || | |_   ||   _| | || | |_  _||_  _| | || |  |_   __ \   | || | |_   ___  |  | || | |_   __ \    | || | |_  _||_  _| | |
| |      | |     | || |   | |__| |   | || |   \ \  / /   | || |    | |__) |  | || |   | |_  \_|  | || |   | |__) |   | || |   \ \  / /   | |
| |      | |     | || |   |  __  |   | || |    \ \/ /    | || |    |  ___/   | || |   |  _|  _   | || |   |  __ /    | || |    > `' <    | |
| |     _| |_    | || |  _| |  | |_  | || |    _|  |_    | || |   _| |_      | || |  _| |___/ |  | || |  _| |  \ \_  | || |  _/ /'`\ \_  | |
| |    |_____|   | || | |____||____| | || |   |______|   | || |  |_____|     | || | |_________|  | || | |____| |___| | || | |____||____| | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
""",
"""
                                                                                                     
                                                                                                     
.--.   .                      _________   _...._            __.....__                                
|__| .'|       .-.          .-\        |.'      '-.     .-''         '.                              
.--.<  |        \ \        / / \        .'```'.    '.  /     .-''"'-.  `. .-,.--.                    
|  | | |         \ \      / /   \      |       \     \/     /________\   \|  .-. | ____     _____    
|  | | | .'''-.   \ \    / /     |     |        |    ||                  || |  | |`.   \  .'    /    
|  | | |/.'''. \   \ \  / /      |      \      /    . \    .-------------'| |  | |  `.  `'    .'     
|  | |  /    | |    \ `  /       |     |\`'-.-'   .'   \    '-.____...---.| |  '-     '.    .'       
|__| | |     | |     \  /        |     | '-....-'`      `.             .' | |         .'     `.      
     | |     | |     / /        .'     '.                 `''-...... -'   | |       .'  .'`.   `.    
     | '.    | '.|`-' /       '-----------'                               |_|     .'   /    `.   `.  
     '---'   '---''..'                                                           '----'       '----' 
"""
]
usage_="""

    ~$ python3 get_mac.py -h    |   Show the help
    ~$ python3 get_mac.py -a 192.168.1.1    |   Get ARP TABLE from 192.168.1.1
    ~$ python3 get_mac.py -s 192.168.1.1 10.1.1.1 10.1.1.2  |   Get the ARP REGISTERED of 10.1.1.1,10.1.1.2 from 192.168.1.1
"""
cli = pxssh.pxssh()
parser = ArgumentParser(description='%(prog)s is an ARP Finder\n',usage=usage_)
users_list = open('../users.txt')
passwords_list = open('../passwords.txt')
log = open('../get_mac_log.txt','a')
num = random.randint(0, 4)
def cliConn(target, usr, passwd):
    try:
        cli.login(target, usr, passwd)
        msg = 'Fetching INFO...'
        print ("->{:>20}".format(msg))
        return cli
    except KeyboardInterrupt:
        print("Connection Cancelled")

def cliCMD(ssh,cmd):
    try:
        ssh.sendline(cmd)
        ssh.prompt()
        print()
        return ssh.before.decode('utf-8').strip(cmd).strip()
        ssh.logout()
    except KeyboardInterrupt:
        print ("Connection interrumpted.")
    except Exception as e:
        print('Connection not established, try again')
def main():
    print(banner_list[num])
    parser.add_argument('-a', '--all', help='This option gets ALL ARP TABLE from the host given')
    parser.add_argument('-s', '--search', nargs='+', help='This option searches an ARP INFO from the host given based on the IP ADDRESSES to look for')
    args = parser.parse_args()
    if args.all is None and args.search is None:
        print(parser.usage)
        exit()
    cmd = "show arp  | grep "
    if args.all:
        cmd += ': | sort'
        host = args.all
    if args.search:
        host = args.search[0]
        cmd += "-E -- '"
        for i,ip in enumerate(args.search): 
            if i == 0:
                cmd
            elif i == len(args.search)-1:
                cmd += ip
            else:
                cmd += ip + '|'
        cmd += "'"
    for user in users_list:
        user = user.strip()
        for password in passwords_list:
            password = password.strip()
            now = datetime.now()
            try:
                ssh = cliConn(host,user,password)
                log.write('{}-{:>5} auth successful\n'.format(now,user))
                break
            except Exception as err:
                log.write('{}-{:>5}|{} auth failed\t|{}\n'.format(now,user,password,err))
            else:
                print('Right credentials.')
    try:
        print(cliCMD(ssh,cmd))
    except KeyboardInterrupt:
        print('Execution Aborted')
    except:
        print('Something went wrong... Aborting...')
    else:
        print('Good Luck')

if __name__  == '__main__':
    main()
