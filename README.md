# IsPhishable

# Introduction to Phishing
Phishing is a type of cyber attack that aims to trick people into divulging sensitive information such as usernames, passwords, and credit card details. Phishing attacks typically involve sending an email or a message that looks like it came from a trustworthy source, such as a bank, social media platform, or an online retailer. The email usually contains a link to a fake website that looks like the legitimate one, where users are prompted to enter their personal information. Phishing attacks can be difficult to spot, and even tech-savvy users can fall victim to them.

# What the Script Does
This script that can help you identify whether a domain is susceptible to spoofing, which is a common technique used in phishing attacks. Spoofing involves sending an email or a message that appears to come from a trusted source, but is actually sent from a different domain or email address.

The script checks whether a domain has DMARC (Domain-based Message Authentication, Reporting and Conformance) and SPF (Sender Policy Framework) records. These records are used to verify that an email message is actually sent from the domain it claims to be from. If a domain has DMARC and SPF records, it is less susceptible to spoofing and phishing attacks.

Using this script, you can quickly check whether a domain is properly configured to prevent spoofing and phishing attacks, which can help you stay safe online.

There's a bash and a python script version. They do the same thing!

# Usage
The script can be run on a domain by executing the command `./IsPhishable.sh example.com` or `./IsPhishable.py example.com`, where example.com is the domain you want to check. The script will then display whether the domain has DMARC and SPF records or not. If a record is found, the script will display a message in green, indicating that the domain is less susceptible to spoofing and phishing attacks. If no record is found, the script will display a message in red, indicating that the domain may be vulnerable to spoofing and phishing attacks.

# Shell version

- Dependencies
  - dig

# Python version
- Dependencies
- Version >= 3.7
  - `pip3 install -r requirements`
