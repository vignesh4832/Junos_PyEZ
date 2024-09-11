from jnpr.junos import Device
from pprint import pprint

device= "10.20.1.1"
user = "admin"
password = "admin"

dev = Device(host=device, user=user, password=password, gather_facts=False)
dev.open()

cnf = dev.rpc.get_config()

interfaces = cnf.findall('.//interface')
for interface in interfaces:
	int_name = interface.findtext('name')
	ip =interface.findtext('unit/family/inet/address/name')
	print (f'{int_name} IP is {ip}')
	
dev.close()


'''
Output :

ge-0/0/0 IP is 20.1.1.1/30
ge-0/0/1 IP is 50.1.1.1/30
fxp0 IP is 10.20.1.1/24
lo0 IP is 1.1.1.1/32

'''