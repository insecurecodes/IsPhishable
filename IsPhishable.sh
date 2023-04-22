#!/bin/bash

# Set the domain to check
domain=$1

# Check for DMARC record
dmarc_record=$(dig +short TXT _dmarc.$1 | grep -E '^"v=DMARC1;')
if [ -n "$dmarc_record" ]; then
    echo -e "\033[32mDMARC record found for $1\033[0m"
else
    echo -e "\033[31mNo DMARC record found for $1\033[0m"
fi

# Check for SPF record
spf_record=$(dig +short TXT $1 | grep -E '^"v=spf1 ')
if [ -n "$spf_record" ]; then
    echo -e "\033[32mSPF record found for $1\033[0m"
else
    echo -e "\033[31mNo SPF record found for $1\033[0m"
fi

echo "====================================="
echo "$dmarc_record"
echo "$spf_record"
