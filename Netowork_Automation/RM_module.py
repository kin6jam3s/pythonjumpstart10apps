from netmiko import ConnectHandler
import re
from collections import Counter


def rm_grab(arista):
    netconnect = ConnectHandler(**arista)
    netconnect.enable()
    prompt = netconnect.find_prompt()
    #print(prompt)
    ## Take the config
    out1 = netconnect.send_command('sh run ')
    #print(out1)
    #from x in out1:
    ## Check for Route-map starting with RM

    result =re.findall(r'(RM[\w]+)+', out1)
    #print(result)

    ## Consolidate RM
    res = {}
    for i in result:
        res[i] = result.count(i)
    #print(res)

    ## Get all unique Route-map
    uniq_rm = []
    for key,val in dict(res).items():
        if val >= 1:
            uniq_rm.append(key)

    #print(uniq_rm)

    x = []
    for i in uniq_rm:
        out2=netconnect.send_command('sh run | in {}'.format(i))
        #print(out2)
        # pattern = 'in|out$'
        # print(pattern)
        p = re.search(r'\sin|out$', out2)
        #print(p)
        if p:
            #print("{} match --> matchObj.group() : ".format(i), p.group())
            pass
        else:
            #print("No match!!")
            x.append(i)

    # return x
    print(x)

    new_x = []
    for i in x:
        out3 = netconnect.send_command('sh run | in {}'.format(i))
        p = re.search(r'redistribute', out3)
        print(p)
        if p:
            #print("{} match --> matchObj.group() : ".format(i), p.group())
            pass
        else:
            #print("No match!!")
            new_x.append(i)
    print(new_x)
    return new_x

    netconnect.disconnect()