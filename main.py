import subprocess
for i in range(20):
    command = ['ping', '-n', '1', '192.168.1.1' + str(i)]  # icrement the device names
    subprocess.call(command)  # ping the devices to update data before  "arp -a'

arpa = subprocess.check_output(("arp", "-a")).decode("utf-8")  # call 'arp -a' and get results
print(arpa)
