import os

# List the workspace directory
workspace_path = '/workspace/agent_workspace'
for item in os.listdir(workspace_path):
    full_path = os.path.join(workspace_path, item)
    if os.path.isdir(full_path):
        print(f"[DIR] {item}")
    else:
        print(f"[FILE] {item}")
