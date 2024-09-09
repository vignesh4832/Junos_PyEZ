from jnpr.junos import Device
import jnpr.junos.facts
from pprint import pprint

device= "10.20.1.1"
user = "admin"
password = "admin"

dev = Device(host=device, user=user, password=password, gather_facts=False)
dev.open()
pprint(dev.facts["hostname"])
pprint(dev.facts)
dev.close()


''' 
Output taken from Junos vlab 

Output for dev.facts["hostname"]

'R1' 

Output for dev.facts

{'2RE': False,
 'HOME': '/var/home/jcluser',
 'RE0': {'last_reboot_reason': 'Router rebooted after a normal shutdown.',
         'mastership_state': 'master',
         'model': 'RE-VMX',
         'status': 'OK',
         'up_time': '1 hour, 31 minutes, 2 seconds'},
 'RE1': None,
 'RE_hw_mi': False,
 'current_re': ['re0', 'master', 'node', 'fwdd', 'member', 'pfem'],
 'domain': None,
 'fqdn': 'R1',
 'hostname': 'R1',
 'hostname_info': {'re0': 'R1'},
 'ifd_style': 'CLASSIC',
 'junos_info': {'re0': {'object': junos.version_info(major=(18, 3), type=R, minor=1, build=9),
                        'text': '18.3R1.9'}},
 'master': 'RE0',
 'model': 'VMX',
 'model_info': {'re0': 'VMX'},
 'personality': 'MX',
 're_info': {'default': {'0': {'last_reboot_reason': 'Router rebooted after a '
                                                     'normal shutdown.',
                               'mastership_state': 'master',
                               'model': 'RE-VMX',
                               'status': 'OK'},
                         'default': {'last_reboot_reason': 'Router rebooted '
                                                           'after a normal '
                                                           'shutdown.',
                                     'mastership_state': 'master',
                                     'model': 'RE-VMX',
                                     'status': 'OK'}}},
 're_master': {'default': '0'},
 'serialnumber': 'VM66DF5123C1',
 'srx_cluster': None,
 'srx_cluster_id': None,
 'srx_cluster_redundancy_group': None,
 'switch_style': 'BRIDGE_DOMAIN',
 'vc_capable': False,
 'vc_fabric': None,
 'vc_master': None,
 'vc_mode': None,
 'version': '18.3R1.9',
 'version_RE0': '18.3R1.9',
 'version_RE1': None,
 'version_info': junos.version_info(major=(18, 3), type=R, minor=1, build=9),
 'virtual': True}

 '''