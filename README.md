# FireHawk

FireHawk is a powerful tool designed for security professionals, ethical hackers, and developers to identify and exploit vulnerabilities in Firebase databases.

## Installation

### Termux

To install FireHawk on Termux, follow these steps:

   ```
pkg install git python
git clone https://github.com/iamunixtz/FireHawk.git
cd FireHawk
pip install -r requirements.txt
   ```

### Kali Linux / macOS
```
sudo apt-get install git python3
git clone https://github.com/iamunixtz/FireHawk.git
cd FireHawk
pip3 install -r requirements.txt
   ```
### POc
![Firehawk](https://github.com/iamunixtz/FireHawk/raw/main/Firehawk.jpg)

## Usage
- `-u URL, --url URL`: Specify the target Firebase URL.
- `-j JSON_FILE, --json JSON_FILE`: Provide a custom JSON file for exploitation.
- `-l, --list`: List Firebase database URLs from a file.
- `-o OUTPUT_FILE, --output OUTPUT_FILE`: Save vulnerable Firebase URLs to a file.
- `add`: Install FireHawk as a system-wide command.

## Contributing

Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests.

## License

This project is licensed under the [MIT License](LICENSE). and Inspired By
[securebinary]

-

