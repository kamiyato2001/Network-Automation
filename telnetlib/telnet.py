#Importing libraries
import getpass
import telnetlib

#Getting user input
HOST = input("Enter host: ")
username = input("Enter your telnet username: ")
password = getpass.getpass()

#Telnet the Host
tn = telnetlib.Telnet(HOST)


tn.read_until(b"Username: ")
tn.write(username.encode('ascii') + b'\n')

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

#Executing some commands on the router
tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"interface loop 1\n")
tn.write(b"ip add 1.1.1.1 255.255.255.255\n")

tn.write(b"router ospf 100\n")
tn.write(b"router-id 2.2.2.2\n")

tn.write(b"int loop 1\n")
tn.write(b"ip ospf 100 a 0\n")

tn.write(b"int e1/0\n")
tn.write(b"ip ospf 100 a 0\n")

#Saving configuration
tn.write(b"end\n")
tn.write(b"write\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))