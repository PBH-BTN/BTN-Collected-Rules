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

comment_blocks = {}
comments_single = {}

def parse_line(l):
    line = l.strip()
    if len(line) <= 2:
        return None, None, None
    if line.startswith("#"):
        return line, None, None
    if not "#" in line:
        return line, ipaddress.ip_network(line, strict=False), None
    else:
        mark = line.find("#")
        return line, ipaddress.ip_network(line[:mark].strip(), strict=False), line[mark:]

def find_comment_blocks(new_ip, full=False):
    if not full and new_ip in comment_blocks:
        return comment_blocks[new_ip], [new_ip]
    blocks = []
    ips = i_include_which(new_ip, comment_blocks)
    for ip in ips:
        for comment in comment_blocks[ip]:
            if not comment in blocks:
                blocks.append(comment)
    return blocks, ips

def i_include_which(new_ip, ip_list):
    ips = []
    for ip in ip_list:
        if ip == new_ip or (ip.version == new_ip.version and ip.subnet_of(new_ip)):
            ips.append(ip)
    return ips

def which_have_me(new_ip, ip_list):
    for ip in ip_list:
        if ip.version == new_ip.version and new_ip.subnet_of(ip):
            return ip
    return None

for name in glob.glob("*.txt"):
    with open(name, encoding='utf-8') as f:
        comment_block = "# " + name
        for l in f:
            line, ip, comment = parse_line(l)
            if not line:
                continue
            if not ip:
                comment_block = line
                continue
            
            if ip.version == 4:
                ipv4_blocklist[ip] += 1
                prefix = ipaddress.ip_network((ip.network_address, ipv4_prefix), strict=False)
                ipv4_prefix_counter[prefix] += 1
            else:
                ipv6_blocklist[ip] += 1
                prefix = ipaddress.ip_network((ip.network_address, ipv6_prefix), strict=False)
                ipv6_prefix_counter[prefix] += 1
            
            if not ip in comment_blocks:
                comment_blocks[ip] = []
            comment_blocks[ip].append(comment_block)
            if comment:
                if not ip in comments_single:
                    comments_single[ip] = []
                comments_single[ip].append(comment)

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

collapsed = list(ipaddress.collapse_addresses(ipv4_blocklist)) + list(ipaddress.collapse_addresses(ipv6_blocklist))
added = list(set(collapsed) - set(comment_blocks.keys()))
deleted = list(set(comment_blocks.keys()) - set(collapsed))

comment_blocks_new = {}

for old_ip in deleted:
    ip = which_have_me(old_ip, collapsed)
    if not ip in added:
        added.append(ip)

for ip in collapsed:
    blocks, ips = find_comment_blocks(ip, ip in added)
    new_comment_block = blocks[0]
    if len(blocks) >= 2:
        new_comment_block = "# [Merged Comment]\n" + "\n".join(blocks)
    if not new_comment_block in comment_blocks_new:
        comment_blocks_new[new_comment_block] = []
    
    ip_str = str(ip.network_address) if (ip.version == 4 and ip.prefixlen == 32) or (ip.version == 6 and ip.prefixlen == 128) else str(ip)
    comment_single_new = []
    for old_ip in ips:
        if old_ip in comments_single:
            comment_single_new += comments_single[old_ip]
    if len(comment_single_new):
        ip_str += " " + " ".join(comment_single_new)
    comment_blocks_new[new_comment_block].append(ip_str)

with open("combine/all.txt", "w", encoding='utf-8') as f:
    f.write(header.format(time=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z'), ipv4_prefix=ipv4_prefix, ipv6_prefix=ipv6_prefix))
    for comment_block in comment_blocks_new:
        f.write(comment_block)
        f.write("\n")
        f.write("\n".join(comment_blocks_new[comment_block]))
        f.write("\n\n")
