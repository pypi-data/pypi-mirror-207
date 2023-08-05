# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .database import *
from .dns_domain_name import *
from .dns_domain_record import *
from .firewall import *
from .firewall_rule import *
from .get_database import *
from .get_disk_image import *
from .get_dns_domain_name import *
from .get_dns_domain_record import *
from .get_firewall import *
from .get_instance import *
from .get_instances import *
from .get_instances_size import *
from .get_kubernetes_cluster import *
from .get_kubernetes_version import *
from .get_load_balancer import *
from .get_network import *
from .get_object_store import *
from .get_object_store_credential import *
from .get_region import *
from .get_reserved_ip import *
from .get_size import *
from .get_ssh_key import *
from .get_volume import *
from .instance import *
from .instance_reserved_ip_assignment import *
from .kubernetes_cluster import *
from .kubernetes_node_pool import *
from .network import *
from .object_store import *
from .object_store_credential import *
from .provider import *
from .reserved_ip import *
from .ssh_key import *
from .volume import *
from .volume_attachment import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_civo.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumi_civo.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "civo",
  "mod": "index/database",
  "fqn": "pulumi_civo",
  "classes": {
   "civo:index/database:Database": "Database"
  }
 },
 {
  "pkg": "civo",
  "mod": "index/dnsDomainName",
  "fqn": "pulumi_civo",
  "classes": {
   "civo:index/dnsDomainName:DnsDomainName": "DnsDomainName"
  }
 },
 {
  "pkg": "civo",
  "mod": "index/dnsDomainRecord",
  "fqn": "pulumi_civo",
  "classes": {
   "civo:index/dnsDomainRecord:DnsDomainRecord": "DnsDomainRecord"
  }
 },
 {
  "pkg": "civo",
  "mod": "index/firewall",
  "fqn": "pulumi_civo",
  "classes": {
   "civo:index/firewall:Firewall": "Firewall"
  }
 },
 {
  "pkg": "civo",
  "mod": "index/firewallRule",
  "fqn": "pulumi_civo",
  "classes": {
   "civo:index/firewallRule:FirewallRule": "FirewallRule"
  }
 },
 {
  "pkg": "civo",
  "mod": "index/instance",
  "fqn": "pulumi_civo",
  "classes": {
   "civo:index/instance:Instance": "Instance"
  }
 },
 {
  "pkg": "civo",
  "mod": "index/instanceReservedIpAssignment",
  "fqn": "pulumi_civo",
  "classes": {
   "civo:index/instanceReservedIpAssignment:InstanceReservedIpAssignment": "InstanceReservedIpAssignment"
  }
 },
 {
  "pkg": "civo",
  "mod": "index/kubernetesCluster",
  "fqn": "pulumi_civo",
  "classes": {
   "civo:index/kubernetesCluster:KubernetesCluster": "KubernetesCluster"
  }
 },
 {
  "pkg": "civo",
  "mod": "index/kubernetesNodePool",
  "fqn": "pulumi_civo",
  "classes": {
   "civo:index/kubernetesNodePool:KubernetesNodePool": "KubernetesNodePool"
  }
 },
 {
  "pkg": "civo",
  "mod": "index/network",
  "fqn": "pulumi_civo",
  "classes": {
   "civo:index/network:Network": "Network"
  }
 },
 {
  "pkg": "civo",
  "mod": "index/objectStore",
  "fqn": "pulumi_civo",
  "classes": {
   "civo:index/objectStore:ObjectStore": "ObjectStore"
  }
 },
 {
  "pkg": "civo",
  "mod": "index/objectStoreCredential",
  "fqn": "pulumi_civo",
  "classes": {
   "civo:index/objectStoreCredential:ObjectStoreCredential": "ObjectStoreCredential"
  }
 },
 {
  "pkg": "civo",
  "mod": "index/reservedIp",
  "fqn": "pulumi_civo",
  "classes": {
   "civo:index/reservedIp:ReservedIp": "ReservedIp"
  }
 },
 {
  "pkg": "civo",
  "mod": "index/sshKey",
  "fqn": "pulumi_civo",
  "classes": {
   "civo:index/sshKey:SshKey": "SshKey"
  }
 },
 {
  "pkg": "civo",
  "mod": "index/volume",
  "fqn": "pulumi_civo",
  "classes": {
   "civo:index/volume:Volume": "Volume"
  }
 },
 {
  "pkg": "civo",
  "mod": "index/volumeAttachment",
  "fqn": "pulumi_civo",
  "classes": {
   "civo:index/volumeAttachment:VolumeAttachment": "VolumeAttachment"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "civo",
  "token": "pulumi:providers:civo",
  "fqn": "pulumi_civo",
  "class": "Provider"
 }
]
"""
)
