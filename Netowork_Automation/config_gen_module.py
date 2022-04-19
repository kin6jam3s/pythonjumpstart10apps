from netmiko import ConnectHandler


def config_gen(arista, acl_return, prfx_return, rm_return, int_return):
    # print(arista)
    # print(acl_return)
    # print(prfx_return)
    # print(rm_return)
    # print(int_return)

    netconnect = ConnectHandler(**arista)
    netconnect.enable()
    prompt = netconnect.find_prompt()
    dname = prompt.replace('#','')

    print('############### COPY THE CONFIG BELOW ###############')
    print('notes:')
    print('')
    print('')
    print('Arista Device Cleanup')
    print('')
    print('hosts: {}'.format(dname))
    print('')
    print('implementation:')
    for i in int_return:
        print('default int {}'.format(i))
        print('int {}'.format(i))
        print('description NOT_IN_USE\n', 'shutdown')
    print('!')
    for i in acl_return:
        print('no ip access-list {}'.format(i))
    print('!')
    for i in prfx_return:
        print('no ip prefix-list {}'.format(i))
    print('!')
    for i in rm_return:
        print('no route-map {}'.format(i))
    print('!\n', 'end\n','sh run diff\n','wr')
    print('')

    print('verification:')
    for i in int_return:
        print('sh run int {}'.format(i))
    print('')
    for i in acl_return:
        print('show ip access-list {}'.format(i))
    print('')
    for i in prfx_return:
        print('show ip prefix-list {}'.format(i))
    print('')
    for i in rm_return:
        print('show route-map {}'.format(i))
    print('')

    print('rollback:')
    for i in int_return:
        out = netconnect.send_command('sh run int {}'.format(i))
        print(out)
    print('!')
    for i in acl_return:
        out = netconnect.send_command('sh run | sec {}'.format(i))
        print(out)
    print('!')
    for i in prfx_return:
        out = netconnect.send_command('sh run | sec {}'.format(i))
        print(out)
    print('!')
    for i in rm_return:
        out = netconnect.send_command('sh run | sec {}'.format(i))
        print(out)
    print('!\n','end\n','sh run diff\n','wr')
    print('')
    netconnect.disconnect()

