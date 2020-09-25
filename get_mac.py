#!/usr/bin/env python3
from argparse import ArgumentParser
import sys
from pexpect import pxssh
import pty

banner = """
    .------..------..------..------..------..------..------.
    |I.--. ||H.--. ||Y.--. ||P.--. ||E.--. ||R.--. ||X.--. |
    | (\/) || :/\: || (\/) || :/\: || (\/) || :(): || :/\: |
    | :\/: || (__) || :\/: || (__) || :\/: || ()() || (__) |
    | '--'I|| '--'H|| '--'Y|| '--'P|| '--'E|| '--'R|| '--'X|
    `------'`------'`------'`------'`------'`------'`------'
"""
usage_="""

    ~$ python3 get_mac.py -h    |   Show the help
    ~$ python3 get_mac.py -a 192.168.1.1    |   Get ARP TABLE from 192.168.1.1
    ~$ python3 get_mac.py -s 192.168.1.1 10.1.1.1   |   Get the ARP REGISTERED of 10.1.1.1 from 192.168.1.1
"""
cli = pxssh.pxssh()
parser = ArgumentParser(description='%(prog)s is an ARP Finder\n',usage=usage_)

def cliConn(target='192.168.0.60', usr='admin', passwd='80211Alf.'):
    try:
        cli.login(target, usr, passwd)
        msg = 'Fetching INFO...'
        print ("->{:>20}".format(msg))
        return cli
    except:
        print("Connection Failed")

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
    print(banner)
    parser.add_argument('-a', '--all', help='This option gets ALL ARP TABLE from the host given')
    parser.add_argument('-s', '--search', nargs=2, help='This option searches an ARP INFO from the host given based on an IP to look for')
    args = parser.parse_args()
    if args.all is None and args.search is None:
        print(parser.usage)
        exit()
    cmd = "show arp  | grep "
    if args.all:
        cmd += ': | sort'
        host = args.all
    if args.search:
        cmd += args.search[1] + ' | sort'
        host = args.search[0]
    username = input("Enter username-> ")
    passwd = input("Enter password-> ")
    try:
        ssh = cliConn(host,username,passwd)
        print(cliCMD(ssh,cmd))
    except KeyboardInterrupt:
        print('Execution Aborted')
    except:
        print('Something went wrong... Aborting...')
    else:
        print('Good Luck')

if __name__  == '__main__':
    main()
