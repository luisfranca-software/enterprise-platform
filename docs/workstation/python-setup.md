# Python 3.14 Setup

## Install Python 3.14

### Ubuntu 26.04 (native or WSL2)

```bash
# Python 3.14 is available in the Ubuntu 26.04 repositories
sudo apt install -y python3.14 python3.14-venv python3.14-dev python3-pip
```

### Using deadsnakes PPA (if not in default repos)

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.14 python3.14-venv python3.14-dev
```

## Verify

```bash
python3.14 --version
# Python 3.14.x
```

## Virtual Environment

This project uses Python's built-in `venv` for environment isolation. Never install project dependencies globally.

### Creating a virtual environment

```bash
# From the project root
python3.14 -m venv .venv

# Activate
source .venv/bin/activate

# Verify
which python
# /home/user/projects/enterprise-platform/.venv/bin/python
```

### Installing project dependencies

```bash
# With the virtual environment activated
pip install -r implementation/backend/requirements/dev.txt
```

### Deactivating

```bash
deactivate
```

## Default Python (optional)

To make `python3` point to Python 3.14:

```bash
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.14 1
```

> **Note:** never replace the system `python3` on Ubuntu if it is required by the OS package manager. The `update-alternatives` approach above is safe.
