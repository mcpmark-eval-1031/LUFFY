import os

# Check if README exists and read it
readme_path = '/workspace/agent_workspace/README.md'
if os.path.exists(readme_path):
    print("README.md exists")
    with open(readme_path, 'r') as f:
        print(f.read()[:2000])
else:
    print("README.md not found")

# Check for .github_token
token_path = '/workspace/agent_workspace/.github_token'
if os.path.exists(token_path):
    print("\n.github_token exists")
    with open(token_path, 'r') as f:
        print(f.read())
