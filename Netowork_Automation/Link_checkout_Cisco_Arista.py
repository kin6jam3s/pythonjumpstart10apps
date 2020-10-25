#!/usr/bin/env python3

import netmiko
import time
import datetime


def main():
    print_header()
    access_device()


def print_header():
    print('--------------------')
    print('    Interface Checkout')
    print('--------------------')


def access_device():
    device = input('Enter device IP: ')
    interface = input('Enter interface(ex.Et1): ')
    # peer_ip = input('Enter Peer IP: ')
    osversion = input('Enter [A]rista or [C]isco e[X]it: ')
    os = osversion.lower().strip()

    now = datetime.datetime.now()
    print('Start time', now)

    cisco = {'device_type': 'cisco_nxos',
             'ip': device,
             'username':'admin1',
             'password':'admin1'
             }

    arista = {'device_type': 'arista_eos',
             'ip': device,
             'username': 'admin',
             'password': 'admin'
             }

    if os == 'c' and os:
        netconnect = netmiko.ConnectHandler(**cisco)
        output = netconnect.send_command('show interface {}'.format(interface))
        print(output)
        netconnect.disconnect()

    elif os == 'a' and os:
        # netconnect = netmiko.ConnectHandler(device_type='arista_eos', ip=device, username='admin', password='admin')
        netconnect = netmiko.ConnectHandler(**arista)
        output = netconnect.send_command('show interface {}'.format(interface))
        print(output)
        netconnect.disconnect()
        print('Disconnecting to the device')
    elif os == 'x' and os:
        print('exit')

    print('Good Bye')


if __name__ == "__main__":
    main()




