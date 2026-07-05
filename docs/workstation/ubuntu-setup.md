# Ubuntu 26.04 LTS Setup

## Installation

1. Download the Ubuntu 26.04 LTS ISO from [ubuntu.com](https://ubuntu.com/download/server).
2. Create a bootable USB drive or use it with your hypervisor of choice.
3. During installation, select:
   - **OpenSSH server** in the software selection step.
   - **Docker** if prompted (otherwise install manually — see [Dev Tools](dev-tools.md)).

## Post-Installation

```bash
# Update all packages
sudo apt update && sudo apt upgrade -y

# Install essential build tools
sudo apt install -y build-essential curl wget git ca-certificates gnupg lsb-release
```

## WSL2 (Windows Only)

If you are running Windows, install Ubuntu 26.04 LTS via WSL2:

```powershell
# In PowerShell (Admin)
wsl --install -d Ubuntu-26.04
```

After installation, launch Ubuntu from the Start menu and proceed with the Python and tool setup below.

## Firewall

```bash
sudo ufw allow OpenSSH
sudo ufw enable
```
