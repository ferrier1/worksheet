import paramiko
import time

ip_address = "xxxx"
username = "xxxx"
password = "xxxx"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print "Successful connection", ip_address

remote_connection = ssh_client.invoke_shell()
remote_connection.send("conf t\n")
for n in range (5):
    print "Creating Loopback " + str(n)
    remote_connection.send("int loop " + str(n) +  "\n")
    time.sleep(0.15)

remote_connection.send("end\n")

time.sleep(1)
output = remote_connection.recv(65535)
print output

ssh_client.close
