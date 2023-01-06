from netmiko import ConnectHandler  

dev_info = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.1.3',
    'username' : 'john',
    'password' : 'cisco',
    'secret' : 'ccna'
}

ssh = ConnectHandler(**dev_info)

output = ssh.enable()
print(output)
ssh.config_mode()
com_list = ['int loop 1' , 'ip add 1.1.1.1 255.255.255.255', 'exit']
output = ssh.send_command('int loop 0')
output = ssh.send_command('ip add 1.1.1.2 255.255.255.255')
output = ssh.send_command('exit')
print(output)
ssh.disconnect()