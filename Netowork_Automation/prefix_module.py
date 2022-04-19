from netmiko import ConnectHandler
import re
from collections import Counter


def prf_grab(arista):
    # xip = device
    # usernme = username
    # pswrd = p
    #
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
    ## Check for ACL starting with PRF
    pattern = 'PRF.*'
    result = re.findall(pattern, out1)
    #print(result)

    ## Count How often the PRF is used
    res = {}
    for i in result:
        res[i] = result.count(i)
    #print(res)

    # res = Counter(result)
    # #print(res)
    # counter1 = res
    # print(counter1)
    ## Take all single PRF count and add them on the list
    uniq_prefix = []
    for key,val in dict(res).items():
        if val == 1:
            uniq_prefix.append(key)
    #print(uniq_prefix)
    return uniq_prefix

    ## Generate the PREFIX config
    # for i in uniq:
    #     out1 = netconnect.send_command('sh run | sec {}'.format(i))
    #     print(out1)
    netconnect.disconnect()