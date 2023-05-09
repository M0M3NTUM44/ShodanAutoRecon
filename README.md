# ShodanAutoRecon
Using Shodan API to automate Recon processes of a Red Team

## Dependencies
---
'''
pip3 install shodan
'''
## Usage
---
-A [Shodan API key] -n [HOSTNAME] -ip [IPv4] -ip6 [IPv6]
-n / --hostname = Target host name (can also be multipul hostnames)
-ip / --ipv4 = Target IPv4 Address (can also be multipul addresses)
-ip6 / --ipv6 = Target IPv6 Address (can also be multipul addresses)
-A / --API = Shodan API key (Requierd)

### Example
---
python3 ./ShodanAutoRecon.py -A "2f497af0d0507de98229" -ip 8.8.8.8

python3 ./ShodanAutoRecon.py -A "2f497af0d0507de98229" -n www.target.com vpn.target.com
