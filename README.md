# dirsearch — Simple Directory & File Enumerator

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-orange.svg)](#)

**⚠️ WARNING:** This tool can be dangerous if misused.
**Do NOT use it against systems you don’t own or don’t have explicit permission to test.**
The author takes **no responsibility** for any illegal or unauthorized use.

---

## Description

A lightweight custom dirsearch-like tool written in Python to discover directories and files on web servers.
All required files are included — just clone or download this repository and run.

---

## Requirements

* Python 3.x
* (Optional) Install dependencies if `requirements.txt` exists:

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python dirsearch.py <target_url> [options]
```

### Quick example

```bash
python dirsearch.py http://example.com/ -ext:.php,.js -t:0.5 -no
```

---

## 🧾 Arguments & Options (copy-friendly)

Use flags with the format `-flag:value` (no spaces around the colon).
Below are the supported arguments, a short description, and ready-to-copy examples.

| Flag             | Type   | Description                                                 |                                                      |
| ---------------- | ------ | ----------------------------------------------------------- | ---------------------------------------------------- |
| `-start:<int>`   | int    | Resume scan from a specific wordlist index.                 |                                                      |
| `-code:<int>`    | int    | Show this HTTP status code in results (in addition to 200). |                                                      |
| `-ext:<str or csv>`  | string                                                      | Comma-separated extensions to use (e.g. `.php,.js`). |
| `-nex:<str>`     | string | Replace shown extension with this one (e.g. `jsp`).         |                                                      |
| `-w:<path>`      | path   | Path to a custom wordlist file.                             |                                                      |
| `-exclude:<str>` | string | Exclude extension(s) from the wordlist (e.g. `html`).       |                                                      |
| `-exc:<int>`     | int    | Exclude this HTTP status code from display.                 |                                                      |
| `-t:<float>`     | float  | Delay (seconds) between requests. Default `0`.              |                                                      |
| `-find:<str>`    | string | Only include words that **contain** this substring.         |                                                      |
| `-nofind:<str>`  | string | Exclude words that **contain** this substring.              |                                                      |
| `-all`           | flag   | Show all status codes **except** `404`.                     |                                                      |
| `-no`            | flag   | Do **not** write a log file.                                |                                                      |
| `-api`           | flag   | Use built-in `api` default wordlist.                        |                                                      |

---

### Quick copyable examples (one-line each)

Resume at index 400, include 403 responses, and skip logging:

```bash
python dirsearch.py http://example.com/ -start:400 -code:403 -ext:.js,.php,.json -exclude:html -no
```

Use a custom wordlist, replace extension shown as `jsp`, and add a 2.5s delay:

```bash
python dirsearch.py http://example.com/ -w:./wordlists/my.txt -ext:php -nex:jsp -t:2.5 -all -no
```

Scan using the built-in API wordlist and include only words containing `admin`:

```bash
python dirsearch.py http://example.com/ -api -find:admin
```

Exclude 500 responses and do not log:

```bash
python dirsearch.py http://example.com/ -exc:500 -no
```

---

### Full template (copy & paste and change values)

```bash
python dirsearch.py <TARGET_URL> -start:0 -code:403 -ext:.php,.js -nex:jsp -w:./wordlists/words.txt -exclude:html -exc:500 -t:0.5 -find:api -nofind:test -all -no -api
```

> Tip: If you only want a subset of flags, remove the rest. Example minimal usage:

```bash
python dirsearch.py http://example.com/ -ext:.php -w:./wordlists/small.txt -t:1.0
```

---

### Notes & aliases

* Flags that are "boolean" (no value) are listed as `-all`, `-no`, and `-api`. Do not add `:true` or `:1` — just include the flag.
* Use sensible `-t` values (e.g., `0.5`, `1`, `2.5`) to avoid overloading targets.

---

## Logging

* If logging is enabled (no `-no` flag), results are written to a log file (check `dirsearch.py` for the exact path and filename).
* Add `.log` or the log filename to `.gitignore` before pushing to GitHub.

---

## Security Best Practices

* Always obtain **written permission** before testing any target.
* Use a reasonable request delay (`-t`) to avoid overloading servers.
* Set a clear custom **User-Agent** string to help identify authorized testing activity.

---

## Legal Notice

This project is for **educational and authorized security testing purposes only**.
You are solely responsible for compliance with local laws.
If you discover vulnerabilities, follow responsible disclosure practices and notify the system owner.

---

## License

This project is provided under the **MIT License**. See the `LICENSE` file for full text.
You are free to use, modify, and distribute this tool, but **without any warranty**.

---

## Contributing

* Keep contributions focused on security, safety, and reliability.
* If you add features that could be misused, document safe usage and include clear warnings.
* Submit issues or pull requests with detailed explanations and test cases.

---


---

## Final Note

This tool is meant to help security researchers and bug bounty hunters improve web security — **not to cause harm**. Use it responsibly, get permission before testing, and follow ethical disclosure practices.
Happy hunting!
