from jnpr.junos import Device
from jnpr.junos.utils.config import Config

device= "10.20.1.1"
user = "admin"
password = "admin"


dev = Device(host=device, user=user, password=password, gather_facts=False)
dev.open()

cu = Config(dev)
with open("config_file.txt", "r") as cnf:
    for command in cnf:
        cu.load(command)
if cu.commit_check():
   cu.commit()
else:
   cu.rollback()

dev.close()


'''

config_file.txt:

set protocols bgp group ibgp type internal
set protocols bgp group ibgp local-address 1.1.1.1
set protocols bgp group ibgp peer-as 65001
set protocols bgp group ibgp local-as 65001
set protocols bgp group ibgp neighbor 2.2.2.2

output:

admin@R1> show configuration protocols bgp|display set 
set protocols bgp group ibgp type internal
set protocols bgp group ibgp local-address 1.1.1.1
set protocols bgp group ibgp peer-as 65001
set protocols bgp group ibgp local-as 65001
set protocols bgp group ibgp neighbor 2.2.2.2

'''