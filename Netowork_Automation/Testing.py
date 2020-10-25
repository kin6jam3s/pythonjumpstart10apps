#!/usr/bin/env python3

import netmiko
import time


def main():
    print_header()
    access_device()


def print_header():
    print('--------------------')
    print('    Interface Checkout')
    print('--------------------')


def access_device():
    # username and password can be modified
    username = 'admin'
    password = 'admin'
    device = input('Enter device IP: ')
    interface = input('Enter interface(ex.Et1): ')
    peer_ip = input('Enter Peer IP: ')

    print('...Connecting to device')
    arista = netmiko.ConnectHandler(device_type='arista_eos', ip=device, username=username, password=password)
    Cisco = netmiko.ConnectHandler(device_type='cisco_nxos', ip=device, username=username, password=password)


    prompt = arista.find_prompt()
    dname = prompt.replace(">", " ")
    print(dname)
    print('Connected to {} '.format(prompt))

    print('...Initiating Checkout in 5sec...')
    time.sleep(5)
    print('======Interface status======')
    intstat = arista.send_command('show interface {} | in Et|Desc|input'.format(interface))
    print(intstat)
    time.sleep(3)
    print('======BGP status======')
    time.sleep(5)
    bgpstat = arista.send_command('show ip bgp summ | in N|id|{}'.format(peer_ip))
    print(bgpstat)
    time.sleep(3)
    print('======Latency check status======')
    latencystat = arista.send_command('ping {}'.format(peer_ip))
    print(latencystat)
    print('...Disconnecting to device {}'.format(device))
    arista.disconnect()


print('...Checkout complete')

if __name__ == "__main__":
    main()
