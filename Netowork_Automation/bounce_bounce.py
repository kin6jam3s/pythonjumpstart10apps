from netmiko import ConnectHandler
from rich import print as rprint
from termcolor import colored, cprint
import time


def connect_to_device(remote_device, interface, ip_name):
    if remote_device['device_type'] == 'arista_eos':
        netconnect = ConnectHandler(**remote_device)
        cname = netconnect.find_prompt()
        device_name = cname.replace('>', ' ')
        print('')
        cprint('Connected to {}'.format(device_name), 'yellow', 'on_red')
        cprint('...Performing PRE-CHECK...', 'yellow', 'on_red')
        print('')
        shint = netconnect.send_command('show interface {} | in ip|Desc|Et'.format(interface))
        rprint(shint)
        netconnect.enable()
        # print(netconnect.find_prompt())
        time.sleep(5)
        print(colored('Checking interface description if port is a TAP', 'white', 'on_red', attrs=['reverse', 'blink']))
        print('')
        x = []
        intf_conf = netconnect.send_command('show run int {} | in desc'.format(interface))
        x = intf_conf.strip()
        result = x.find('TAP')
        if result != -1:
            print(colored('PORT IS A TAP', 'white', 'on_red', attrs=['reverse', 'blink']))

        else:
            print(colored('PORT IS NOT A TAP', 'white', 'on_red', attrs=['reverse', 'blink']))
            rprint('[red]...Disconnecting[red]')
            netconnect.disconnect()

        # matching = [s for s in tap if "TAP" in s]
        # print(matching)
        print('')
        shrun = netconnect.send_command('show run interface {}'.format(interface))
        rprint(shrun)
        print('')
        print(colored('##########################################', 'white', 'on_red', attrs=['reverse', 'blink']))
        print('ARE YOU SURE YOU WANT TO BOUNCE THIS PORT?')
        print(colored('##########################################', 'white', 'on_red', attrs=['reverse', 'blink']))
        rprint('')
        user_input = input('ENTER [Y]es or [N]o: ')
        select = user_input.lower().strip()

        if select == 'y' and select:
            commands = ['int {}'.format(interface), 'shutdown',
                        'do show run diff',
                        'no shut', 'do show run int {}'.format(interface),
                        'do show run diff']
            print('')
            output = netconnect.send_config_set(commands)
            output += netconnect.save_config()
            rprint(output)
            print('')
            time.sleep(10)
            netconnect.disconnect()
            rprint('[red]..Disconnecting to {} [red]'.format(device_name))

        elif select == 'n' and select:
            print('..Try again..')
            netconnect.disconnect()

        else:
            rprint('.Try Again..')

    else:
        print(colored('This script is only for Arista AGG device', 'white', 'on_red', attrs=['reverse', 'blink']))