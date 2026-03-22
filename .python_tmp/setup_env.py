import subprocess
import os

workspace = '/workspace/agent_workspace'

# Initialize git repo
subprocess.run(['git', 'init'], cwd=workspace, capture_output=True)
subprocess.run(['git', 'config', 'user.email', 'agent@example.com'], cwd=workspace, capture_output=True)
subprocess.run(['git', 'config', 'user.name', 'Agent'], cwd=workspace, capture_output=True)

# Create main branch first
subprocess.run(['git', 'checkout', '-b', 'main'], cwd=workspace, capture_output=True)

# Create some Python files with TODO comments
files = {
    'module_a.py': '''"""Module A - Data processing utilities."""

import json

def process_data(data):
    """Process input data and return transformed result."""
    # TODO: Add input validation for empty data
    # TODO: Implement caching mechanism for repeated calls
    return [x * 2 for x in data]

def validate_input(data):
    """Validate input data format."""
    # TODO - Implement proper schema validation
    if not isinstance(data, list):
        return False
    return True

class DataProcessor:
    """Data processor class."""
    
    def __init__(self, config):
        # TODO: Load config from file instead of hardcoding
        self.config = config
    
    def run(self):
        """Run the data processor."""
        # TODO(warning): Handle network timeout gracefully
        # TODO(future): Add support for batch processing
        pass
''',
    'module_b.py': '''"""Module B - Network utilities."""

import requests

# TODO: Add retry logic for failed requests
# TODO(bug): Fix memory leak in connection pool

def fetch_data(url):
    """Fetch data from URL."""
    # TODO: Add timeout parameter
    # TODO: Handle SSL certificate errors
    pass

def post_data(url, payload):
    """Post data to URL."""
    # TODO - Implement request signing
    pass
''',
    'utils/helpers.py': '''"""Helper utilities."""

# TODO add support for multi-threading
# TODO(bugfix): Race condition in concurrent access

def format_output(result):
    """Format result for display."""
    # TODO: Support custom formatting templates
    return str(result)
''',
    'tests/test_module_a.py': '''"""Tests for Module A."""

# TODO: Add more test cases
# TODO: Mock external dependencies

def test_process_data():
    # TODO: Test edge cases
    pass
'''
}

# Create directory structure
os.makedirs(os.path.join(workspace, 'utils'), exist_ok=True)
os.makedirs(os.path.join(workspace, 'tests'), exist_ok=True)

# Write files
for filename, content in files.items():
    filepath = os.path.join(workspace, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Created {filename}")

# Create initial README
readme_content = '''# LUFFY Project

## Current TODO Items

No TODO items found.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Refer to individual module documentation.
'''
with open(os.path.join(workspace, 'README.md'), 'w') as f:
    f.write(readme_content)

print("\nCreated README.md")

# Create initial commit on main
subprocess.run(['git', 'add', '.'], cwd=workspace, capture_output=True)
subprocess.run(['git', 'commit', '-m', 'Initial commit with project structure'], cwd=workspace, capture_output=True)

# Create dev branch with additional TODOs
subprocess.run(['git', 'checkout', '-b', 'dev'], cwd=workspace, capture_output=True)

# Update module_a.py with additional TODOs for dev branch
dev_module_a = '''"""Module A - Data processing utilities."""

import json

def process_data(data):
    """Process input data and return transformed result."""
    # TODO: Add input validation for empty data
    # TODO: Implement caching mechanism for repeated calls
    # TODO(dev): Add support for streaming data processing
    return [x * 2 for x in data]

def validate_input(data):
    """Validate input data format."""
    # TODO - Implement proper schema validation
    # TODO(dev): Add type hints
    if not isinstance(data, list):
        return False
    return True

def transform_data(data, options=None):
    """Transform data with given options."""
    # TODO(dev): Implement option handling
    pass

class DataProcessor:
    """Data processor class."""
    
    def __init__(self, config):
        # TODO: Load config from file instead of hardcoding
        # TODO(dev): Add validation for config parameters
        self.config = config
    
    def run(self):
        """Run the data processor."""
        # TODO(warning): Handle network timeout gracefully
        # TODO(future): Add support for batch processing
        # TODO(dev): Implement error recovery
        pass
    
    def shutdown(self):
        # TODO(dev): Graceful shutdown implementation
        pass
'''

with open(os.path.join(workspace, 'module_a.py'), 'w') as f:
    f.write(dev_module_a)

# Update module_b.py for dev branch
dev_module_b = '''"""Module B - Network utilities."""

import requests

# TODO: Add retry logic for failed requests
# TODO(bug): Fix memory leak in connection pool
# TODO(dev): Add connection pooling configuration

def fetch_data(url, timeout=30):
    """Fetch data from URL."""
    # TODO: Add timeout parameter
    # TODO: Handle SSL certificate errors
    # TODO(dev): Implement exponential backoff
    pass

def post_data(url, payload):
    """Post data to URL."""
    # TODO - Implement request signing
    # TODO(dev): Add response compression support
    pass

def batch_request(urls):
    """Fetch multiple URLs in parallel."""
    # TODO(dev): Implement concurrent batch processing
    pass
'''

with open(os.path.join(workspace, 'module_b.py'), 'w') as f:
    f.write(dev_module_b)

# Commit dev changes
subprocess.run(['git', 'add', '.'], cwd=workspace, capture_output=True)
subprocess.run(['git', 'commit', '-m', 'Add dev branch features'], cwd=workspace, capture_output=True)

# Verify branches
result = subprocess.run(['git', 'branch', '-a'], cwd=workspace, capture_output=True, text=True)
print(f"\nBranches created:\n{result.stdout}")

# Show git log
result = subprocess.run(['git', 'log', '--oneline'], cwd=workspace, capture_output=True, text=True)
print(f"\nGit log:\n{result.stdout}")
