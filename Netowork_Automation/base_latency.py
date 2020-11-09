import time
from netmiko import ConnectHandler
from prettytable import PrettyTable
import datetime

device1 = {'device_type': 'arista_eos',
               'ip': '192.168.1.131',
               'username': 'admin',
               'password': 'admin'
               }

device2 = {'device_type': 'cisco_nxos',
               'ip': '192.168.1.132',
               'username': 'admin',
               'password': 'admin'
               }

netconnect = ConnectHandler(**device1)
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
print(rtt[-3],'ms')
rtt1 = rtt[-3]

pingstat = netconnect.send_command('ping 192.168.1.147 repeat 1')

arista = []
with open('test.txt', 'w') as fin:
    for i in pingstat:
        fin.write(i)

with open('test.txt', 'r') as fout:
    for i in fout:
        arista.append(i)

x = arista[-1]
rtt = x.split('/')
# rtt3 = rtt[-3]
print(rtt)


netconnect.disconnect()

netconnect=ConnectHandler(**device2)
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


x = PrettyTable()

print('Arista {} ms'.format(rtt1))
print('NX-OS {} ms'.format(rtt2))

x.field_names = ["device", "baseline", 'latency(ms)']
x.add_row(["Arista", '1', rtt1])
x.add_row(["NX-OS", '1', rtt2])
x.add_row(["Arista", '1', rtt3])

print(x)

x_text = x.get_string()
with open('result.txt', 'w') as fin:
    fin.write(x_text)

# with open('result.txt', 'r', encoding='UTF') as fout:
#     print(fout.read())
