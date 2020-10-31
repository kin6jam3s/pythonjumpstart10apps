#!/usr/bin/env python3

from netmiko.ssh_autodetect import SSHDetect
import netmiko
import datetime
import getpass
from rich import print as rprint
from connect_module import connect_to_device


def main():
    print_header()
    ipaddress, interface, username, password, peer_ip = user_input()
    remote_device = access_device(ipaddress, username, password)
    get_output(interface, remote_device, peer_ip)


def print_header():
    print('--------------------')
    rprint('[cyan]Interface Checkout[cyan]')
    print('--------------------')


def user_input():
    username = input('username: ')
    password = getpass.getpass()
    device = input('Enter device IP: ')
    interface = input('Enter interface(ex.Et1): ')
    peer_ip = input('Enter Peer IP: ')
    return device, interface, username, password, peer_ip


def access_device(ipaddress, username, password):
    now = datetime.datetime.now()
    print('')
    rprint('[red]Start time[red]', now)
    print('')

    remote_device = {'device_type': 'autodetect',
                     'ip': ipaddress,
                     'username': username,
                     'password': password
                     }

    netconnect = SSHDetect(**remote_device)
    match = netconnect.autodetect()
    print('...Checking device type..')
    print('Device type: {}'.format(match))
    print('')
    remote_device['device_type'] = match
    return remote_device


def get_output(interface, remote_device, peer_ip):
    connect_to_device(remote_device, interface, peer_ip)


if __name__ == "__main__":
    main()
