import subprocess
import os

workspace = '/workspace/agent_workspace'

# Check if there's a .git directory
git_dir = os.path.join(workspace, '.git')
if os.path.exists(git_dir):
    print(".git directory exists")
    # Run git commands
    result = subprocess.run(['git', 'branch', '-a'], cwd=workspace, capture_output=True, text=True)
    print("Branches:", result.stdout)
    
    result = subprocess.run(['git', 'status'], cwd=workspace, capture_output=True, text=True)
    print("Status:", result.stdout)
else:
    print(".git directory NOT found")

# List all files recursively
print("\nFull directory listing:")
for root, dirs, files in os.walk(workspace):
    level = root.replace(workspace, '').count(os.sep)
    indent = ' ' * 2 * level
    print(f'{indent}{os.path.basename(root)}/')
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        print(f'{subindent}{file}')
