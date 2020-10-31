import netmiko
from rich import print as rprint


def connect_to_device(remote_device, interface, peer_ip):
    if remote_device['device_type'] == 'arista_eos':
        netconnect = netmiko.ConnectHandler(**remote_device)
        cname = netconnect.find_prompt()
        device_name = cname.replace('>', ' ')
        rprint('Connected to {}'.format(device_name))
        output = netconnect.send_command('show interface {}'.format(interface))
        rprint(output)
        rprint('======================')
        rprint('[red]..Disconnecting to {} [red]'.format(device_name))
        netconnect.disconnect()

    elif remote_device['device_type'] == 'cisco_nxos':
        netconnect = netmiko.ConnectHandler(**remote_device)
        cname = netconnect.find_prompt()
        device_name = cname.replace('>', ' ')
        rprint('Connected to {}'.format(device_name))
        output = netconnect.send_command('show interface {}'.format(interface))
        rprint(output)
        rprint('======================')
        rprint('..Disconnecting to {} '.format(device_name))
        netconnect.disconnect()
    else:
        print('Exit..')

    rprint('[red]...session closed[red]')

