#!/usr/bin/env python3


from netmiko import ConnectHandler
from acl_module import acl_grab
from prefix_module import prf_grab
from RM_module import rm_grab
from config_gen_module import config_gen
from int_clean_module import int_grab
import getpass


def main():

    print_header()
    arista = user_input()
    # print(arista)
    acl_return = acl_test(arista)
    prfx_return = prefix_test(arista)
    rm_return = rm_test(arista)
    int_return = int_test(arista)
    config_test(arista, acl_return, prfx_return, rm_return, int_return)



def print_header():
    print('########################################')
    print('#######   CONFIG CLEAN-UP TOOL  ########')
    print('########################################')


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
    return prfx_return


def rm_test(arista):
    rm_return = rm_grab(arista)
    print('BELOW')
    print(rm_return)
    return rm_return


def int_test(arista):
    int_return = int_grab(arista)
    print('BELOW')
    print(int_return)
    return int_return


def config_test(arista, acl_return, prfx_return, rm_return, int_return):
     config_gen(arista, acl_return, prfx_return, rm_return, int_return)


if __name__ == "__main__":
    main()