from netmiko import ConnectHandler
import re
from collections import Counter


def int_grab(arista):
    netconnect = ConnectHandler(**arista)
    netconnect.enable()
    prompt = netconnect.find_prompt()

    out1 = netconnect.send_command('sh int desc')
    result=re.findall(r'Et.*\s+admin',out1)
    #print(result)

    ## Get interface on admin down
    z = []
    for i in result:
        x = i.split(' ')
        y = x[0]
    #    print(x)
    #    print(y)
        z.append(y)
    print(z)

    ## sort by interface
    zz = []
    for i in z:
        out2 = netconnect.send_command('sh run int {}'.format(i))
        p = re.search(r'NOT_IN_USED', out2)
        #print(p)
        if p:
            #print("{} match --> matchObj.group() : ".format(i), p.group())
            pass
        else:
            #print("No match!!")
            zz.append(i)
    #print(zz)
    return zz
    netconnect.disconnect()