import glob
import ipaddress
from collections import Counter
from datetime import datetime, timezone

ipv4_prefix = 24
ipv6_prefix = 56
ipv4_merge_count = 3
ipv6_merge_count = 3

header = """# PBH-BTN/BTN-Collected-Rules, Licensed under CC-BY 4.0. Generated at {time}.
# [START] Auto merged CIDR - IPV4: {ipv4_prefix}, IPV6: {ipv6_prefix}
"""

ipv4_blocklist = Counter()
ipv6_blocklist = Counter()
ipv4_prefix_counter = Counter()
ipv6_prefix_counter = Counter()

for name in glob.glob("*.txt"):
    with open(name, encoding='utf-8') as f:
        for l in f:
            line = l.strip()
            if line.startswith("#") or len(line) <= 2:
                continue
            ip = ipaddress.ip_network(line, strict=False)
            
            if ip.version == 4:
                ipv4_blocklist[str(ip)] += 1
                prefix = ipaddress.ip_network((ip.network_address, ipv4_prefix), strict=False)
                ipv4_prefix_counter[str(prefix)] += 1
            else:
                ipv6_blocklist[str(ip)] += 1
                prefix = ipaddress.ip_network((ip.network_address, ipv6_prefix), strict=False)
                ipv6_prefix_counter[str(prefix)] += 1

for ip, count in ipv4_prefix_counter.most_common():
    if count >= ipv4_merge_count:
        ipv4_blocklist[ip] += count
    else:
        break

for ip, count in ipv6_prefix_counter.most_common():
    if count >= ipv6_merge_count:
        ipv6_blocklist[ip] += count
    else:
        break

with open("combine/all.txt", "w", encoding='utf-8') as f:
    f.write(header.format(time=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z'), ipv4_prefix=ipv4_prefix, ipv6_prefix=ipv6_prefix))

    for ip in ipaddress.collapse_addresses([ipaddress.ip_network(x) for x in ipv4_blocklist]):
        f.write(str(ip.network_address) if ip.prefixlen == 32 else str(ip))
        f.write("\n")
    for ip in ipaddress.collapse_addresses([ipaddress.ip_network(x) for x in ipv6_blocklist]):
        f.write(str(ip.network_address) if ip.prefixlen == 128 else str(ip))
        f.write("\n")
