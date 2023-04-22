#!/usr/bin/env python3

import sys
import subprocess
from termcolor import colored

# Get the domain from the command line argument
if len(sys.argv) > 1:
    domain = sys.argv[1]
else:
    print("Please provide a domain name as an argument")
    sys.exit(1)

# Check for DMARC record
dmarc_record = subprocess.check_output(["dig", "+short", "TXT", "_dmarc." + domain]).decode()
dmarc_record = next((line for line in dmarc_record.split("\n") if line.startswith('"v=DMARC1;')), None)
if dmarc_record:
    print(colored(f"DMARC record found for {domain}", "green"))
else:
    print(colored(f"No DMARC record found for {domain}", "red"))

# Check for SPF record
spf_record = subprocess.check_output(["dig", "+short", "TXT", domain]).decode()
spf_record = next((line for line in spf_record.split("\n") if line.startswith('"v=spf1 ')), None)
if spf_record:
    print(colored(f"SPF record found for {domain}", "green"))
else:
    print(colored(f"No SPF record found for {domain}", "red"))

print("=====================================")
print(dmarc_record)
print(spf_record)
