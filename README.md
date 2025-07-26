# INFOPY

`INFOPY` is a lightweight Python OSINT tool that uses the [SecurityTrails API](https://securitytrails.com) to fetch **WHOIS data** and **subdomains** for a given domain.

---

## 📦 Features

- 🔍 Subdomain enumeration
- 📄 WHOIS record lookup
- ✅ Configurable via `config.yaml`
- 🧩 Simple CLI interface using `argparse`

---

## 📁 Requirements

- Python 3.6+
- `requests`
- `pyyaml`

Install dependencies:

```bash
pip install requests pyyaml
```
## ⚙️ Setup
- add your SecurityTrails API key into config.yaml file:

```yaml
apikey: your_securitytrails_api_key_here
```
## 🚀 Usage
```bash
python3 infopy.py -d example.com --whois
python3 infopy.py -d example.com --sub
```
## Arguments
| Flag      | Description              | Example          |
| --------- | ------------------------ | ---------------- |
| `-d`      | (Required) Target domain | `-d example.com` |
| `--whois` | Get WHOIS information    | `--whois`        |
| `--sub`   | Fetch list of subdomains | `--sub`          |
| `-o `     | Save output              | `-o result.txt`  |

## 🖨️ Example Output
- Subdomain Finder:
```bash
$ python3 infopy.py -d example.com --sub
api
mail
dev
www
[-] total subdomains: 4
```
- WHOIS Lookup:
```bash
$ python3 infopy.py -d example.com --whois
{
  "registrar": "Example Registrar",
  "created": "2000-01-01T00:00:00Z",
  ...
}
```
## 🛡️ Notes
- Uses the SecurityTrails API — you need a free or paid API key.
- API rate limits apply depending on your subscription.

## 📄 License
This project is open-source and free to use under the MIT License.
