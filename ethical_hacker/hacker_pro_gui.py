#!/usr/bin/env python3
"""
Ethical Hacker Pro GUI - World's Deadliest Ethical Hacking Tool Suite GUI
Professional penetration testing interface with all hacking tools
Author: Security Research
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox, Canvas
import threading
import json
import sqlite3
from datetime import datetime
import webbrowser
import os
import subprocess
import sys
from hacker_pro import EthicalHackerPro, Colors

class HackerProGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("HACKER PRO - World's Deadliest Ethical Hacking Tool Suite")
        self.root.geometry("1600x1000")
        self.root.configure(bg='#0a0a0a')
        
        # Initialize scanner
        self.scanner = EthicalHackerPro()
        self.is_attacking = False
        self.current_attack_thread = None
        
        # Setup GUI
        self.setup_styles()
        self.create_widgets()
        self.center_window()
        
    def setup_styles(self):
        """Setup dark hacker theme styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure dark theme colors
        style.configure('TFrame', background='#1a1a1a')
        style.configure('TLabel', background='#1a1a1a', foreground='#00ff00')
        style.configure('TButton', background='#2a2a2a', foreground='#00ff00')
        style.map('TButton', background=[('active', '#3a3a3a')])
        style.configure('TCombobox', fieldbackground='#2a2a2a', background='#2a2a2a', foreground='#00ff00')
        style.configure('TEntry', fieldbackground='#2a2a2a', foreground='#00ff00')
        style.configure('TCheckbutton', background='#1a1a1a', foreground='#00ff00')
        style.configure('TRadiobutton', background='#1a1a1a', foreground='#00ff00')
        style.configure('TLabelframe', background='#1a1a1a', foreground='#00ff00')
        style.configure('TLabelframe.Label', background='#1a1a1a', foreground='#00ff00')
    
    def create_widgets(self):
        """Create all GUI widgets"""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title with animation
        self.create_animated_title(main_frame)
        
        # Target Configuration
        target_frame = ttk.LabelFrame(main_frame, text="TARGET CONFIGURATION", padding="10")
        target_frame.grid(row=1, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=(0, 10))
        
        tk.Label(target_frame, text="Target IP/URL:", bg='#1a1a1a', fg='#00ff00', font=("Courier", 10, "bold")).grid(row=0, column=0, sticky=tk.W)
        self.target_var = tk.StringVar()
        self.target_entry = ttk.Entry(target_frame, textvariable=self.target_var, width=60, font=("Courier", 10))
        self.target_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(10, 0))
        
        tk.Label(target_frame, text="Interface:", bg='#1a1a1a', fg='#00ff00', font=("Courier", 10, "bold")).grid(row=1, column=0, sticky=tk.W, pady=(10, 0))
        self.interface_var = tk.StringVar()
        self.interface_entry = ttk.Entry(target_frame, textvariable=self.interface_var, width=60, font=("Courier", 10))
        self.interface_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(10, 0), pady=(10, 0))
        
        # Attack Configuration
        config_frame = ttk.LabelFrame(main_frame, text="ATTACK CONFIGURATION", padding="10")
        config_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        tk.Label(config_frame, text="Threads:", bg='#1a1a1a', fg='#00ff00', font=("Courier", 10, "bold")).grid(row=0, column=0, sticky=tk.W)
        self.threads_var = tk.StringVar(value="100")
        self.threads_spinbox = ttk.Spinbox(config_frame, from_=1, to=500, textvariable=self.threads_var, width=10)
        self.threads_spinbox.grid(row=0, column=1, sticky=tk.W, padx=(10, 0))
        
        tk.Label(config_frame, text="Timeout:", bg='#1a1a1a', fg='#00ff00', font=("Courier", 10, "bold")).grid(row=0, column=2, sticky=tk.W, padx=(20, 0))
        self.timeout_var = tk.StringVar(value="10")
        self.timeout_spinbox = ttk.Spinbox(config_frame, from_=1, to=60, textvariable=self.timeout_var, width=10)
        self.timeout_spinbox.grid(row=0, column=3, sticky=tk.W, padx=(10, 0))
        
        # Network Exploitation Tools
        network_frame = ttk.LabelFrame(main_frame, text="NETWORK EXPLOITATION", padding="10")
        network_frame.grid(row=2, column=2, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.attack_vars = {
            'port_scan': tk.BooleanVar(value=True),
            'sniff': tk.BooleanVar(value=False),
            'arp_spoof': tk.BooleanVar(value=False),
            'mitm': tk.BooleanVar(value=False),
            'wifi_scan': tk.BooleanVar(value=False),
            'deauth': tk.BooleanVar(value=False)
        }
        
        network_tools = [
            ("Advanced Port Scan", 'port_scan', "Critical"),
            ("Network Sniffer", 'sniff', "High"),
            ("ARP Spoofing", 'arp_spoof', "High"),
            ("MITM Attack", 'mitm', "Critical"),
            ("WiFi Scanner", 'wifi_scan', "Medium"),
            ("Deauth Attack", 'deauth', "High")
        ]
        
        for i, (name, key, severity) in enumerate(network_tools):
            cb = ttk.Checkbutton(network_frame, text=f"{name} ({severity})", variable=self.attack_vars[key])
            cb.grid(row=i//2, column=(i%2)*2, sticky=tk.W, padx=(0, 20))
        
        # Web Application Tools
        web_frame = ttk.LabelFrame(main_frame, text="WEB APPLICATION ATTACKS", padding="10")
        web_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.web_vars = {
            'sqli': tk.BooleanVar(value=True),
            'xss': tk.BooleanVar(value=True),
            'dir_brute': tk.BooleanVar(value=True),
            'csrf': tk.BooleanVar(value=False),
            'ssrf': tk.BooleanVar(value=False)
        }
        
        web_tools = [
            ("SQL Injection", 'sqli', "Critical"),
            ("Cross-Site Scripting", 'xss', "High"),
            ("Directory Brute Force", 'dir_brute', "Medium"),
            ("CSRF Testing", 'csrf', "Medium"),
            ("SSRF Testing", 'ssrf', "High")
        ]
        
        for i, (name, key, severity) in enumerate(web_tools):
            cb = ttk.Checkbutton(web_frame, text=f"{name} ({severity})", variable=self.web_vars[key])
            cb.grid(row=i//2, column=(i%2)*2, sticky=tk.W, padx=(0, 20))
        
        # Password & Crypto Tools
        crypto_frame = ttk.LabelFrame(main_frame, text="PASSWORD & CRYPTO", padding="10")
        crypto_frame.grid(row=3, column=2, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.crypto_vars = {
            'password_crack': tk.BooleanVar(value=False),
            'ssh_brute': tk.BooleanVar(value=False),
            'hash_crack': tk.BooleanVar(value=False)
        }
        
        crypto_tools = [
            ("Password Cracker", 'password_crack', "High"),
            ("SSH Brute Force", 'ssh_brute', "Critical"),
            ("Hash Cracker", 'hash_crack', "Medium")
        ]
        
        for i, (name, key, severity) in enumerate(crypto_tools):
            cb = ttk.Checkbutton(crypto_frame, text=f"{name} ({severity})", variable=self.crypto_vars[key])
            cb.grid(row=i, column=0, sticky=tk.W, padx=(0, 20))
        
        # Social Engineering Tools
        social_frame = ttk.LabelFrame(main_frame, text="SOCIAL ENGINEERING", padding="10")
        social_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.social_vars = {
            'phishing': tk.BooleanVar(value=False),
            'email_spoof': tk.BooleanVar(value=False)
        }
        
        social_tools = [
            ("Phishing Generator", 'phishing', "High"),
            ("Email Spoofing", 'email_spoof', "Medium")
        ]
        
        for i, (name, key, severity) in enumerate(social_tools):
            cb = ttk.Checkbutton(social_frame, text=f"{name} ({severity})", variable=self.social_vars[key])
            cb.grid(row=i, column=0, sticky=tk.W, padx=(0, 20))
        
        # Control Buttons
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=4, column=2, columnspan=2, pady=(0, 10))
        
        self.start_btn = ttk.Button(control_frame, text="START ATTACK", command=self.start_attack, width=20)
        self.start_btn.grid(row=0, column=0, padx=(0, 5))
        
        self.stop_btn = ttk.Button(control_frame, text="STOP ATTACK", command=self.stop_attack, width=20, state="disabled")
        self.stop_btn.grid(row=0, column=1, padx=(5, 0))
        
        ttk.Button(control_frame, text="COMPREHENSIVE SCAN", command=self.comprehensive_scan, width=20).grid(row=1, column=0, padx=(0, 5), pady=(10, 0))
        ttk.Button(control_frame, text="GENERATE REPORT", command=self.generate_report, width=20).grid(row=1, column=1, padx=(5, 0), pady=(10, 0))
        
        # Statistics Display
        stats_frame = ttk.LabelFrame(main_frame, text="ATTACK STATISTICS", padding="10")
        stats_frame.grid(row=5, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.stats_labels = {}
        stats = ['Critical', 'High', 'Medium', 'Low', 'Info', 'Credentials']
        colors = ['#ff0000', '#ff8800', '#ffff00', '#00ff00', '#00ffff', '#ff00ff']
        
        for i, (stat, color) in enumerate(zip(stats, colors)):
            label = tk.Label(stats_frame, text=f"{stat}: 0", bg='#1a1a1a', fg=color, font=("Courier", 12, "bold"))
            label.grid(row=i//3, column=(i%3)*2, sticky=tk.W, padx=(0, 20), pady=(0, 5))
            self.stats_labels[stat.lower()] = label
        
        # Results Display
        results_frame = ttk.LabelFrame(main_frame, text="ATTACK RESULTS", padding="10")
        results_frame.grid(row=6, column=0, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Create Treeview for results
        columns = ('ID', 'Type', 'Severity', 'Target', 'Description')
        self.results_tree = ttk.Treeview(results_frame, columns=columns, show='headings', height=12)
        
        # Configure columns
        self.results_tree.heading('ID', text='ID')
        self.results_tree.heading('Type', text='Type')
        self.results_tree.heading('Severity', text='Severity')
        self.results_tree.heading('Target', text='Target')
        self.results_tree.heading('Description', text='Description')
        
        # Column widths
        self.results_tree.column('ID', width=80)
        self.results_tree.column('Type', width=150)
        self.results_tree.column('Severity', width=80)
        self.results_tree.column('Target', width=200)
        self.results_tree.column('Description', width=300)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.results_tree.yview)
        self.results_tree.configure(yscrollcommand=scrollbar.set)
        
        self.results_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Bind double-click for details
        self.results_tree.bind('<Double-1>', self.show_attack_details)
        
        # Attack Log
        log_frame = ttk.LabelFrame(main_frame, text="ATTACK LOG", padding="10")
        log_frame.grid(row=7, column=0, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=8, width=160, 
                                                bg='#0a0a0a', fg='#00ff00', 
                                                font=("Courier", 9))
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(6, weight=1)
        main_frame.rowconfigure(7, weight=1)
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
    
    def create_animated_title(self, parent):
        """Create animated title with matrix effect"""
        title_frame = ttk.Frame(parent)
        title_frame.grid(row=0, column=0, columnspan=4, pady=(0, 20))
        
        # Create canvas for animation
        canvas = Canvas(title_frame, width=1400, height=80, bg='#0a0a0a', highlightthickness=0)
        canvas.pack()
        
        # Static title
        canvas.create_text(700, 30, text="HACKER PRO", 
                         font=("Courier", 24, "bold"), fill='#00ff00')
        canvas.create_text(700, 55, text="World's Deadliest Ethical Hacking Tool Suite", 
                         font=("Courier", 12), fill='#00ff00')
        
        # Matrix rain effect (simplified)
        self.matrix_chars = "01"
        self.matrix_items = []
        
        for i in range(50):
            x = random.randint(0, 1400)
            y = random.randint(0, 80)
            char = random.choice(self.matrix_chars)
            item = canvas.create_text(x, y, text=char, font=("Courier", 8), fill='#00ff00')
            self.matrix_items.append(item)
        
        # Start animation
        self.animate_matrix(canvas)
    
    def animate_matrix(self, canvas):
        """Animate matrix rain effect"""
        for item in self.matrix_items:
            coords = canvas.coords(item)
            if coords:
                x, y = coords
                y += 2
                if y > 80:
                    y = 0
                    x = random.randint(0, 1400)
                    canvas.itemconfig(item, text=random.choice(self.matrix_chars))
                canvas.coords(item, x, y)
        
        self.root.after(100, lambda: self.animate_matrix(canvas))
    
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def log_message(self, message, level="info"):
        """Add message to log with color coding"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Color based on level
        if level == "success":
            color = "#00ff00"
        elif level == "warning":
            color = "#ffff00"
        elif level == "error":
            color = "#ff0000"
        elif level == "critical":
            color = "#ff00ff"
        else:
            color = "#00ffff"
        
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n", color)
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def start_attack(self):
        """Start selected attacks"""
        if self.is_attacking:
            return
        
        target = self.target_var.get().strip()
        interface = self.interface_var.get().strip()
        
        if not target and not interface:
            messagebox.showwarning("Warning", "Please enter a target IP/URL or interface")
            return
        
        # Safety confirmation
        result = messagebox.askyesno("WARNING", 
                                     "This is a powerful ethical hacking tool suite.\n"
                                     "Only use on targets you own or have explicit permission.\n\n"
                                     "Do you understand and accept full responsibility?")
        if not result:
            return
        
        # Update scanner config
        self.scanner.config['threads'] = int(self.threads_var.get())
        self.scanner.config['timeout'] = int(self.timeout_var.get())
        
        # Clear previous results
        self.scanner.vulnerabilities = []
        self.scanner.credentials = []
        self.results_tree.delete(*self.results_tree.get_children())
        self.update_statistics()
        
        # Update UI
        self.is_attacking = True
        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        
        self.log_message("Starting attack sequence...", "info")
        
        # Start attacks in background thread
        self.current_attack_thread = threading.Thread(target=self.run_attacks, args=(target, interface))
        self.current_attack_thread.daemon = True
        self.current_attack_thread.start()
    
    def run_attacks(self, target, interface):
        """Run selected attacks in background"""
        try:
            # Network Exploitation
            if target and self.attack_vars['port_scan'].get():
                self.root.after(0, lambda: self.log_message("Starting advanced port scan...", "info"))
                self.scanner.advanced_port_scan(target)
                self.root.after(0, self.update_results)
            
            if interface and self.attack_vars['sniff'].get():
                self.root.after(0, lambda: self.log_message("Starting network sniffer...", "info"))
                self.scanner.network_sniffer(interface, duration=30)
                self.root.after(0, self.update_results)
            
            if target and interface and self.attack_vars['arp_spoof'].get():
                self.root.after(0, lambda: self.log_message("Starting ARP spoofing...", "warning"))
                # Run for limited time
                spoof_thread = threading.Thread(target=self.scanner.arp_spoof, args=(target, "192.168.1.1", interface))
                spoof_thread.daemon = True
                spoof_thread.start()
                spoof_thread.join(timeout=30)
                self.root.after(0, self.update_results)
            
            if target and interface and self.attack_vars['mitm'].get():
                self.root.after(0, lambda: self.log_message("Starting MITM attack...", "critical"))
                self.scanner.mitm_attack(interface, target)
                self.root.after(0, self.update_results)
            
            if interface and self.attack_vars['wifi_scan'].get():
                self.root.after(0, lambda: self.log_message("Starting WiFi scanner...", "info"))
                self.scanner.wifi_scanner(interface)
                self.root.after(0, self.update_results)
            
            if interface and self.attack_vars['deauth'].get():
                self.root.after(0, lambda: self.log_message("Starting deauth attack...", "warning"))
                self.scanner.deauth_attack(interface, "AA:BB:CC:DD:EE:FF")
                self.root.after(0, self.update_results)
            
            # Web Application Attacks
            if target and self.web_vars['sqli'].get():
                self.root.after(0, lambda: self.log_message("Starting SQL injection...", "critical"))
                self.scanner.sql_injection_advanced(target)
                self.root.after(0, self.update_results)
            
            if target and self.web_vars['xss'].get():
                self.root.after(0, lambda: self.log_message("Starting XSS testing...", "warning"))
                self.scanner.xss_advanced(target)
                self.root.after(0, self.update_results)
            
            if target and self.web_vars['dir_brute'].get():
                self.root.after(0, lambda: self.log_message("Starting directory brute force...", "info"))
                self.scanner.directory_bruteforce(target)
                self.root.after(0, self.update_results)
            
            # Password & Crypto Attacks
            if self.crypto_vars['password_crack'].get():
                self.root.after(0, lambda: self.log_message("Starting password cracker...", "warning"))
                # Example hash cracking
                self.scanner.password_cracker('md5', '5f4dcc3b5aa765d61d8327deb882cf99')
                self.root.after(0, self.update_results)
            
            if target and self.crypto_vars['ssh_brute'].get():
                self.root.after(0, lambda: self.log_message("Starting SSH brute force...", "critical"))
                self.scanner.ssh_bruteforce(target, 'root')
                self.root.after(0, self.update_results)
            
            # Social Engineering
            if self.social_vars['phishing'].get():
                self.root.after(0, lambda: self.log_message("Generating phishing page...", "warning"))
                self.scanner.phishing_generator("http://evil.com", target)
                self.root.after(0, self.update_results)
            
            self.root.after(0, lambda: self.log_message("Attack sequence completed!", "success"))
            
        except Exception as e:
            self.root.after(0, lambda: self.log_message(f"Attack error: {e}", "error"))
        finally:
            self.root.after(0, self.attack_completed)
    
    def stop_attack(self):
        """Stop current attacks"""
        self.is_attacking = False
        self.log_message("Attacks stopped by user", "warning")
        self.attack_completed()
    
    def attack_completed(self):
        """Handle attack completion"""
        self.is_attacking = False
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        
        # Update statistics
        self.update_statistics()
        
        # Show summary
        total_vulns = len(self.scanner.vulnerabilities)
        total_creds = len(self.scanner.credentials)
        self.log_message(f"Attacks completed! Found {total_vulns} vulnerabilities, {total_creds} credentials", "success")
    
    def comprehensive_scan(self):
        """Run comprehensive penetration test"""
        target = self.target_var.get().strip()
        
        if not target:
            messagebox.showwarning("Warning", "Please enter a target IP/URL")
            return
        
        # Safety confirmation
        result = messagebox.askyesno("Comprehensive Scan", 
                                     "This will run ALL available attacks on the target.\n"
                                     "Only use on targets you own or have explicit permission.\n\n"
                                     "Continue with comprehensive scan?")
        if not result:
            return
        
        # Clear previous results
        self.scanner.vulnerabilities = []
        self.scanner.credentials = []
        self.results_tree.delete(*self.results_tree.get_children())
        
        # Update UI
        self.is_attacking = True
        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        
        self.log_message("Starting comprehensive penetration test...", "critical")
        
        # Start comprehensive scan
        scan_thread = threading.Thread(target=self.scanner.run_comprehensive_scan, args=(target,))
        scan_thread.daemon = True
        scan_thread.start()
    
    def update_results(self):
        """Update results treeview"""
        # Clear existing items
        self.results_tree.delete(*self.results_tree.get_children())
        
        # Add vulnerabilities
        for vuln in self.scanner.vulnerabilities:
            # Truncate long values for display
            target = vuln['target'][:40] + "..." if len(vuln['target']) > 40 else vuln['target']
            description = vuln['description'][:50] + "..." if len(vuln['description']) > 50 else vuln['description']
            
            self.results_tree.insert('', 'end', values=(
                vuln['id'],
                vuln['type'],
                vuln['severity'],
                target,
                description
            ))
        
        # Add credentials
        for cred in self.scanner.credentials:
            self.results_tree.insert('', 'end', values=(
                cred['id'],
                "Credential Found",
                "Critical",
                f"{cred['service']}@{cred['target']}",
                f"{cred['username']}:{cred['password']}"
            ))
        
        # Update statistics
        self.update_statistics()
    
    def update_statistics(self):
        """Update statistics labels"""
        summary = self.scanner.generate_summary()
        
        self.stats_labels['critical'].config(text=f"Critical: {summary['critical']}")
        self.stats_labels['high'].config(text=f"High: {summary['high']}")
        self.stats_labels['medium'].config(text=f"Medium: {summary['medium']}")
        self.stats_labels['low'].config(text=f"Low: {summary['low']}")
        self.stats_labels['info'].config(text=f"Info: {summary['info']}")
        self.stats_labels['credentials'].config(text=f"Credentials: {len(self.scanner.credentials)}")
    
    def show_attack_details(self, event):
        """Show detailed attack information"""
        selection = self.results_tree.selection()
        if not selection:
            return
        
        item = self.results_tree.item(selection[0])
        values = item['values']
        
        # Find vulnerability or credential
        vuln_id = values[0]
        vuln = None
        cred = None
        
        for v in self.scanner.vulnerabilities:
            if v['id'] == vuln_id:
                vuln = v
                break
        
        if not vuln:
            for c in self.scanner.credentials:
                if c['id'] == vuln_id:
                    cred = c
                    break
        
        if vuln:
            self.show_vulnerability_dialog(vuln)
        elif cred:
            self.show_credential_dialog(cred)
    
    def show_vulnerability_dialog(self, vuln):
        """Show vulnerability details dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Vulnerability Details - {vuln['type']}")
        dialog.geometry("900x700")
        dialog.configure(bg='#0a0a0a')
        
        # Create scrolled text widget
        text_widget = scrolledtext.ScrolledText(dialog, wrap=tk.WORD, width=100, height=40,
                                             bg='#0a0a0a', fg='#00ff00', font=("Courier", 10))
        text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Format vulnerability details
        details = f"""
VULNERABILITY DETAILS
====================

ID: {vuln['id']}
Type: {vuln['type']}
Severity: {vuln['severity']}
Target: {vuln['target']}
Timestamp: {vuln['timestamp']}

DESCRIPTION
-----------
{vuln['description']}

EVIDENCE
--------
{vuln['evidence']}

REMEDIATION
-----------
{vuln['remediation']}

SEVERITY INFORMATION
====================
Critical: Immediate action required, system compromise possible
High: Significant risk, should be addressed immediately
Medium: Moderate risk, address in next update cycle
Low: Minor risk, address when convenient
Info: Informational finding, no immediate risk

ATTACK RECOMMENDATIONS
=====================
1. Verify vulnerability manually
2. Assess business impact
3. Implement remediation
4. Test fix effectiveness
5. Document findings for security team
"""
        
        text_widget.insert(tk.END, details)
        text_widget.config(state='disabled')
        
        # Center dialog
        dialog.update_idletasks()
        width = dialog.winfo_width()
        height = dialog.winfo_height()
        x = (dialog.winfo_screenwidth() // 2) - (width // 2)
        y = (dialog.winfo_screenheight() // 2) - (height // 2)
        dialog.geometry(f'{width}x{height}+{x}+{y}')
    
    def show_credential_dialog(self, cred):
        """Show credential details dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Credential Details")
        dialog.geometry("700x500")
        dialog.configure(bg='#0a0a0a')
        
        # Create scrolled text widget
        text_widget = scrolledtext.ScrolledText(dialog, wrap=tk.WORD, width=80, height=30,
                                             bg='#0a0a0a', fg='#00ff00', font=("Courier", 10))
        text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Format credential details
        details = f"""
CREDENTIAL DETAILS
==================

ID: {cred['id']}
Username: {cred['username']}
Password: {cred['password']}
Service: {cred['service']}
Target: {cred['target']}
Timestamp: {cred['timestamp']}

SECURITY IMPLICATIONS
===================
1. Weak password detected
2. Potential credential reuse
3. Service vulnerability
4. Immediate password change required

REMEDIATION STEPS
================
1. Change the compromised password immediately
2. Review password policy
3. Enable multi-factor authentication
4. Audit other accounts for password reuse
5. Implement account lockout policies

RECOMMENDATIONS
===============
1. Use strong, unique passwords
2. Enable 2FA/MFA where possible
3. Regular password rotation
4. Monitor for suspicious account activity
5. Educate users on password security
"""
        
        text_widget.insert(tk.END, details)
        text_widget.config(state='disabled')
        
        # Center dialog
        dialog.update_idletasks()
        width = dialog.winfo_width()
        height = dialog.winfo_height()
        x = (dialog.winfo_screenwidth() // 2) - (width // 2)
        y = (dialog.winfo_screenheight() // 2) - (height // 2)
        dialog.geometry(f'{width}x{height}+{x}+{y}')
    
    def generate_report(self):
        """Generate comprehensive security report"""
        if not self.scanner.vulnerabilities and not self.scanner.credentials:
            messagebox.showinfo("Info", "No results to report")
            return
        
        try:
            report = self.scanner.generate_report('json')
            self.scanner.generate_report('txt')
            
            self.log_message("Security reports generated successfully!", "success")
            messagebox.showinfo("Success", "Reports generated:\n- ethical_hacker_report.json\n- ethical_hacker_report.txt")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate report: {e}")
    
    def on_closing(self):
        """Handle window closing"""
        if self.is_attacking:
            if messagebox.askokcancel("Quit", "Attacks are running. Stop and quit?"):
                self.stop_attack()
                self.root.after(1000, self.root.destroy)
        else:
            self.root.destroy()

def main():
    """Main function"""
    root = tk.Tk()
    app = HackerProGUI(root)
    
    # Handle window closing
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    
    # Start GUI
    root.mainloop()

if __name__ == "__main__":
    main()
