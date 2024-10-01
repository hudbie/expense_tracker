#!/usr/bin/env python3
"""
Installation script for Expense Tracker
"""

import subprocess
import sys

def install_requirements():
    """Install required packages"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies. Please install manually:")
        print("pip install -r requirements.txt")

if __name__ == "__main__":
    install_requirements()