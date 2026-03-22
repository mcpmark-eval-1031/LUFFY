import subprocess
import os

workspace = '/workspace/agent_workspace'

# Backup .github_token
token_file = os.path.join(workspace, '.github_token')
with open(token_file, 'r') as f:
    token = f.read().strip()

# Remove .git directory and reinitialize
subprocess.run(['rm', '-rf', '.git'], cwd=workspace, capture_output=True)

# Reinitialize
subprocess.run(['git', 'init'], cwd=workspace, capture_output=True)
subprocess.run(['git', 'config', 'user.email', 'agent@example.com'], cwd=workspace, capture_output=True)
subprocess.run(['git', 'config', 'user.name', 'Agent'], cwd=workspace, capture_output=True)

# Create .gitignore first to prevent tracking of .github_token
with open(os.path.join(workspace, '.gitignore'), 'w') as f:
    f.write('.github_token\n')

# Add all files except .github_token
subprocess.run(['git', 'add', '.'], cwd=workspace, capture_output=True)

# Create first commit on main
subprocess.run(['git', 'commit', '-m', 'Initial commit with project structure'], cwd=workspace, capture_output=True)

# Create dev branch
subprocess.run(['git', 'checkout', '-b', 'dev'], cwd=workspace, capture_output=True)

# Verify status
result = subprocess.run(['git', 'status'], cwd=workspace, capture_output=True, text=True)
print(f"Status:\n{result.stdout}")

result = subprocess.run(['git', 'log', '--oneline'], cwd=workspace, capture_output=True, text=True)
print(f"\nGit log:\n{result.stdout}")

# Check what's tracked
result = subprocess.run(['git', 'ls-files'], cwd=workspace, capture_output=True, text=True)
print(f"\nTracked files:\n{result.stdout}")
