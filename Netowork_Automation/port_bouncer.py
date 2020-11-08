#!/usr/bin/env python3

from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import datetime
import os
import sys
from termcolor import colored, cprint
from bounce_bounce import connect_to_device


def main():
    print_header()
    ip_name, interface = user_input()
    remote_device = device_access(ip_name)
    get_output(interface, remote_device, ip_name)


def print_header():
    print('')
    print(colored('##########################################################################', 'white', 'on_red', attrs=['reverse', 'blink']))
    print(colored('WARNING: THIS IS ONLY USE FOR BOUNCING PORT ON ARISTA AGG CONNECTED TO TAP', 'white', 'on_red', attrs=['reverse', 'blink']))
    print(colored('##########################################################################', 'white', 'on_red', attrs=['reverse', 'blink']))
    print('')


def user_input():
    # ip_name = input('Device: ')
    # interface = input('interface: ')
    ip_name = sys.argv[1]
    interface = sys.argv[2]
    print(ip_name, interface)
    return ip_name, interface

    now = datetime.datetime.now()
    print('')
    rprint('Start time', now)
    print('')


def device_access(ip_name):
    # Checking device reachability
    response = os.system('ping -c1 {}'.format(ip_name))
    if response == 0:
        cprint('...DEVICE IS ACTIVE..', 'green', 'on_red')
    else:
        cprint('..DEVICE IS DOWN...', 'green', 'on_red')

    remote_device = {'device_type': 'autodetect',
                     'ip': ip_name,
                     'username': 'admin',
                     'password': 'admin'
                     }

    try:
        netconnect = SSHDetect(**remote_device)
        match = netconnect.autodetect()
        print('')
        cprint('...Checking device type..', 'yellow', 'on_red')
        cprint('Device type: {}'.format(match), 'yellow', 'on_red')
        print('')
        remote_device['device_type'] = match
        return remote_device

    except NetMikoTimeoutException:
        cprint('Device not reachable..', 'green', 'on_red')

    except AuthenticationException:
        cprint('Authentication Failure..', 'green', 'on_red')

    except SSHException:
        cprint('Make sure ssh is enable', 'green', 'on_red')


def get_output(interface, remote_device, ip_name):
    connect_to_device(remote_device, interface, ip_name)


if __name__ == '__main__':
    main()
