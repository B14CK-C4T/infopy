import argparse
import requests
import yaml
import json


<<<<<<< HEAD
=======
def save_file(path, data):
    with open(path, 'a') as file:
        for lines in data:
            file.writelines(lines)
            file.write("\n")


>>>>>>> master
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
<<<<<<< HEAD
=======
    parser.add_argument("-o", type=str, help="save output")
>>>>>>> master
    args = parser.parse_args()

    domain = args.d  # get domain name
    config = load_key("config.yaml")
    api_key = config.get('apikey')
<<<<<<< HEAD
=======
    save_file_name = args.o  # get save file name
>>>>>>> master

    if args.whois:
        url = f"https://api.securitytrails.com/v1/domain/{
            domain}/whois?apikey={api_key}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        data = response.json()
        if "message" in json.dumps(data):
            print("[!]", data.get("message"))
        else:
<<<<<<< HEAD
            print(json.dumps(data, intent=2))
=======
            whois_data = json.dumps(data, indent=2)
            print(whois_data)
            # print(json.dumps(data, intent=2))
            # whois_data = data.get("<set_keys>") #this part is not tested yet
            # bcz of the free tire API key
            if save_file_name:
                save_file(save_file_name, whois_data)
            else:
                pass
>>>>>>> master

    elif args.sub:
        url = f"https://api.securitytrails.com/v1/domain/{
            domain}/subdomains?apikey={api_key}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
<<<<<<< HEAD
        # filtering response
        data = response.json()
        for x in data.get("subdomains"):
            print(f"{x}")  # it print subdomains only
        print("[-] total subdomains:", data.get("subdomain_count"))

=======
        sub_data = []  # create empty list to store data for saving this output
        # filtering response
        data = response.json()
        for x in data.get("subdomains"):
            sub_data.append(x)
            print(f"{x}")  # it print subdomains only
        print("[-] total subdomains:", data.get("subdomain_count"))

        if save_file_name:  # if -o True then this save -
            # process run otherwise pass
            save_file(save_file_name, sub_data)
        else:
            pass

>>>>>>> master

if __name__ == "__main__":
    main()
