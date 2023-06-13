import nmap

def scan_ip(ip_address):
    scanner = nmap.PortScanner()
    scanner.scan(ip_address, arguments='-sS')

    results = []

    for host in scanner.all_hosts():
        if scanner[host].state() == 'up':
            result = f"Host: {host}\n"

            for proto in scanner[host].all_protocols():
                if proto == 'tcp':
                    ports = scanner[host][proto].keys()
                    for port in ports:
                        state = scanner[host][proto][port]['state']
                        service = scanner[host][proto][port]['name']
                        result += f"Port: {port}\tState: {state}\tService: {service}\n"

            os = scanner[host]['osmatch'][0]['name']
            result += f"Operating System: {os}\n"

            results.append(result)

    return results

def save_results(results, filename):
    with open(filename, 'w') as file:
        for result in results:
            file.write(result)
            file.write('\n')

ip_address = input("Enter the IP address to scan: ")
results = scan_ip(ip_address)
filename = input("Enter the filename to save the results: ")
save_results(results, filename)
