#!/usr/bin/env python3


from netmiko import ConnectHandler
from acl_module import acl_grab
from prefix_module import prf_grab
from RM_module import rm_grab
import getpass


def main():

    print_header()
    arista = user_input()
    # print(arista)
    acl_return = acl_test(arista)
    prfx_return = prefix_test(arista)
    rm_test(arista)
    # generate_config(acl_return, prfx_return)
    #RM_test()


def print_header():
    print('###########################')
    print('#######   TESTING  ########')
    print('###########################')


def user_input():
    # device = input('Enter device name or IP: ')
    device = '192.168.1.131'
    usernme = input('Username: ')
    p = getpass.getpass('Password: ')

    arista = {'device_type': 'arista_eos',
              'ip': device,
              'username': usernme,
              'password': p,
              'secret': p
              }

    return arista


def acl_test(arista):
    acl_return = acl_grab(arista)
    print('BELOW')
    print(acl_return)
    return acl_return

def prefix_test(arista):
    prfx_return = prf_grab(arista)
    print('BELOW')
    print(prfx_return)


def rm_test(arista):
    rm_return = rm_grab(arista)
    print('BELOW')
    print(rm_return)


if __name__ == "__main__":
    main()