from netmiko import ConnectHandler  

dev_info_1 = {
    'device_type' : 'cisco_ios',
    'ip' : ' 192.168.122.45',
    'username' : 'john',
    'password' : 'cisco',
    'secret' : 'ccna'
}

dev_info_2 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.31',
    'username' : 'john',
    'password' : 'cisco',
    'secret' : 'ccna'
}

dev_info_3 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.61',
    'username' : 'john',
    'password' : 'cisco',
    'secret' : 'ccna'
}

dev_set = [dev_info_1, dev_info_2, dev_info_3]

for per_dev in dev_set:
    ssh = ConnectHandler(**per_dev)
    output = ssh.enable()
    print(output)
    ssh.config_mode()
    com_list = ['int loop 1' , 'ip add 1.1.1.1 255.255.255.255', 'exit']
    output = ssh.send_config_set(com_list)
    print(output)
    ssh.disconnect()
