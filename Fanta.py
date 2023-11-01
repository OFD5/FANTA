import requests
import json

# Banner text with color
banner = f"""
\033[1;32m----------------------------------------------
\033[1;32m███████╗ █████╗ ███╗   ██████████╗ █████╗ 
\033[1;32m██╔════╝██╔══██╗████╗  ██║\033[1;31m╚═██╔══╝██╔══██╗
\033[1;32m█████╗  ███████║██╔██╗ ██║\033[1;32m  ██║   ███████║
\033[1;32m██╔══╝  ██╔══██║██║╚██╗██║\033[1;31m  ██║   ██╔══██║
\033[1;32m██║     ██║  ██║██║ ╚████║\033[1;32m  ██║   ██║  ██║
\033[1;32m╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝\033[1;31m  ╚═╝   ╚═╝  ╚═╝
                                    \033[1;36mAuthour: OFD5

                \033[1;34mSafepayload.co.za

\033[1;36mSecurityTrails Subdomain Retrieval Tool
\033[1;32mFollow me On https://github.com/OFD5
\033[1;32mThis tool is provided for enhancement of OSINT during Penetration testing.
\033[1;35mUse with caution. You are responsible for your actions.
\033[1;32mDevelopers assume no liability and are not responsible for any misuse or damage.
\033[1;31mAlways ensure that you have proper authorization to access and collect information about individuals or entities.
----------------------------------------------
\033[0m"""

print(banner)

domain = input("Please enter your domain name e.g example.com :  ")

# Hardcoded API key (replace 'YOUR_API_KEY' with your actual API key)
apiKey = ""

print("\n")

while True:
    if not domain:
        domain = input("Please enter your domain name :  ")
    else:
        break

url = "https://api.securitytrails.com/v1/domain/" + domain + "/subdomains?children_only=false&include_inactive=true"
headers = {
    "accept": "application/json",
    "APIKEY": apiKey
}

response = requests.get(url, headers=headers)

data = response.json()

count = 0
with open(f'subdomains_{domain}.txt', 'w') as f:
    for subdomains in data['subdomains']:
        subdomain = subdomains + "." + domain
        print(subdomain)
        f.write(subdomain + "\n")
        count += 1

print("\nsubdomains count: " + str(count))
print(f"Subdomains saved to subdomains_{domain}.txt")
