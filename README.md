# AutoRecon
This script runs an nmap scan on a specified target and outputs the results. Also, if port 80 is found to be open it runs a nikto scan on that ip address.

NOTE:
DOES NOT WORK ON IP ADDRESS RANGES
DO NOT SCAN ANYTHING YOU ARE NOT AUTHORIZED TO

USAGE:
python autorecon.py -a '127.0.0.1'
python autorecon.py -a 'scanme.nmap.org'
