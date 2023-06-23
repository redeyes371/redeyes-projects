import socket

# Define the target host and the range of ports to scan
target_host = input("Enter a target host to scan: ")
start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

# Loop through the specified range of ports and attempt to connect to each one
for port in range(start_port, end_port+1):
    try:
        # Create a new socket object and attempt to connect to the target host and port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target_host, port))

        # If the connection is successful, report back on the open port and service
        if result == 0:
            print(f"Port {port} is open - {socket.getservbyport(port)}")

        # Close the socket connection
        sock.close()

    # Handle any exceptions that occur during the scan
    except socket.error:
        print(f"Could not connect to port {port}")