from netmiko import ConnectHandler

sw_1 = {
    'device_type' : 'cisco_ios',
    'ip' : ' 192.168.122.45',
    'username' : 'john',
    'password' : 'cisco',
    'secret' : 'ccna'
}

sw_2 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.31',
    'username' : 'john',
    'password' : 'cisco',
    'secret' : 'ccna'
}

sw_3 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.61',
    'username' : 'john',
    'password' : 'cisco',
    'secret' : 'ccna'
}

dev_set = [sw_1, sw_2, sw_3]
i = 1
for per_dev in dev_set:
    with open(f"sw_{i}",'w') as file: 
        ssh = ConnectHandler(**per_dev)
        ssh.enable()
        ssh.send_command('terminal length 0')
        output = ssh.send_command('sh run all')
        file.write(output)
        ssh.disconnect()
        i = i + 1
    