#!/usr/bin/env python3

import sys
import dns.resolver
from termcolor import colored

# Get the domain from the command line argument
if len(sys.argv) > 1:
    domain = sys.argv[1]
else:
    print("Please provide a domain name as an argument")
    sys.exit(1)

# Check for DMARC record
try:
    dmarc_record = dns.resolver.resolve('_dmarc.' + domain, 'TXT')
    dmarc_record = next((str(r.strings[0]) for r in dmarc_record if r.strings[0].startswith(b'v=DMARC1;')), None)
except dns.exception.DNSException:
    dmarc_record = None

if dmarc_record:
    print(colored(f"DMARC record found for {domain}", "green"))
else:
    print(colored(f"No DMARC record found for {domain}", "red"))

# Check for SPF record
try:
    spf_record = dns.resolver.resolve(domain, 'TXT')
    spf_record = next((str(r.strings[0]) for r in spf_record if r.strings[0].startswith(b'v=spf1 ')), None)
except dns.exception.DNSException:
    spf_record = None

if spf_record:
    print(colored(f"SPF record found for {domain}", "green"))
else:
    print(colored(f"No SPF record found for {domain}", "red"))

print("=====================================")
print(dmarc_record)
print(spf_record)
