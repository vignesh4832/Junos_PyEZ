from jnpr.junos import Device
from jnpr.junos.utils.config import Config

device= "10.20.1.1"
user = "jcluser"
password = "Juniper!1"

dev = Device(host=device, user=user, password=password, gather_facts=False)
dev.open()

cu = Config(dev)

data = """

 <interfaces>
    <interface>
        <name>ge-0/0/1</name>
        <description>test</description>
    </interface>
 </interfaces>

"""

cu.load(data)
if cu.commit_check():
   cu.commit()
else:
   cu.rollback()

dev.close()


'''
Output:


Pre-cehck:

admin@R1> show configuration interfaces ge-0/0/1| display xml 
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/18.3R1/junos">
    <configuration junos:commit-seconds="1726039843" junos:commit-localtime="2024-09-11 07:30:43 UTC" junos:commit-user="admin">
            <interfaces>
                <interface>
                    <name>ge-0/0/1</name>
                    <unit>
                        <name>0</name>
                        <family>
                            <inet>
                                <address>
                                    <name>20.1.1.1/30</name>
                                </address>
                            </inet>
                        </family>
                    </unit>
                </interface>
            </interfaces>
    </configuration>
    <cli>
        <banner></banner>
    </cli>
</rpc-reply>


Post check:

We have added the description test for the interface ge-0/0/1

admin@R1> show configuration interfaces ge-0/0/1|display xml 
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/18.3R1/junos">
    <configuration junos:commit-seconds="1726039843" junos:commit-localtime="2024-09-11 07:30:43 UTC" junos:commit-user="admin">
            <interfaces>
                <interface>
                    <name>ge-0/0/1</name>
                    <description>test</description>
                    <unit>
                        <name>0</name>
                        <family>
                            <inet>
                                <address>
                                    <name>20.1.1.1/24</name>
                                </address>
                            </inet>
                        </family>
                    </unit>
                </interface>
            </interfaces>
    </configuration>
    <cli>
        <banner></banner>
    </cli>
</rpc-reply>


'''