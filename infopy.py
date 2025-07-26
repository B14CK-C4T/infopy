import argparse
import requests
import yaml
import json


def load_key(path):
    # load key from config.yaml file
    try:
        with open(path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except yaml.YAMLError as e:
        print(e)
    except FileNotFoundError:
        print("[!] Error: The config.yaml file was not found.")


def main():
    # arguments
    parser = argparse.ArgumentParser(description="INFOPY")
    parser.add_argument("-d", required=True, type=str, help="domain name")
    parser.add_argument("--sub", action="store_true", help="subdomain finder")
    parser.add_argument("--whois", action="store_true", help="whois lookup")
    args = parser.parse_args()

    domain = args.d  # get domain name
    config = load_key("config.yaml")
    api_key = config.get('apikey')

    if args.whois:
        url = f"https://api.securitytrails.com/v1/domain/{
            domain}/whois?apikey={api_key}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        data = response.json()
        if "message" in json.dumps(data):
            print("[!]", data.get("message"))
        else:
            print(json.dumps(data, intent=2))

    elif args.sub:
        url = f"https://api.securitytrails.com/v1/domain/{
            domain}/subdomains?apikey={api_key}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        # filtering response
        data = response.json()
        for x in data.get("subdomains"):
            print(f"{x}")  # it print subdomains only
        print("[-] total subdomains:", data.get("subdomain_count"))


if __name__ == "__main__":
    main()
