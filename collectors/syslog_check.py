from typing import Tuple
from collector_registry import general_collector
import collectors

@general_collector()
def check_syslog() -> Tuple[str, str]:
    syslog_file = open("/var/log/syslog")
    syslog_content = syslog_file.read()
    hash = collectors.check_content_hash(syslog_content)
    syslog_file.close()
    return (hash, syslog_content)
