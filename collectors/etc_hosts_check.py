from typing import Tuple
from collector_registry import general_collector
import collectors

@general_collector()
def check_etc_host() -> Tuple[str, str]:
    etc_host_file = open("/etc/hosts")
    etc_hosts_content = etc_host_file.read()
    hash = collectors.check_content_hash(etc_hosts_content)
    etc_host_file.close()
    return (hash, etc_hosts_content)
