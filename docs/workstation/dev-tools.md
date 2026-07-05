# Development Tools

This guide covers the installation and configuration of Docker, Git, GitHub CLI, VS Code, and OpenCode.

---

## Docker

### Install Docker Engine

```bash
# Add Docker's official GPG key and repository
sudo apt update
sudo apt install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

### Post-install (non-root access)

```bash
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
```

### Verify

```bash
docker --version
docker compose version
```

---

## Git

```bash
sudo apt install -y git

git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global init.defaultBranch main
```

---

## GitHub CLI (`gh`)

```bash
# Install via apt
sudo apt install -y gh

# Authenticate
gh auth login
```

### Useful commands

```bash
gh repo view           # View the current repository
gh pr create           # Create a pull request
gh pr checkout <num>   # Check out a PR locally
gh run watch           # Watch CI/CD workflow runs
```

---

## VS Code

### Install

```bash
# Download and install the .deb package
wget -qO- https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64 -O /tmp/code.deb
sudo dpkg -i /tmp/code.deb
```

Or install via Snap:

```bash
sudo snap install code --classic
```

### Recommended Extensions

| Extension | ID | Purpose |
|-----------|----|---------|
| Python | `ms-python.python` | Python language support |
| Ruff | `charliermarsh.ruff` | Linting and formatting |
| Django | `batisteo.vscode-django` | Django template syntax |
| Docker | `ms-azuretools.vscode-docker` | Docker Compose management |
| YAML | `redhat.vscode-yaml` | YAML schema validation |
| GitHub Pull Requests | `github.vscode-pull-request-github` | PR review in-editor |

### Workspace Settings

When opening the project in VS Code, use **File > Open Workspace from File** and select the `.code-workspace` file (if present), or simply open the project root folder.

---

## OpenCode

OpenCode is the AI assistant used for implementation tasks in this project's development workflow.

### Installation

```bash
# Install via npm
npm install -g @opencode/cli

# Verify
opencode --version
```

### Usage

```bash
# Start an interactive session
opencode

# Run with a specific task
opencode "Add a health-check endpoint"
```

### Configuration

OpenCode reads the project's `AGENTS.md` file to understand project conventions. Ensure you are in the project root when running OpenCode so it can load the project context automatically.

See the [OpenCode documentation](https://opencode.ai) for detailed configuration options.
