from typing import Tuple
from collector_registry import general_collector
import collectors

@general_collector()
def check_auth_logs() -> Tuple[str, str]:
    user_logs_file = open("/var/log/user.log")
    user_logs_content = user_logs_file.read()
    hash = collectors.check_content_hash(user_logs_content)
    user_logs_file.close()
    return (hash, user_logs_content)
    