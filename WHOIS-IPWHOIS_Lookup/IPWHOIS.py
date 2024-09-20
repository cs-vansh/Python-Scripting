from ipwhois import IPWhois

def perform_ip_whois(ip_address):
	try:
		ip=IPWhois(ip_address)
		ip_info = ip.lookup_rdap()
		print(ip_info)
	except Exception as e:
		print("Error:", e)

if __name__ =="__main__":
	ip_address="142.251.214.142"	#IP address to lookup
	perform_ip_whois(ip_address)
