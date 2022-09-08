from . import etc_hosts_check
import hashlib

def check_content_hash(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest();
