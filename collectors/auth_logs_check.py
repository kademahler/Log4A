from typing import Tuple
from collector_registry import general_collector
import collectors

@general_collector()
def check_auth_logs() -> Tuple[str, str]:
    auth_logs_file = open("/var/log/auth.log")
    auth_logs_content = auth_logs_file.read()
    hash = collectors.check_content_hash(auth_logs_content)
    auth_logs_file.close()
    return (hash, auth_logs_content)
    