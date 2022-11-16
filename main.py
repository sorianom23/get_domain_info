import whois

def get_domain_info(link):
    
    try:
        domain_info = whois.whois(link)
        return domain_info
    except:
        return f"{link} not found"

domain_info = get_domain_info("thehouseofdrew.com")
print(domain_info)