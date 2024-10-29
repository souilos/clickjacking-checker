# Clickjacking Checker

Find here is a simple script to check if your web app is vulnerable to clickjacking.

## Usage

```bash
git clone https://github.com/souilos/clickjacking-checker.git
cd clickjacking-checker
pip install requests & pip install termcolor
python3 clickjacking.py
```
If your web app is vulnerable the domain will generate a PoC in the same folder.

## Clickjacking Tricks Users into Revealing Sensitive Information

**What is clickjacking?**

Clickjacking is a vulnerability where users are tricked into clicking hidden or disguised elements on a webpage, leading to unintended actions. If exploited in production, attackers could trick users into unknowingly transferring funds, revealing private keys, or granting unauthorized access to sensitive data, resulting in financial loss or compromised account security.

## Vulnerability Details

```bash
[!] Missing security header: X-Frame-Options
```

The vulnerability arises from the absence of the X-Frame-Options HTTP headers in the server responses. The X-Frame-Options header is crucial for preventing clickjacking attacks, as it controls whether a browser is allowed to render a webpage within a `<frame>`, `<iframe>`, `<embed>`, or `<object>`. Without this protection, an attacker can embed the vulnerable webpage into a malicious site, tricking users into interacting with hidden or misleading elements (like buttons or forms) without their knowledge.

## Impact Details

**Phishing Attacks:** In a clickjacking scenario, attackers can overlay a malicious frame on top of a legitimate webpage, capturing sensitive information. For instance, they could disguise a login form or a wallet connection prompt, leading users to input their credentials or private keys unwittingly. Once the attacker obtains this sensitive data, they can access users' accounts, leading to theft of funds and personal information. They could also trick users into authorizing transactions without their knowledge, a user may think they are clicking a harmless button, but instead, they could be approving a fund transfer to the attacker’s wallet.

