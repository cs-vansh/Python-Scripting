# alternatively, in terminal directly use <whois domain_name>
import whois

def perform_whois_lookup(domain_name):
	try:
		whois_info = whois.whois(domain_name)
		print(whois_info)
		
	except Exception as e:
		print("Error:", e)
		
if __name__ == "__main__":
	domain_name="fast.com"	#Replace witht the Domain Name or IP of the domain to lookup
	perform_whois_lookup(domain_name)
	
 