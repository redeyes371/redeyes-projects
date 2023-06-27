#!/bin/bash
# Ask the user to enter an IP address or a range
echo "Enter an IP address or a range to scan with nmap:"
read ip
# Run nmap with the given IP address or range and save the output to a file
nmap -sV $ip > scan.txt
# Display the content of the file
cat scan.txt
