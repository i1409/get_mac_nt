# get_mac_nt

This tool allows you to find an arp register in Edgerouter devices (from Ubiquiti Networks) from your GNU/Linux Terminal

> install requirements running: pip3 install -r reqs.txt

# Usage
- Looking for all registers in the ARP table? run it! (it will ask for the username and password.... password not showed while typing) 

$ ./get_mac.py -a 192.168.1.1


- Looking some registers in the ARP table? run it! (it will ask for the username and password.... password not showed while typing)

$ ./get_mac.py -s 192.168.1.1 192.168.1.150

In this example is looking for the ARP register for 192.168.1.150 host but it could be an ip address, a MAC address, or even just a little part of those criterias and grep work on it
