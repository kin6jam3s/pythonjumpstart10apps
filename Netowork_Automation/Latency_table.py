from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import datetime
import os
import time
from termcolor import colored,cprint
from netmiko import ConnectHandler
from prettytable import PrettyTable

ip_name = []

remote_device = {'device_type': 'autodetect',
               'ip': ip_name,
               'username': 'admin',
               'password': 'admin'
               }

device = ['192.168.1.131', '192.168.1.132']


for i in device:
    remote_device['ip'] = i
    print(remote_device)
    netconnect = SSHDetect(**remote_device)
    match = netconnect.autodetect()
    remote_device['device_type'] = match
    if remote_device['device_type'] == 'arista_eos':
        netconnect=ConnectHandler(**remote_device)
        cname = netconnect.find_prompt()
        netconnect.enable()
        pingstat = netconnect.send_command('ping 192.168.1.1 repeat 1')
        arista = []
        with open('test.txt', 'w') as fin:
            for i in pingstat:
                fin.write(i)

        with open('test.txt', 'r') as fout:
            for i in fout:
                arista.append(i)

        x = arista[-1]
        rtt = x.split('/')
        print(rtt[-3], 'ms')
        rtt1 = rtt[-3]


        time.sleep(10)
        netconnect.disconnect()
        remote_device['device_type'] = 'autodetect'

    elif remote_device['device_type'] == 'cisco_nxos':
        netconnect=ConnectHandler(**remote_device)
        cname = netconnect.find_prompt()
        netconnect.enable()
        pingstat = netconnect.send_command('ping 192.168.1.1 source-interface mgmt 0 count 1')
        arista = []
        with open('test.txt', 'w') as fin:
            for i in pingstat:
                fin.write(i)

        with open('test.txt', 'r') as fout:
            for i in fout:
                arista.append(i)

        x = arista[-1]
        rtt = x.split('/')
        print(rtt[-2], 'ms')
        rtt2 = rtt[-2]

        time.sleep(10)
        netconnect.disconnect()
        remote_device['device_type'] = 'autodetect'

x = PrettyTable()

print('Arista {} ms'.format(rtt1))
print('NX-OS {} ms'.format(rtt2))

x.field_names = ["device", "baseline", 'latency(ms)']
x.add_row(["Arista", '1', rtt1])
x.add_row(["NX-OS", '1', rtt2])

print(x)

x_text = x.get_string()
with open('result.txt', 'w') as fin:
    fin.write(x_text)

with open('result.txt', 'r', encoding='UTF') as fout:
    print(fout.read())





    # cname = netconnect.find_prompt()
    # device_name = cname.replace('>', ' ')
    # print('')
    # cprint('Connected to {}'.format(device_name), 'yellow', 'on_red')
    #
