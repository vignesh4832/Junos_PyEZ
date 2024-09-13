from jnpr.junos import Device
from lxml import etree   

device= "10.12.1.1"
user = "admin"
password = "admin123"


dev = Device(host=device, user=user, password=password, gather_facts=False)

dev.open()
data = dev.rpc.get_bgp_neighbor_information() # We can pull this info from "show bgp summary | display xml rpc"
print (etree.tostring(data, encoding='unicode', pretty_print=True)) 
dev.close()  

'''

admin@R1> show bgp summary 
Groups: 2 Peers: 2 Down peers: 0
Table          Tot Paths  Act Paths Suppressed    History Damp State    Pending
inet.0               
                       0          0          0          0          0          0
Peer                     AS      InPkt     OutPkt    OutQ   Flaps Last Up/Dwn State|#Active/Received/Accepted/Damped...
172.16.1.2            65001         27         26       0       0       10:59 0/0/0/0              0/0/0/0
172.16.2.2            65002         27         26       0       0       10:55 0/0/0/0              0/0/0/0


admin@R1> show bgp summary | display xml rpc 
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/18.3R1/junos">
    <rpc>
        <get-bgp-summary-information>
        </get-bgp-summary-information>
    </rpc>
    <cli>
        <banner></banner>
    </cli>
</rpc-reply>

Output from the script:

<rpc-reply xmlns:junos="http://xml.juniper.net/junos/18.3R1/junos">
    <bgp-information xmlns="http://xml.juniper.net/junos/18.3R1/junos-routing">
        <bgp-peer junos:style="detail">
            <peer-address>172.16.1.1+179</peer-address>
            <peer-as>65001</peer-as>
            <local-address>172.16.1.2+50900</local-address>
            <local-as>65001</local-as>
            <peer-group>ibgp</peer-group>
            <peer-cfg-rti>master</peer-cfg-rti>
            <peer-fwd-rti>master</peer-fwd-rti>
            <peer-type>Internal</peer-type>
            <peer-state>Established</peer-state>
            <peer-flags>Sync</peer-flags>
            <last-state>OpenConfirm</last-state>
            <last-event>RecvKeepAlive</last-event>
            <last-error>None</last-error>
            <bgp-option-information xmlns="http://xml.juniper.net/junos/18.3R1/junos-routing">
                <bgp-options>Preference LocalAddress PeerAS LocalAS Refresh</bgp-options>
                <bgp-options2></bgp-options2>
                <bgp-options-extended></bgp-options-extended>
                <local-address>172.16.1.2</local-address>
                <holdtime>90</holdtime>
                <preference>170</preference>
                <local-as>65001</local-as>
                <local-system-as>0</local-system-as>
            </bgp-option-information>
            <flap-count>0</flap-count>
            <peer-id>100.123.1.0</peer-id>
            <local-id>100.123.1.1</local-id>
            <active-holdtime>90</active-holdtime>
            <keepalive-interval>30</keepalive-interval>
            <group-index>0</group-index>
            <peer-index>0</peer-index>
            <snmp-index>0</snmp-index>
            <bgp-peer-iosession>
                <iosession-thread-name>bgpio-0</iosession-thread-name>
                <iosession-state>Enabled</iosession-state>
            </bgp-peer-iosession>
            <bgp-bfd>
                <bfd-configuration-state>disabled</bfd-configuration-state>
                <bfd-operational-state>down</bfd-operational-state>
            </bgp-bfd>
            <peer-restart-nlri-configured>inet-unicast</peer-restart-nlri-configured>
            <nlri-type-peer>inet-unicast</nlri-type-peer>
            <nlri-type-session>inet-unicast</nlri-type-session>
            <peer-refresh-capability>2</peer-refresh-capability>
            <peer-stale-route-time-configured>300</peer-stale-route-time-configured>
            <peer-no-restart/>
            <peer-restart-flags-received>Notification</peer-restart-flags-received>
            <peer-restart-nlri-negotiated>inet-unicast</peer-restart-nlri-negotiated>
            <peer-end-of-rib-received>inet-unicast</peer-end-of-rib-received>
            <peer-end-of-rib-sent>inet-unicast</peer-end-of-rib-sent>
            <peer-end-of-rib-scheduled></peer-end-of-rib-scheduled>
            <peer-no-llgr-restarter/>
            <peer-4byte-as-capability-advertised>65001</peer-4byte-as-capability-advertised>
            <peer-addpath-not-supported/>
            <bgp-rib junos:style="detail">
                <name>inet.0</name>
                <rib-bit>20000</rib-bit>
                <bgp-rib-state>BGP restart is complete</bgp-rib-state>
                <send-state>in sync</send-state>
                <active-prefix-count>0</active-prefix-count>
                <received-prefix-count>0</received-prefix-count>
                <accepted-prefix-count>0</accepted-prefix-count>
                <suppressed-prefix-count>0</suppressed-prefix-count>
                <advertised-prefix-count>0</advertised-prefix-count>
            </bgp-rib>
            <last-received>9</last-received>
            <last-sent>9</last-sent>
            <last-checked>39</last-checked>
            <input-messages>3</input-messages>
            <input-updates>1</input-updates>
            <input-refreshes>0</input-refreshes>
            <input-octets>61</input-octets>
            <output-messages>3</output-messages>
            <output-updates>0</output-updates>
            <output-refreshes>0</output-refreshes>
            <output-octets>61</output-octets>
            <bgp-output-queue>
                <number>1</number>
                <count>0</count>
                <table-name>inet.0</table-name>
                <rib-adv-nlri>inet-unicast</rib-adv-nlri>
            </bgp-output-queue>
        </bgp-peer>
    </bgp-information>
    <cli>
        <banner></banner>
    </cli>
</rpc-reply>


'''