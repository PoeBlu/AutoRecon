import nmap
import optparse
import subprocess

ps = nmap.PortScanner()
def runScan(ipAddress):
    return ps.scan(ipAddress, '1-1024', '-sV -A')

def getPorts(scanResults):
    portsDict = []
    hosts = scanResults['scan'].keys()
    for host in hosts:
        ports = scanResults['scan'][host]['tcp'].keys()
        portsDict.append({host: list(ports)})
    return portsDict


def main():
    parser = optparse.OptionParser('usage%prog -a <ip address>')
    parser.add_option('-a', dest='ipaddress', type='string', help='provide ip address')
    (options, args) = parser.parse_args()
    if options.ipaddress == None:
    	print parser.usage
	exit()
    ipaddress = options.ipaddress
    results = runScan(ipaddress)
    portsList = getPorts(results)
    for i in portsList:
	hosts = i.keys()
	for host in hosts:
		print 'host: {}'.format(host)
		ports = i[host]
		for port in ports:
			portInfo = results['scan'][host]['tcp'][port]
			product = portInfo['product']
			state = portInfo['state']
			version = portInfo['version']
			name = portInfo['name']
			print 'port: {}\nproduct: {}\nstate: {}\nversion: {}\nname: {}'.format(port, product, state, version, name)
			print '\n'
   		if 80 in ports or 443 in ports:
			print '=' * 50
			print 'running nikto scan'
			subprocess.call(['nikto', '-h', 'http://192.168.1.1'])
			print '=' * 50
			print 'scan ended'

if __name__ == '__main__':
    main()



