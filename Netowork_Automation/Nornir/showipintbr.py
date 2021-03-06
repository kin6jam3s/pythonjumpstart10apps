from nornir import InitNornir
from nornir_scrapli.task import send_command
from nornir.plugins.functions import print_result


nr = InitNornir(config_file="config.yaml")
result = nr.run(task=send_command, command="show ip int br")
print_result(result)
