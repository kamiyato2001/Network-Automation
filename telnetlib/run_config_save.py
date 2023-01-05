#importing libraries
import getpass
import telnetlib

#Getting user input
user = input("Enter telnet Username: ")
password = getpass.getpass()

#Opening file with the list of IP addresses
file = open("iplist.txt")

for IP in file:
    #Clearing whitespaces from a line
    IP = IP.strip()
    
    #Telnet the host
    tn = telnetlib.Telnet(IP)

    #Writing username and password into CLI
    tn.read_until(b"Username: ")
    tn.write(user.encode("ascii") + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")

    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"terminal length 0\n") #So, we can see switches configuration in one go

    tn.write(b"show run\n")
    tn.write(b"exit\n")
    
    #Creating a file relative to the Swictch's IP and saving it's configuration
    readoutput = tn.read_all()
    saveoutput = open("switch" + IP, "w")

    saveoutput.write(readoutput.decode("ascii"))
    saveoutput.write("\n")
    saveoutput.close()