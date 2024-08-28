#!/usr/bin/env python3
"""
Script to install required dependencies
"""

import subprocess
import sys

def install_package(package):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✓ Successfully installed {package}")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install {package}")

def main():
    print("Installing required dependencies...")
    
    # Read requirements from file
    try:
        with open('requirements.txt', 'r') as f:
            packages = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        print("❌ requirements.txt not found")
        return
    
    for package in packages:
        install_package(package)
    
    print("\n✅ All dependencies installed successfully!")
    print("You can now run the expense tracker with: python expense_tracker.py")

if __name__ == "__main__":
    main()