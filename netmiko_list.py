from netmiko import ConnectHandler

R1 = {
    'device_type': 'cisco_ios',
    'ip': 'xxxx',
    'username': 'xxxx',
    'password': 'xxxx',
    'global_delay_factor': 0,
}

R2 = {
    'device_type': 'cisco_ios',
    'ip': 'xxxx',
    'username': 'xxxx',
    'password': 'xxxx',
    'global_delay_factor': 0,
}

device_list = [R2, R1]

with open('port_config.txt') as f:
    lines = f.read().splitlines()

print(lines)

for device in device_list:
    net_connect = ConnectHandler(**device)
    #net_connect.find_prompt()
    #no need to iterate over file handler when using send_config_set
    output = net_connect.send_config_set(lines, max_loops=10)
    print(output)
