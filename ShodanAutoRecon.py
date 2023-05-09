import shodan
import argparse
from shodan import exception

# Define command-line argument parser

parser = argparse.ArgumentParser()

# -A [Shodan API key] -n [HOSTNAME] -ip [IPv4] -ip6 [IPv6]
parser.add_argument("-n", "--hostname", help="Target host name", nargs='+')
parser.add_argument("-ip", "--ipv4", help="Target IPv4 Address", nargs='+')
parser.add_argument("-ip6", "--ipv6", help="Target IPv6 Address", nargs='+')
parser.add_argument("-A", "--API", help= "Shodan API key", required=True)

args = parser.parse_args()

# shodan API key
SHODAN_API_KEY = args.API
api = shodan.Shodan(SHODAN_API_KEY)


# search results from hostname
def search_target_by_name(hostname):
    try:
        # Search Shodan
        results = api.search(hostname)

        # Print the results of Hostname API shodan Scan
        print("----------------------------------Results for {}----------------------------------".format(hostname))
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
            print('IP: {}'.format(result['ip_str']))
            print(result['data'])
            print('')
        # Error in API key
    except shodan.APIError as e:
        print('Error: {}'.format(e))


# search results from IPv4 address
def search_target_by_ip(ipv4):
    try:
        # Lookup the IPV4 Address
        host = api.host(ipv4)

        # Print the results of IPv4 API shodan Scan
        print("----------------------------------Results for {}----------------------------------".format(ipv4))
        print("""
                IP: {}
                Organization: {}
                Operating System: {}
            """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

        # Print all banners
        for item in host['data']:
            print("""
                        Port: {}
                        Banner: {}
    
                """.format(item['port'], item['data']))
    except shodan.APIError as e:
        print('Error: {}'.format(e))


if args.hostname is not None:
    for hostname in args.hostname:
        search_target_by_name(hostname)

if args.ipv4 is not None:
    for ipv4 in args.ipv4:
        search_target_by_name(ipv4)