import glob
import ipaddress
from collections import Counter
from datetime import datetime, timezone

ipv4_prefix = 24
ipv6_prefix = 50
ipv4_merge_count = 3
ipv6_merge_count = 3

header = """# PBH-BTN/BTN-Collected-Rules, Licensed under CC-BY 4.0. Generated at {time}.
# [START] Auto merged CIDR - IPV4: {ipv4_prefix}, IPV6: {ipv6_prefix}

"""

_START_ = "---START---"
_END_ = "---END---"

ipv4_blocklist = Counter()
ipv6_blocklist = Counter()
ipv4_prefix_counter = Counter()
ipv6_prefix_counter = Counter()

comments_block = {} # ip:[块注释]
comments_line = {} # ip:[行注释]

def parse_line(l):
    line = l.strip()
    if len(line) <= 2:
        return None, None, None
    if line.startswith("#"):
        return line, None, None
    if not "#" in line:
        return line, ipaddress.ip_network(line, strict=True), None
    else:
        mark = line.find("#")
        return line, ipaddress.ip_network(line[:mark].strip(), strict=True), line[mark:]

def find_comments_block(new_ip, full=False):
    if not full and new_ip in comments_block:
        return comments_block[new_ip], [new_ip]
    blocks = []
    ips = i_include_which(new_ip, comments_block)
    for ip in ips:
        for comment in comments_block[ip]:
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

def add_comment(ip,comment_block,comment_multi_line):
    if not ip in comments_block:
        comments_block[ip] = []
    if not comment_block in comments_block[ip]:
        comments_block[ip].append(comment_block)
    
    if not ip in comments_line:
        comments_line[ip] = []
    comments_line[ip] += comment_multi_line

for name in glob.glob("*.txt"):
    with open(name, encoding='utf-8') as f:
        file_comment_block = "# " + name
        comment_block = file_comment_block
        comment_multi_line = []
        for l in f:
            line, ip, comment = parse_line(l)
            if not line:
                continue
            if not ip:
                if _START_ in line:
                    comment_block = "# " + line[line.index(_START_)+len(_START_):].strip()
                    comment_multi_line = []
                elif _END_ in line:
                    comment_block = file_comment_block
                    comment_multi_line = []
                else:
                    comment_multi_line.append(line)
                continue
            if comment:
                comment_multi_line.append(comment)
            if ip.version == 6 and ip.network_address.ipv4_mapped:
                ipv6_blocklist[ip] += 1
                add_comment(ip,comment_block,comment_multi_line)
                ip = ipaddress.ip_network(ip.network_address.ipv4_mapped)
            if ip.version == 4:
                ipv4_blocklist[ip] += 1
                prefix = ipaddress.ip_network((ip.network_address, ipv4_prefix), strict=False)
                ipv4_prefix_counter[prefix] += 1
            else:
                ipv6_blocklist[ip] += 1
                prefix = ipaddress.ip_network((ip.network_address, ipv6_prefix), strict=False)
                ipv6_prefix_counter[prefix] += 1
            add_comment(ip,comment_block,comment_multi_line)
            comment_multi_line = []

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
added = list(set(collapsed) - set(comments_block.keys()))
deleted = list(set(comments_block.keys()) - set(collapsed))

comments_block_new = {}

for old_ip in deleted:
    ip = which_have_me(old_ip, collapsed)
    if not ip in added:
        added.append(ip)

for ip in collapsed:
    blocks, ips = find_comments_block(ip, ip in added)
    new_comment_block = blocks[0]
    if len(blocks) >= 2:
        new_comment_block = "# [Merged Comment]\n" + "\n".join(blocks)
    if not new_comment_block in comments_block_new:
        comments_block_new[new_comment_block] = []
    
    ip_str = str(ip.network_address) if (ip.version == 4 and ip.prefixlen == 32) or (ip.version == 6 and ip.prefixlen == 128) else str(ip)
    comment_multi_line = []
    for old_ip in ips:
        if old_ip in comments_line:
            comment_multi_line += comments_line[old_ip]
    if len(comment_multi_line):
        ip_str = "\n".join({}.fromkeys(comment_multi_line).keys()) + "\n" + ip_str
    comments_block_new[new_comment_block].append(ip_str)

with open("combine/all.txt", "w", encoding='utf-8') as f:
    f.write(header.format(time=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z'), ipv4_prefix=ipv4_prefix, ipv6_prefix=ipv6_prefix))
    for comment_block in comments_block_new:
        for new_ip in comments_block_new[comment_block]:
            f.write(comment_block)
            f.write("\n")
            f.write(new_ip)
            f.write("\n")
        f.write("\n")
