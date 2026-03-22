import subprocess
import os

workspace = '/workspace/agent_workspace'

# Read token
token_file = os.path.join(workspace, '.github_token')
with open(token_file, 'r') as f:
    token = f.read().strip()

# Update remote with token
remote_url = f'https://{token}@github.com/mcpmark-eval-1031/LUFFY.git'
subprocess.run(
    ['git', 'remote', 'set-url', 'origin', remote_url],
    cwd=workspace, capture_output=True
)

# Check status
result = subprocess.run(['git', 'status'], cwd=workspace, capture_output=True, text=True)
print(f"Status:\n{result.stdout}")

# Push main branch
result = subprocess.run(
    ['git', 'push', '-u', 'origin', 'main'],
    cwd=workspace, capture_output=True, text=True
)
print(f"\nPush main result: {result.returncode}")
print(f"stdout: {result.stdout}")
print(f"stderr: {result.stderr}")

# Push dev branch
result = subprocess.run(
    ['git', 'push', '-u', 'origin', 'dev'],
    cwd=workspace, capture_output=True, text=True
)
print(f"\nPush dev result: {result.returncode}")
print(f"stdout: {result.stdout}")
print(f"stderr: {result.stderr}")
