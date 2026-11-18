# Learn TCP/IP with Python (Modernized Hyper-V Edition)

An updated, Infrastructure-as-Code (IaC) modernization of my 2018 TCP/IP networking lab. Refactored from a legacy VirtualBox + CentOS 7 setup to run natively on **Windows Hyper-V** with **Ubuntu 22.04 LTS**, **PowerShell automation**, and **Python 3 socket diagnostics**.

---

## Project Architecture & Modernization Highlights

| Component | Legacy 2018 Lab | Modernized Edition |
| :--- | :--- | :--- |
| **Hypervisor** | Oracle VirtualBox (Type-2) | **Windows Hyper-V (Type-1 Bare-Metal)** |
| **Guest OS** | CentOS 7 (EOL) | **Ubuntu 22.04 LTS (`generic/ubuntu2204`)** |
| **Resource Allocation** | Static 1024 MB RAM | **Dynamic Memory (1024 MB – 1536 MB) & 2 vCPUs** |
| **Automation** | Manual `vagrant up` | **One-click PowerShell launcher (`start-lab.ps1`)** |
| **Network Addressing** | Hardcoded static IP | **Dynamic DHCP via Hyper-V Default Switch** |

---

## Hybrid-Cloud & Certification Alignment (CCNA + AWS CLF-C02)

This local lab serves as the on-premises foundation for my multi-branch hybrid-cloud architecture (**`netgiocafe.ph`**):
* **Cisco CCNA Fundamentals:** Verifies TCP 3-way handshakes, dynamic DHCP addressing, DNS resolution (`dig`), packet capture (`tcpdump`), and path tracing (`traceroute`) using Python sockets.
* **AWS re/Start & Cloud Practitioner (CLF-C02):** Mirrors cloud-native Infrastructure as Code (CloudFormation/Vagrant), dynamic IP handling, least-privilege port verification, and resource-efficient FinOps sizing.

---

## Repository Structure

```text
learn-tcpip-with-python-hyperv/
├── README.md
└── python-basics/
    ├── Vagrantfile              # Hyper-V Ubuntu 22.04 LTS IaC definition
    ├── start-lab.ps1            # PowerShell launcher & external storage router
    └── scripts/
        └── tcpip_diag.py        # Python 3 TCP/IP port & dynamic IP diagnostic tool
```

---

## Quick Start (Windows Hyper-V)

1. Open **Windows PowerShell as Administrator**.
2. Clone this repository and navigate to `python-basics`:
   ```powershell
   git clone https://github.com<your-username>/learn-tcpip-with-python-hyperv.git
   cd learn-tcpip-with-python-hyperv\python-basics
   ```
3. Run the PowerShell launcher:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\start-lab.ps1
   ```
4. When prompted, choose **`Default Switch`**, then connect and run the diagnostic script:
   ```powershell
   vagrant ssh
   ``` 
