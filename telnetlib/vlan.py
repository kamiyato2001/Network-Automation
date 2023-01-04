#importing libraries
import telnetlib
import getpass

#Getting user input
username = input("Enter username: ")
password = getpass.getpass()

file = open('iplist')

for ip in file:
    #To remove whitespaces from line
    ip = ip.strip()
    host = ip
    #Telnet the host
    tn = telnetlib.Telnet(host)

    tn.read_until(b"Username: ")
    tn.write(username.encode("ascii") + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")

    tn.write(b"en\n")
    tn.write(b"conf t\n")

    #creating even vlans in the range 2-20
    for i in range(2, 20 , 2):
        tn.write(b"vlan " + str(i).encode("ascii") + b"\n")

    tn.write(b"end\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode("ascii"))