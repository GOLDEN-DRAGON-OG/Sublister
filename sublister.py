import requests
from colorama import Fore, Style

def print_banner():
    print("""
███████╗██╗   ██╗██████╗ ██╗     ██╗███████╗████████╗███████╗██████╗ 
██╔════╝██║   ██║██╔══██╗██║     ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗
███████╗██║   ██║██████╔╝██║     ██║███████╗   ██║   █████╗  ██████╔╝
╚════██║██║   ██║██╔══██╗██║     ██║╚════██║   ██║   ██╔══╝  ██╔══██╗
███████║╚██████╔╝██████╔╝███████╗██║███████║   ██║   ███████╗██║  ██║
╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

    """)

def print_heading(text):
    length = len(text) + 4
    print(Fore.RED + "=" * length)
    print(Fore.RED + "| " + text + " |")
    print(Fore.RED + "=" * length)
    print(Style.RESET_ALL)

def print_square(text):
    print(Fore.BLUE + "[" + text + "]")
    print(Style.RESET_ALL)

def find_subdomains(domain):
    url = f"https://crt.sh/?q={domain}&output=json"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            subdomains = []
            for item in data:
                subdomain = item.get('name_value')
                if subdomain.endswith(f".{domain}"):
                    subdomains.append(subdomain)
            return sorted(set(subdomains))
        else:
            print(Fore.RED + "Failed to retrieve subdomains. Please try again later." + Style.RESET_ALL)
            return []
    except requests.exceptions.RequestException as e:
        print(Fore.RED + "An error occurred while retrieving subdomains:", e + Style.RESET_ALL)
        return []

# Call the banner function
print_banner()

# User input for the domain
domain = input("Enter the domain to find subdomains: ")

# Call the subdomain lister function
subdomains = find_subdomains(domain)

# Print the heading and square
print_heading("Active Subdomain Lister")
print_square("Developed by: Golden Dragon")

# Print the subdomains
if subdomains:
    print(Fore.GREEN + "Active subdomains found:" + Style.RESET_ALL)
    for subdomain in subdomains:
        print(Fore.YELLOW + subdomain + Style.RESET_ALL)
else:
    print(Fore.RED + "No active subdomains found." + Style.RESET_ALL)

