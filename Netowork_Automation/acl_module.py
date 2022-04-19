from netmiko import ConnectHandler
import re
from collections import Counter


def acl_grab(arista):
    # xip = device
    # usernme = username
    # pswrd = p

    # arista = {'device_type': 'arista_eos',
    #           'ip': xip,
    #           'username': usernme,
    #           'password': pswrd,
    #           'secret': pswrd
    #           }

    netconnect = ConnectHandler(**arista)
    netconnect.enable()
    prompt = netconnect.find_prompt()
    #print(prompt)
    ## Take the config
    out1 = netconnect.send_command('sh run ')
    #print(out1)
    #from x in out1:
    ## Check for ACL starting with NL | NP | RACL | MB
    pattern = 'NL.*|NP.*|RACL.*'
    result = re.findall(pattern, out1)
    #print(result)

    ## Count How often the ACL is used
    res = {}
    for i in result:
        res[i] = result.count(i)
    #print(res)

    # res = Counter(result)
    # #print(res)
    # counter1 = res
    # print(counter1)
    ## Take all single ACL count and add them on the list
    uniq_acl = []
    for key,val in dict(res).items():
        if val == 1:
            uniq_acl.append(key)
    # print(uniq_acl)
    return uniq_acl

    ## Generate the config
    # for i in uniq:
    #     out1 = netconnect.send_command('sh run | sec {}'.format(i))
    #     print(out1)
    # netconnect.disconnect()





