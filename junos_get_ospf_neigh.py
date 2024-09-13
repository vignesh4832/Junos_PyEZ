from jnpr.junos import Device
from lxml import etree   

device= "10.12.1.1"
user = "admin"
password = "admin123"


dev = Device(host=device, user=user, password=password, gather_facts=False)

dev.open()
data = dev.rpc.get_ospf_neighbor_information() # We can pull this info from "show bgp summary | display xml rpc"
print (etree.tostring(data, encoding='unicode', pretty_print=True)) 
dev.close()  


'''

Output from device:

admin@R1> show ospf neighbor 
Address          Interface              State     ID               Pri  Dead
172.16.1.2       ge-0/0/0.0             Full      100.123.1.1      128    39
172.16.2.2       ge-0/0/1.0             Full      100.123.1.1      128    33

admin@R1> show ospf neighbor | display xml 
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/18.3R1/junos">
    <ospf-neighbor-information xmlns="http://xml.juniper.net/junos/18.3R1/junos-routing">
        <ospf-neighbor>
            <neighbor-address>172.16.1.2</neighbor-address>
            <interface-name>ge-0/0/0.0</interface-name>
            <ospf-neighbor-state>Full</ospf-neighbor-state>
            <neighbor-id>100.123.1.1</neighbor-id>
            <neighbor-priority>128</neighbor-priority>
            <activity-timer>39</activity-timer>
        </ospf-neighbor>
        <ospf-neighbor>
            <neighbor-address>172.16.2.2</neighbor-address>
            <interface-name>ge-0/0/1.0</interface-name>
            <ospf-neighbor-state>Full</ospf-neighbor-state>
            <neighbor-id>100.123.1.1</neighbor-id>
            <neighbor-priority>128</neighbor-priority>
            <activity-timer>32</activity-timer>
        </ospf-neighbor>
    </ospf-neighbor-information>
    <cli>
        <banner></banner>
    </cli>
</rpc-reply>



output from script:

labuser@pyez-vm:~$ python3 1.py
<ospf-neighbor-information>
  <ospf-neighbor>
    <neighbor-address>172.16.1.1</neighbor-address>
    <interface-name>ge-0/0/0.0</interface-name>
    <ospf-neighbor-state>Full</ospf-neighbor-state>
    <neighbor-id>100.123.1.0</neighbor-id>
    <neighbor-priority>128</neighbor-priority>
    <activity-timer>31</activity-timer>
  </ospf-neighbor>
  <ospf-neighbor>
    <neighbor-address>172.16.2.1</neighbor-address>
    <interface-name>ge-0/0/1.0</interface-name>
    <ospf-neighbor-state>Full</ospf-neighbor-state>
    <neighbor-id>100.123.1.0</neighbor-id>
    <neighbor-priority>128</neighbor-priority>
    <activity-timer>39</activity-timer>
  </ospf-neighbor>
</ospf-neighbor-information>

'''